# Criminal-Identification & Missing People Detection

## Problem Statement🧐 

Develop an Desktop application or a native mobile application to demonstrate application of Face Recognition technology.

## Solution ✨

I propose criminal identification system and missing people identification to enhance and upgrade the criminal distinguishing into a more effective and efficient approach. Technology working behind it will be face recognition, from the footage captured by the CCTV cameras our system will detect the face and recognize the criminal who is coming to that public place. The captured images of the person coming to that public place get compared with the criminal data we have in our database. If any person’s face from public place matches, the system will display their image on the system screen and will give the message with their name that the criminal is found and present in this public place.

<!--
## Presentation 


https://user-images.githubusercontent.com/81081105/170887653-e613abe3-74aa-41e7-8db4-ca6c8767bed4.mp4
-->


<!--

## Workflow of Project 🗺
 <img width="500" alt="Screenshot 2022-05-21 at 2 51 35 PM" src="https://user-images.githubusercontent.com/81081105/169645049-0b84ff23-5b71-424c-9820-fa55a84143a5.png"> -->

 
<!--
## Model Build on Keeping These Criteria in Mind 👩🏻‍💻

1. Performance of model
2. Model selection
3. Scalability
4. Scalability of model
5. Retrainable model
6. Accessibility
7. User friendly
8. Accuracy 
-->

## Technologies 👩🏻‍💻

### 1. Tkinter 

Python has a lot of GUI frameworks, but Tkinter is the only framework that’s built into the Python standard library. Tkinter has several strengths. It’s cross-platform, so the same code works on Windows, macOS, and Linux. Visual elements are rendered using native operating system elements, so applications built with Tkinter look like they belong on the platform where they’re run. 

### 2. Python <img width="30" src="https://img.icons8.com/color/48/000000/python--v1.png"/>

Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis. Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn't specialized for any specific problems. Python is dynamically-typed and garbage-collected. 


### 3. Open-CV <img width="30" src="https://img.icons8.com/color/48/000000/opencv.png"/>

OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products. Being a BSD-licensed product, OpenCV makes it easy for businesses to utilize and modify the code.

### 4. MySQL <img width="30" src = "https://user-images.githubusercontent.com/81081105/179774941-89b16b8c-0a21-4782-96b8-c247f158757d.png"/>


Python MySQL Connector is a Python driver that helps to integrate Python and MySQL. This Python MySQL library allows the conversion between Python and MySQL data types. MySQL Connector API is implemented using pure Python and does not require any third-party library.

## Prerequisite 🖥

