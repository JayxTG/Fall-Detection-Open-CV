# Elder Fall Detection

## Project Description

This project aims to develop a real-time fall detection system using a webcam and computer vision techniques. The system detects humans in the camera frame, tracks their movements, and identifies potential falls. It uses a pre-trained human detection model (HOG descriptor) and draws stick figures around detected humans to visualize the detection. The system also includes a simple fall detection algorithm based on changes in aspect ratios and movement patterns.

## 🎯 Objective

The objective of this project is to create an automated system that can detect falls in real-time, providing a potential safety mechanism for elderly individuals.

## 🔑 Key Features

- 🎥 Real-time human detection using a webcam
- 🕵️ Drawing stick figures around detected humans
- 🛠️ Simple fall detection algorithm based on aspect ratio and movement analysis
- 🚨 Displaying alerts when a fall is detected

## 🛠️ Hardware and Software Requirements

### Hardware:
- Webcam

### Software:
- OpenCV
- NumPy

## 📁 Folder Structure

- `src`: Contains the source code for the project
- `models`: Pre-trained models and related files
- `docs`: Project documentation and related materials

## 🎛️ How to Use

1. **Clone the Repository**

   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/elder-fall-detection.git
    ```
2. **Install Dependencies**
 Navigate to the project directory and install the required dependencies:

   ```bash
   pip install -r requirements.txt

    ```
3. **Run the Application**

Execute the main script to start the fall detection system:

   ```bash
   python src/fall_detection.py
```

## 📸 Sample Usage
**Detecting Falls**
Run the application, and it will start the webcam feed. The system will detect humans in the frame, draw stick figures around them, and display an alert if a fall is detected.

## Dependencies
- OpenCV
- NumPy

## 🏢 Acknowledgments
- OpenCV community for the computer vision tools
- NumPy community for the numerical computation tools
  
## License

Author: Jayamadu Gammune

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do 
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.

**DISCLAIMER:**
This code is provided for educational and informational purposes only. It is 
still under development and may contain bugs or inaccuracies. The authors are 
not responsible for any damage or loss resulting from the use of this code. Use 
at your own risk.
