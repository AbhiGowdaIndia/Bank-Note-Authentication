# Bank-Note-Authentication
Bank note authentication using machine learning.

The data set is available in kaggle.

Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.

In this repository there are may folder, which are all for the same "Bank note authentication" projects but using different deployment techniques. Following are the folders with details,

1.Data sets

This folder contains two CSV files, namely 
 * 'BankNote_Authentication.csv' used to train the model and,
 * 'TestFile.csv' used to test the model.

2. Flask
 
Here the model is deployed using flask.</br>
The folder contains the necessry file to run the app. 'flask_api.py' is the file which we need to run to see the result. we can see the result in url which we get when we run the app or with the help of the 'post man' software which is a popular API client that makes it easy for developers to create, share, test and document APIs.
