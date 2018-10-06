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
photos = UploadSet('photos', IMAGES)                                            ## image upload handling
app.config['UPLOADED_PHOTOS_DEST'] = 'static/uploads'
configure_uploads(app, photos)



############################################################################# VIEWS #####################################################################################################################################
    
    
### MAIN PAGE


@app.route('/')    
@app.route('/classifier', methods=['GET', 'POST'])
def classifier():
    
    return render_template("classifier.html")


### TEST PHOTO


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        keras.backend.clear_session()                                           ## clear Tensor session to avoid error
        image_classifier = load_model('image_classifier.h5')                    ## load saved model
        class_labels = {0:'Cat', 1:'Dog'}                                       ## prepare labels
        img = imread(request.files['photo'])                                    ## read photo & transform it into array
        img = resize(img,(128,128))
        img = np.expand_dims(img,axis=0)
        if(np.max(img)>1):
            img = img/255.0
        prediction = image_classifier.predict_classes(img)                      ## predict class    
        guess = class_labels[prediction[0][0]]                                  ## for website display
        keras.backend.clear_session()                                           ## clear Tensor session to avoid error
        
        return render_template("guess.html", guess = guess)
    

    
### ERROR HANDLING


@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404
    
@app.errorhandler(500)
def error500(error):
    return render_template('500.html'), 500


## APP INITIATION

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False) 
            