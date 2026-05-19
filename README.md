# TrashTrack - AI-Based Litter Detection and Challan Management System

TrashTrack is a Flask-based web application that uses computer vision to detect littering incidents from uploaded images. The system uses a trained YOLOv8 object detection model to identify litter in an image and then simulates challan generation for the detected incident.

This project is designed as a smart civic-tech solution that combines artificial intelligence, web development, and automated report management to support cleaner public spaces.

---

## Project Overview

TrashTrack allows users to report littering incidents through a web dashboard. A user can upload an image of the incident along with basic details such as date, location, and description. The backend processes the uploaded image using a YOLOv8 model. If litter is detected, the system generates a challan record and updates the report status.

The project demonstrates how AI-based image detection can be integrated with a web application to create an automated litter reporting and fine management system.

---

## Key Features

- User login using predefined demo credentials
- Interactive dashboard for navigating project modules
- Image upload for reporting littering incidents
- YOLOv8-based litter detection from uploaded images
- Automatic simulated challan generation when litter is detected
- Challan history page with fine amount and payment status
- Incident report status tracking
- Informational pages such as About, Help, Grievance, Notifications, Rewards, and User Profile
- Responsive frontend design using HTML, CSS, and JavaScript
- Trained YOLO model artifacts included in the project directory

---

## Technologies Used

### Backend

- Python
- Flask
- Werkzeug
- Ultralytics YOLOv8
- OpenCV

### Frontend

- HTML5
- CSS3
- JavaScript
- Jinja2 Templates

### Machine Learning / Computer Vision

- YOLOv8s Object Detection Model
- Custom Litter Detection Dataset

### Tools

- VS Code
- Git
- GitHub

---

## Folder Structure

```text
TrashTrack/
│
├── backend/
│   ├── app.py
│   ├── face_recog_handler.py
│   ├── yolov8s.pt
│   ├── users/
│   │   ├── user1.jpg
│   │   ├── user2.jpg
│   │   ├── user3.jpg
│   │   └── user4.jpg
│   │
│   ├── static/
│   │   └── Uploads/
│   │
│   ├── ML/
│   │   └── taco_dataset/
│   │       └── data/
│   │           ├── data.yaml
│   │           ├── images/
│   │           │   ├── train/
│   │           │   └── val/
│   │           └── labels/
│   │               ├── train/
│   │               └── val/
│   │
│   └── runs/
│       └── detect/
│           └── train/
│               ├── args.yaml
│               ├── results.csv
│               ├── labels.jpg
│               ├── labels_correlogram.jpg
│               ├── train_batch*.jpg
│               └── weights/
│                   ├── best.pt
│                   └── last.pt
│
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── script.js
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── incident-report.html
│   ├── my-challans.html
│   ├── report-status.html
│   ├── about.html
│   ├── help.html
│   ├── grievance.html
│   ├── notifications.html
│   ├── my-rewards.html
│   └── user-profile.html
│
├── requirements.txt
└── README.md
```

---

## Important Files

### `backend/app.py`

This is the main Flask application file. It handles the complete backend flow of the project.

Main responsibilities:

- Creates and runs the Flask application
- Loads the trained YOLOv8 model
- Handles user login
- Accepts uploaded incident images
- Runs litter detection on uploaded images
- Generates simulated challans
- Stores reports and challan data temporarily
- Renders different dashboard pages

Main routes included in the application:

| Route | Description |
|---|---|
| `/` | Opens the login page |
| `/login` | Validates demo login credentials |
| `/dashboard` | Displays the main dashboard |
| `/incident-report` | Opens the incident reporting form |
| `/detect-litter` | Handles image upload and YOLO detection |
| `/my-challans` | Displays generated challans |
| `/get-challans` | Returns challan data in JSON format |
| `/report-status` | Shows uploaded report status |
| `/payment/<challan_id>` | Placeholder payment route |
| `/about` | Displays project information |
| `/help` | Displays help page |
| `/notifications` | Displays notifications page |
| `/grievance` | Displays grievance form |
| `/profile` | Displays user profile page |
| `/rewards` | Displays rewards page |

---

### `backend/face_recog_handler.py`

This file contains helper code for face recognition.

It is designed to:

- Load known user images from the `backend/users/` folder
- Encode faces using the `face_recognition` library
- Match an uploaded image with known user faces
- Return the identified user name

Current status:

- This file is included as a future enhancement module.
- It is not directly connected to the main detection flow in `app.py`.
- The current challan generation logic assigns a random user when litter is detected.

---

### `templates/`

This folder contains all HTML pages used in the web application.

Important templates:

