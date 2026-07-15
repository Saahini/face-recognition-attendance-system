# 🎓 Face Recognition Attendance Monitoring System

A Python-based desktop application that automates student attendance using **real-time face recognition**. The system captures facial data, trains an **LBPH Face Recognizer**, identifies registered students through a webcam, and automatically records attendance with timestamps in CSV format.

---

## 📖 Overview

Manual attendance systems are time-consuming, error-prone, and inefficient. This project uses **Computer Vision** and **Machine Learning** to automate attendance by recognizing registered students in real time.

The application provides a user-friendly **Tkinter-based graphical interface** for student registration, model training, and attendance management.

---

## ✨ Features

- ✅ Real-time face detection using OpenCV
- ✅ Face recognition using the LBPH algorithm
- ✅ Student registration with image capture
- ✅ Automatic face dataset generation
- ✅ Face recognition model training
- ✅ Attendance recording with date and time
- ✅ Attendance stored in CSV format
- ✅ Password-protected student registration
- ✅ Student details management
- ✅ Simple and intuitive desktop interface

---

## 🛠️ Tech Stack

| Category | Technologies |
|-----------|--------------|
| Programming Language | Python |
| GUI Framework | Tkinter |
| Computer Vision | OpenCV |
| Face Recognition | LBPH Face Recognizer |
| Libraries | NumPy, Pandas, Pillow |
| Data Storage | CSV Files |

---

## 📂 Project Structure

```text
face-recognition-attendance-system/
│
├── Attendance/
├── StudentDetails/
├── TrainingImageLabel/
├── attendance_system.py
├── main.py
├── haarcascade_frontalface_default.xml
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Saahini/face-recognition-attendance-system.git
```

### 2. Navigate to the project directory

```bash
cd face-recognition-attendance-system
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

---

## 🚀 Usage

1. Launch the application.
2. Register a new student by entering the required details.
3. Capture facial images for the student.
4. Train the face recognition model.
5. Start the attendance system.
6. The application automatically recognizes registered students.
7. Attendance is saved with the current date and time inside the **Attendance/** folder.

---

## 🔄 System Workflow

```text
Student Registration
        │
        ▼
Capture Face Images
        │
        ▼
Train Face Recognition Model
        │
        ▼
Real-Time Face Detection
        │
        ▼
Recognize Student
        │
        ▼
Attendance Recorded in CSV
```

---

## 📊 Core Functionalities

- Face Detection using Haar Cascade Classifier
- Face Recognition using LBPH Algorithm
- Student Registration Module
- Face Dataset Generation
- Model Training
- Automated Attendance Recording
- CSV-based Data Management
- Password Authentication

---

## 📈 Future Enhancements

- Deep Learning-based Face Recognition (FaceNet / ArcFace)
- MySQL or PostgreSQL Database Integration
- Flask or Django Web Application
- Cloud-Based Attendance Synchronization
- Email Attendance Reports
- Face Mask Detection
- Student Analytics Dashboard
- Mobile Application Support

---

## 📚 Learning Outcomes

This project strengthened practical knowledge in:

- Python Programming
- Computer Vision
- OpenCV
- Face Recognition
- Image Processing
- GUI Development with Tkinter
- CSV File Handling
- Machine Learning Fundamentals

---

## 📸 Screenshots

> Screenshots will be added soon.

---

## 👩‍💻 Author

**Saahini Pasham**

B.Tech – Computer Science & Engineering

GitHub: https://github.com/Saahini

---

## 🤝 Acknowledgements

This project was developed for educational and portfolio purposes using Python, OpenCV, and Tkinter.

---

## 📄 License

This project is licensed under the **MIT License**.

---

⭐ **If you found this project useful, consider giving it a Star on GitHub!**