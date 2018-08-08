## App Utilities
import os
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, current_app, request, redirect, url_for, flash
from flask_uploads import UploadSet, configure_uploads, IMAGES

import numpy as np
import keras
import h5py
from keras.models import load_model   

from skimage.io import imread
from skimage.transform import resize
     

## App Settings

app = Flask(__name__)
app.config['SECRET_KEY'] = 'BiggestSecret'
Bootstrap(app)
photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'static/uploads'
configure_uploads(app, photos)



############################################################################# VIEWS #####################################################################################################################################
    
    
### MAIN PAGE


@app.route('/')    
@app.route('/classifier', methods=['GET', 'POST'])
def classifier():
    
    return render_template("classifier.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        image_classifier = load_model('my_classifier.h5')
        class_labels = {0:'Cat', 1:'Dog'}
        img = imread(request.files['photo']) 
        img = resize(img,(96,96))
        img = np.expand_dims(img,axis=0)
        if(np.max(img)>1):
            img = img/255.0
        prediction = image_classifier.predict_classes(img)
        guess = class_labels[prediction[0][0]]
        keras.backend.clear_session()
        
        return render_template("guess.html", guess = guess)
    

    



## APP INITIATION

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 
            