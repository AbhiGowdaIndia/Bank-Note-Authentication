# Bank-Note-Authentication
Bank note authentication using machine learning. It is a complete end-to-end project.

The data set is available in kaggle.

Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.

In this repository there are may folder, which are all for the same "Bank note authentication" projects but using different deployment techniques. Following are the folders with details,

1. Data sets

This folder contains two CSV files, namely 
 * 'BankNote_Authentication.csv' used to train the model and,
 * 'TestFile.csv' used to test the model.

2. Flask
 
Here the model is deployed using flask.</br>
The folder contains the necessry file to run the app. 'flask_api.py' is the file which we need to run to see the result. we can see the result in url which we get when we run the app or with the help of the 'post man' software which is a popular API client that makes it easy for developers to create, share, test and document APIs.

3. Flasgger

Here the model is deployed in AWS EC2 using flask and flasgger.</br>
* http://ec2-18-212-73-136.compute-1.amazonaws.com:8080/apidocs/  This is the URL of the app where we can see the result of the project since it is deployed and running on AWS EC2 instance.
This folder contains all the necessary file required to deploy the model.

4. Streamlit

Here the model is deployed in AWS EC2 using streamlit.</br>
* http://ec2-3-83-217-79.compute-1.amazonaws.com:8501/ This is the URL of the app where we can see the result of the project since it is deployed and running on AWS EC2 instance.

5. Flasgger-and-Docker

Here the model is dockerized and deployed in AWS EC2 using Flasgger.
* http://ec2-3-82-142-165.compute-1.amazonaws.com:8000/apidocs/ This is the URL of the app where we can see the result of the project since it is dockerized, deployed and running on AWS EC2 instance.


When you click on the URLs the resultent page will open where you can see the result just by enter the values or by choosing a file. The file should be a csv file and should be in the same format as the file we used to train the model, so we can use the 'Testfile.csv' file which is in 'Data sets' folder.

Thank you.
