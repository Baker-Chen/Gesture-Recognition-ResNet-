# 2021 Synopsys ARC AIoT Design Contest
![image](https://user-images.githubusercontent.com/85024328/120073598-9e337a80-c0cb-11eb-91b6-afecf940a960.png)


## Project Name:
**Smart elevator based on edge computing architecture combined with gesture recognition**
## Team Name:
WE-I Goose • Smith
## Project Description:
In the post pandemic era, zero-contact technology has become a trend. Among them, the elevator is beneficial to the spread of the virus, because the elevator space is small, closed and crowded. It is easy to infect because people contact the elevator control panel and talk to each other in the elevator. So we wanted to achieve a smart elevator control panel that can recognize the specific gestures and always-on system through the benefits of Himax WE-I Plus ultra-low power consumption and AI acceleration, and reduce  operation complexity and overall power consumption through a distributed computing architecture of edge computing. First, with the help of OpenCV, convert the collected training data into the output form of the WE-I Plus lens module (single-channel grayscale 640x480 image), and use the gesture recognition algorithm to classify the data we collected and reduce the complexity of  training model. Then use the TensorFlow Lite machine learning framework to train the gesture recognition model.
## Contents:
* Auto-labeling module: MediaPipe
 ![image](https://user-images.githubusercontent.com/85024328/120074141-08e5b580-c0ce-11eb-8b37-c051b1601184.png)

* Training Data:
1. Input: grayscale 640x480
2. 10 + 1 categories (0~9 & ok)
3. 400~500 img/caregory
4. Shffule & Split (training, validation)
5. Data augment
  
![image](https://user-images.githubusercontent.com/85024328/120074181-39c5ea80-c0ce-11eb-89b9-d259e0ce8781.png)



* Training model:
ResNet50

![image](https://user-images.githubusercontent.com/85024328/120074207-5e21c700-c0ce-11eb-96a2-d5f9fca245fd.png)

* Accuracy & Confusion Matrix
  
![image](https://user-images.githubusercontent.com/85024328/120074267-a4772600-c0ce-11eb-8fda-885c03c7520b.png)
![image](https://user-images.githubusercontent.com/85024328/120074293-be186d80-c0ce-11eb-8f4f-91923c39f19d.png)

* Demo:
  
  ![image](https://user-images.githubusercontent.com/85024328/120074376-26674f00-c0cf-11eb-94d7-eb143bc4ee89.png)


* Elevator animation (flask):
  
![image](https://user-images.githubusercontent.com/85024328/120074352-0c2d7100-c0cf-11eb-8317-13d3bfbff962.png)


 

## Gesture-Recognition-ResNet-
