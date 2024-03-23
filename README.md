# AGROAI ML APPLICATION

Our project aims to develop a comprehensive, fully automated outdoor farm management and analysis system tailored for agricultural operations. With a focus on continual improvement and future development, our objectives are to modernize agriculture practices and maximize crop yields while ensuring sustainability and efficiency.

Key Features:

Pest and Disease Detection: Our system includes advanced algorithms for detecting pests and diseases affecting paddy and tea crops, enabling timely intervention and mitigation.
Automation: Through the integration of cutting-edge technologies such as sensors, drones, and satellite imaging, our system automates various tasks including irrigation, fertilization, and pest control, reducing reliance on manual labor and improving efficiency.
Data Analysis: We employ sophisticated data analytics techniques to analyze information collected from multiple sources, providing insights into crop health, environmental conditions, and resource management.
Scalability: Designed with scalability in mind, our system is adaptable to different farm sizes and types, allowing for seamless expansion and integration of additional features in the future.
Sustainability: By promoting sustainable farming practices and optimizing resource utilization, our system contributes to environmental conservation and long-term agricultural viability.
User-Friendly Interface: We prioritize usability and accessibility, offering an intuitive interface that enables farmers to easily monitor and manage their crops, make data-driven decisions, and track performance metrics.
Overall, our project aims to revolutionize outdoor farm management by harnessing the power of automation, data analytics, and sustainability principles, ultimately driving productivity and resilience in agriculture.
   
<br />

# Paddy Disease and Pest, Tea Disease Identification ML Application

## Introduction

This application utilizes machine learning to analyze images of paddy and tea plants, helping users identify potential diseases and pests affecting their crops. By uploading an image, the application can classify the presence and type of disease or pest, allowing for timely intervention and improved crop management.

## Technologies Used

- **Deep Learning:** TensorFlow, PyTorch
- **Object Detection Model:**YOLOv5, SSD
- **Image Processing Libraries:** Pillow


```bash
$ git clone git@github.com:Nawanjane/agroAi.git
$ cd agroAi
```

<br />

> 👉 **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br /> 

## ✅ Manual Build 

> Download the code 

```bash
$ git clone https://github.com/app-generator/flask-gradient-able.git
$ cd flask-gradient-able
```

<br />

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Flask Environment

```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
```

<br />

> Start the app

```bash
$ flask run
```

At this point, the app runs at `http://127.0.0.1:5000/`. 

<br />

### 👉 Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Flask Environment

```bash
$ # CMD 
$ set FLASK_APP=run.py
$ set FLASK_ENV=development
$
$ # Powershell
$ $env:FLASK_APP = ".\run.py"
$ $env:FLASK_ENV = "development"
```

<br />

> Start the app

```bash
$ flask run
```

At this point, the app runs at `http://127.0.0.1:5000/`. 



<br />