| File | Purpose |
|---|---|
| `index.html` | Login page |
| `dashboard.html` | Main dashboard |
| `incident-report.html` | Image upload and incident reporting page |
| `my-challans.html` | Displays generated challans |
| `report-status.html` | Shows submitted report status |
| `about.html` | Project information page |
| `help.html` | Help center page |
| `grievance.html` | Grievance submission page |
| `notifications.html` | Notifications page |
| `my-rewards.html` | Rewards page |
| `user-profile.html` | User profile page |

---

### `static/css/styles.css`

This file contains the complete styling of the project.

It controls:

- Login page layout
- Dashboard design
- Navigation bar
- Cards and sections
- Forms and buttons
- Tables
- Report pages
- Responsive layout

---

### `static/js/script.js`

This file contains frontend JavaScript logic.

It mainly handles:

- Reading login form values
- Sending login data to the backend
- Redirecting users to the dashboard after successful login
- Showing an alert for invalid login credentials

---

### `backend/ML/taco_dataset/data/data.yaml`

This is the YOLO dataset configuration file.

It defines:

- Training image path
- Validation image path
- Number of classes
- Class names used for training

Classes mentioned in the dataset configuration:

```text
bag
metal
plastic
trash
nonlitter
```

---

### `backend/runs/detect/train/`

This folder contains the YOLOv8 training outputs.

Important files:

| File | Purpose |
|---|---|
| `args.yaml` | Stores YOLO training configuration |
| `results.csv` | Contains epoch-wise training metrics |
| `labels.jpg` | Shows dataset label distribution |
| `labels_correlogram.jpg` | Shows label correlation visualization |
| `train_batch*.jpg` | Shows training batch previews |
| `weights/best.pt` | Best trained model checkpoint |
| `weights/last.pt` | Last trained model checkpoint |

The `best.pt` file is used by the Flask backend for litter detection.

---

## How the Project Works

1. The user opens the web application.
2. The user logs in using demo credentials.
3. After login, the user is redirected to the dashboard.
4. The user opens the incident report page.
5. The user enters incident details and uploads an image.
6. The Flask backend receives the uploaded image.
7. The YOLOv8 model checks whether litter is present in the image.
8. If litter is detected, the system generates a simulated challan.
9. The challan is displayed on the My Challans page.
10. The submitted report status is displayed on the Report Status page.

---

## Model Training Summary

The project includes a YOLOv8s model trained for litter detection.

| Item | Details |
|---|---|
| Model | YOLOv8s |
| Task | Object Detection |
| Dataset Type | Custom litter dataset |
| Image Size | 640 |
| Epochs | 30 |
| Batch Size | 16 |
| Best Model | `backend/runs/detect/train/weights/best.pt` |

Final training metrics:

| Metric | Value |
|---|---:|
| Precision | 0.95695 |
| Recall | 0.94992 |
| mAP@50 | 0.98495 |
| mAP@50-95 | 0.77597 |

These metrics show that the model performed well on the validation data included in the training run.

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/AnshSingh2312/TrashTrack.git
cd TrashTrack
```

---

### 2. Create a Virtual Environment

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Recommended `requirements.txt`:

```text
flask
werkzeug
opencv-python-headless
ultralytics
gunicorn
```

If face recognition is integrated later, install:

```text
face-recognition
```

---

### 4. Run the Flask App

```bash
cd backend
python app.py
```

---

### 5. Open the Application

Open the following URL in your browser:

```text
http://127.0.0.1:5000
```

---

## Demo Login Credentials

```text
Username: user1
Password: p1
```

Other demo users available in the project:

```text
user2 / p2
user3 / p3
user4 / p4
```

---

## Current Limitations

- The project uses demo login credentials instead of database-based authentication.
- Reports and challans are stored temporarily in Python lists.
- Stored data resets when the server restarts.
- Challan assignment currently uses a random user.
- Face recognition code is available but not integrated into the main Flask flow.
- Payment functionality is only a placeholder.
- Notifications, rewards, grievance, and profile pages are partially implemented or static.
- The system is currently a prototype and not a production-ready application.

---

## Future Enhancements

- Add database support using MySQL or PostgreSQL
- Add secure user registration and login
- Store challans and reports permanently
- Integrate face recognition for offender identification
- Add license plate recognition for vehicle-based littering cases
- Add admin dashboard for authorities
- Add online challan payment integration
- Add email or SMS notifications
- Add map-based location tagging
- Improve dataset quality and model accuracy
- Deploy the application as a live web service

---

## Conclusion

TrashTrack demonstrates how artificial intelligence can be used in civic management systems. By combining Flask, YOLOv8, and a web dashboard, the project provides a prototype for automated litter detection, incident reporting, and challan generation.

The project highlights the practical use of computer vision in smart city applications and shows how AI-based systems can support cleaner and more responsible public environments.
