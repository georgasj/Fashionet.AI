# Fashionet.ai
a classification CNN for fashion clothes in keras/tensorflow.

This project aims to create an application that performs garment classification based on their category: blouse, t-shirt, trousers etc and colour(s). The basic steps are the following:

1) web scrapping programs used to create the training and validation sets that we will use to train our CNN VGG16 model. 
2) First part of CNN training, aiming to train our model using pre-trained imagenet weights.
3) Second part of CNN training, aiming to fine tune the complete model.
4) Application using the trained model to classify clothes based on their type.
5) An algorithm called K-means that is able to identify the dominant colours of the garment as seen in the photo.

Files:

Jupiter notebooks:

Application.ipynb - this is the app pulling all together: the trained model and the K-means algorithm.

Bottleneck features Softmax.ipynb - this file trains the model on the bottleneck features

Fine-tuning Softmax.ipynb - this file trains the model's last layers 

Scrappers:

flickr5.py - this is a program to download photos from flickr

instagram.txt - this is a command to download photos from instagram 

websitescrap.py - this is a program for web scrapping

Other files:

vgg16_weights.txt - this is a placeholder, the actual file should be downloade from the internet, used for pre-trained imagenet early layers of the CNN model.

chromedriver.txt - this is a placeholder, the actual file should be downloaded from the internet, used for web scrapping

blousetest.jpg - a test photo
