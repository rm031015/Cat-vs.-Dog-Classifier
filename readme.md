# Cat vs. Dog Image Classifier

## INSTALLING REQUIREMENTS (Conda Environment, Cloud9)

wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh<br>
chmod a+x Miniconda3-latest-Linux-x86_64.sh<br>
./Miniconda3-latest-Linux-x86_64.sh<br>

NEW TERMINAL

conda create -n py3 python=3 ipython <br>
source activate py3 <br>

pip install --upgrade pip<br>
pip install numpy <br>
conda install -c conda-forge tensorflow<br>
pip install keras==2.1.3<br>
pip install scikitlearn <br>
pip install scipy image<br>

pip install flask

pip freeze --local > requirements.txt