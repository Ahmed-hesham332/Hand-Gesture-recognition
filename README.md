# AI
HCI Hand gesture recognition

**To implement the hand gesture recognition system, we utilized several libraries and tools:**

- OpenCV (cv2): Used for capturing video frames from the webcam and processing images.
- Mediapipe: Employed for hand tracking and detecting hand landmarks.
- Ultralytics YOLO: Utilized for object detection to classify gestures.
- PyAutoGUI: Used for simulating mouse and keyboard actions based on detected gestures.
- Screen Brightness Control: Managed screen brightness adjustments.
- PyCaw: Controlled system volume.
- Tkinter: Created graphical user interfaces for user interaction.

**Key Functions:**

- Volume Control: Gestures like a closed fist with the index finger raised increase the volume, while a peace sign decreases it.
- Brightness Control: An open palm increases brightness, and a closed fist decreases it.
- Other Controls: Gestures like thumbs up play or pause videos, and raising all fingers except the thumb closes the application.

The home.py file defines the introductory page of the application. It provides 
instructions and options for the user to choose between cursor and non-cursor 
functionalities.

The optionPage.py file presents two buttons to the user: one for activating cursor 
control mode (main.py) and another for non-cursor functions (Yolo_realTime.py). 
Additionally, a back button allows the user to return to the home page

**Challenges and Limitations**
1. Lighting Conditions: The system's performance could be affected by poor lighting, leading to inaccurate gesture detection.
2. Background Noise: A cluttered background might interfere with hand tracking, causing false detections.
3. Some instability detection: The pause and play gesture seems to be instable

**Future Work**
1. Gesture Set Expansion: Adding more gestures to control additional functionalities.
2. Enhanced Robustness: Improving the system's performance under varying lighting conditions and background complexities.
3. User Customization: Allowing users to customize gestures for different actions
   
Screenshots:
![image](https://github.com/Ahmed-hesham332/Hand-Gesture-recognition/assets/68594545/8ab2d576-b66b-45d0-afe1-4aa1547a7501)
![image](https://github.com/Ahmed-hesham332/Hand-Gesture-recognition/assets/68594545/7efd9a6d-3e95-4a1b-8252-e4b46c489cbf)

for more inforamtion, Contact me 
