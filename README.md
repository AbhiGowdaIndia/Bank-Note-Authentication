# Bank-Note-Authentication
Bank note authentication using machine learning complete end-to-end project.

The data set is available in kaggle.

Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.

In this repository there are many folder, which are all for the same "Bank note authentication" projects but using different deployment techniques. Following are the folders with details,

1. Data sets

This folder contains two CSV files, namely 
 * 'BankNote_Authentication.csv' used to train the model and,
 * 'TestFile.csv' used to test the model.
 
 2. Streamlit

Here the model is deployed in AWS EC2 using streamlit.</br>
* http://ec2-3-83-217-79.compute-1.amazonaws.com:8501/ This is the URL of the app where we can see the result of the project since it is deployed and running on AWS EC2 instance.

3. Flask
 
The folder contains the necessary file to run the app. 'flask_api.py' is the file which we need to run to see the result. we can see the result in url which we get when we run the app or with the help of the 'post man' software which is a popular API client that makes it easy for developers to create, share, test and document APIs.

4. Flasgger

Here the model is deployed using both Flask and flasgger and containes all the necessary file required for deployment.

5. Flasgger-and-Docker

Here the model is dockerized and deployed using Flasgger and and containes all the necessary file required for deployment.


When you click on the URLs the resultent page will open where you can see the result just by enter the values or by choosing a file. The file should be a csv file and should be in the same format as the file we used to train the model, so we can use the 'Testfile.csv' file which is in 'Data sets' folder.

Thank you.