1. Python version must be `3.8.10`
2. Tkinter version must be `8.6`
3. [Xampp](https://www.apachefriends.org/download.html) must be installed on your system.

`Note: Tk interface can be different for different systems and their versions`

## Steps to run the project 👇🏻

1. start your mysql and apache server and navigate to localhost and create database of name `criminaldb`.
2. Import `table.sql` file into your newly created `criminaldb`. 
3. run this sql command in your criminaldb `SET GLOBAL sql_mode='';`
4. Install the requiremnts using command `pip or pip3 install -r requirements.txt`.
5. Before running the file extract all the files of `Images` Folder to your root directory. 
6. Run the main python file `python or python3 main.py`.
7. Now experience the GUI and features of the project.

## Glimpse of my Application 💁🏻‍♀️

**Login Page**            |  **Sign-Up Page**
:-------------------------:|:-------------------------:
![](https://user-images.githubusercontent.com/81081105/170031961-682d7f02-45e0-47b0-b8de-12fbb8576287.png)  |  ![](https://user-images.githubusercontent.com/81081105/170031999-d0f4ab21-aec8-4020-9466-d08fbf346321.png)

**Home Page** 

<img width="800" alt="Screenshot 2022-05-24 at 11 09 27 PM" src="https://user-images.githubusercontent.com/81081105/170098347-9f328ba0-4f63-4f26-968c-395b1c20663f.png">

**Criminal Detection**            |  **Finding Missing People**
:-------------------------:|:-------------------------:
<img width="600" alt="Screenshot 2022-05-24 at 11 14 45 PM" src="https://user-images.githubusercontent.com/81081105/170099565-dfc2e897-3602-4678-9ce0-592c24649e5a.png">  |  <img width="600" alt="Screenshot 2022-05-24 at 11 19 00 PM" src="https://user-images.githubusercontent.com/81081105/170100191-829547af-66b5-4cc1-9d42-c8ea06a16556.png">


**Register Criminal**            |  **Register Missing Person**
:-------------------------:|:-------------------------:
<img width="600" alt="Screenshot 2022-05-28 at 4 03 16 PM" src="https://user-images.githubusercontent.com/81081105/170822969-67fe0d7a-180c-4874-a36b-86174425e720.png"> | <img width="600" alt="Screenshot 2022-05-28 at 4 16 37 PM" src="https://user-images.githubusercontent.com/81081105/170822906-0a180413-3c15-42f8-b434-7dfdd2932b7c.png"> 

**Image Observation**      |  **Image Observation**
:-------------------------:|:-------------------------:
<img width="600" alt="Screenshot 2022-05-28 at 4 19 33 PM" src="https://user-images.githubusercontent.com/81081105/170823024-4f6c3432-8eca-4e9e-8d57-458a2728fc6b.png">  |  <img width="600" alt="Screenshot 2022-05-28 at 4 17 09 PM" src="https://user-images.githubusercontent.com/81081105/170823029-a3c15dd6-279d-40f4-9862-43cce47609a6.png">

<!-- **Video Observation**      |  **Video Observation**
:-------------------------:|:-------------------------:
https://user-images.githubusercontent.com/81081105/170838208-4eea8b95-a8a3-428b-bab0-176e9377cad4.mp4  | https://user-images.githubusercontent.com/81081105/170838232-701ca29d-2477-44db-a097-f01f62b42f51.mp4 -->


**Alerts**                 |  **Alerts**    
:-------------------------:|:-------------------------:
<img width="600" alt="Screenshot 2022-05-28 at 11 24 19 PM" src="https://user-images.githubusercontent.com/81081105/170837323-d9ddf905-e837-43e5-ac43-7036eed7b653.png"> | <img width="600" alt="Screenshot 2022-05-28 at 4 20 32 PM" src="https://user-images.githubusercontent.com/81081105/170837045-d021aea3-cf91-4dd6-8446-344f8fbf680e.png">  

**Alerts**                 | **Alerts**    
:-------------------------:|:-------------------------:
<img width="600" alt="Screenshot 2022-05-28 at 11 25 17 PM" src="https://user-images.githubusercontent.com/81081105/170837354-d99b0d47-0163-46f0-9432-e73ed613f381.png"> |  <img width="600" alt="Screenshot 2022-05-28 at 4 21 54 PM" src="https://user-images.githubusercontent.com/81081105/170837081-a88f4599-b149-4a41-81c8-3c309ee7c65d.png">


**Terminal Output**

<img width="1152" alt="Screenshot 2022-05-28 at 4 35 31 PM" src="https://user-images.githubusercontent.com/81081105/170837449-361ae831-e024-40b0-9413-a1bc0fa94a35.png"> 

## Added Webcam Support for real time detection

**Live Observation**      |  **Webcam access**
:-------------------------:|:-------------------------:
<img width="600" alt="image" src="https://user-images.githubusercontent.com/81081105/188306412-ff133778-1981-4f82-955d-b854bf05f249.png"> |  <img width="600" alt="image" src="https://user-images.githubusercontent.com/81081105/188306792-6a60cf99-d0ba-48a7-be75-29e8f7af61cb.png">


## Future Scope 🕵️‍♀️

1. Fingerprint Recognition and Eye detection can be added for Observation.


