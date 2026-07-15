# 🎓 Face Recognition Attendance Monitoring System

A Python-based desktop application that automates student attendance using real-time face recognition. The system captures student facial data, trains a face recognition model, identifies registered students through a webcam, and automatically records attendance with timestamps.

---

## 📌 Project Overview

Manual attendance systems are time-consuming and prone to human error. This project utilizes **Computer Vision** and **Machine Learning** techniques to recognize registered students in real time and automatically generate attendance records, making the attendance process faster, more accurate, and efficient.

---

## ✨ Features

- Real-time face detection and recognition
- User-friendly Tkinter graphical interface
- Student registration with image capture
- Face dataset generation and model training
- Automatic attendance recording with date and time
- Attendance stored in CSV format
- Password-protected student registration
- Student details management
- Lightweight desktop application

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| GUI | Tkinter |
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

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

---

## 🚀 How to Use

1. Launch the application.
2. Register a new student.
3. Capture facial images.
4. Train the face recognition model.
5. Start the attendance system.
6. The application automatically recognizes registered students.
7. Attendance is recorded with the current date and time.

---

## 📊 Key Functionalities

- Face Detection using OpenCV Haar Cascade
- Face Recognition using LBPH Algorithm
- Student Registration Module
- Model Training Module
- Attendance Recording Module
- CSV-based Data Management
- Password Protection for Registration

---

## 📈 Future Enhancements

- Deep Learning-based face recognition
- MySQL or MongoDB database integration
- Flask/Django web application
- Cloud-based attendance synchronization
- Email attendance reports
- Face mask detection support
- Student analytics dashboard

---

## 📚 Learning Outcomes

This project strengthened practical knowledge in:

- Python Programming
- Computer Vision
- OpenCV
- Face Recognition
- GUI Development with Tkinter
- Image Processing
- CSV File Handling
- Attendance Automation

---

## 👩‍💻 Author

**Saahini Pasham**

B.Tech – Computer Science & Engineering

GitHub: https://github.com/Saahini

---

## 📄 License

This project is licensed under the **MIT License**.

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub.