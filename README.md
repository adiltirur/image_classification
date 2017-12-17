# Image Classification With Tensorflow

### This is a project for the Machine Learning Course by Prof.Luca Iocch @ Sapienza University di Roma

### Data set used:
Maritime Detection, Classification and tracking data set and can be downloaded from
http://www.dis.uniroma1.it/~labrococo/MAR/classification.htm
The training set contains images from 24 different categories of boats navigating in the City of Venice (Italy). The .rar file contains a folder for each category. The jpeg files inside the folders are named according to the date, hour, and system track number. The folder "Water" contains false positives

# Let's begin!!

## Install needed libraries
1.Tensorflow<br />
https://www.tensorflow.org/install/install_linux<br /><br />
2.Pandas<br />
pip install pandas <br /><br />
3.Numpy<br />
pip install numpy<br /><br />
4.clone this repo<br />
git clone git@github.com:adiltirur1/Image_classification.git<br /><br />

## Getting the data sets ready
Copy the training and testing data set in to <br />
/image_classifier/supporting_files/data_set <br />

## Let's Train the classifier 

from the root directory of this repository run the command <br />
python -m code.retrain   --bottleneck_dir=supporting_files/bottlenecks   --how_many_training_steps=500   --model_dir=supporting_files/models/   --summaries_dir=supporting_files/training_summaries/"${ARCHITECTURE}"   --output_graph=supporting_files/retrained_graph.pb   --output_labels=supporting_files/retrained_labels.txt   --inception_v3   --image_dir=supporting_files/sc5 <br />

### yesss!! The training is done and it shows you the estimated accuracy
