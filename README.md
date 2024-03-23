# AGROAI ML APPLICATION

   
<br />

# Paddy Disease and Pest, Tea Disease Identification ML Application

## Introduction

This application utilizes machine learning to analyze images of paddy and tea plants, helping users identify potential diseases and pests affecting their crops. By uploading an image, the application can classify the presence and type of disease or pest, allowing for timely intervention and improved crop management.

## Technologies Used

- **Deep Learning:** TensorFlow, PyTorch
- **Object Detection Model:YOLOv5, SSD
- **Image Processing Libraries:** Pillow
<br />
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
