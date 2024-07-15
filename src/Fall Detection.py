"""
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

DISCLAIMER:
This code is provided for educational and informational purposes only. It is 
still under development and may contain bugs or inaccuracies. The authors are 
not responsible for any damage or loss resulting from the use of this code. Use 
at your own risk.


"""

import cv2
import numpy as np
from collections import deque

# Load a pre-trained human detection model (e.g., HOG descriptor)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def detect_humans(frame):
    # Resize frame for faster processing
    frame = cv2.resize(frame, (640, 480))
    
    # Detect humans in the frame
    humans, _ = hog.detectMultiScale(frame, winStride=(8, 8), padding=(32, 32), scale=1.05)
    
    return humans

def draw_stick_figure(frame, bbox):
    x, y, w, h = bbox
    cv2.circle(frame, (int(x + w / 2), y), 10, (0, 255, 255), -1)
    cv2.line(frame, (int(x + w / 2), y), (int(x + w / 2), int(y + h / 2)), (0, 255, 255), 2)
    cv2.line(frame, (int(x + w / 2), int(y + h / 2)), (x, y + h), (0, 255, 255), 2)
    cv2.line(frame, (int(x + w / 2), int(y + h / 2)), (x + w, y + h), (0, 255, 255), 2)
    cv2.line(frame, (int(x + w / 2), int(y + h / 4)), (x, int(y + h / 2)), (0, 255, 255), 2)
    cv2.line(frame, (int(x + w / 2), int(y + h / 4)), (x + w, int(y + h / 2)), (0, 255, 255), 2)

def detect_fall(previous_bboxes, current_bbox):
    if not previous_bboxes:
        return False
    
    prev_bbox = previous_bboxes[-1]
    _, prev_y, _, prev_h = prev_bbox
    _, curr_y, _, curr_h = current_bbox
    
    # Calculate vertical movement and height change
    vertical_movement = (curr_y + curr_h/2) - (prev_y + prev_h/2)
    height_change = curr_h - prev_h
    
    # Criteria for detecting a fall
    if vertical_movement > prev_h * 0.3 and height_change < -prev_h * 0.3:
        return True
    
    return False

def main():
    cap = cv2.VideoCapture(0)
    previous_bboxes = deque(maxlen=5)
    fall_frames = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        humans = detect_humans(frame)
        fall_detected = False
        
        for (x, y, w, h) in humans:
            current_bbox = (x, y, w, h)
            
            if detect_fall(previous_bboxes, current_bbox):
                fall_frames += 1
                if fall_frames >= 3:  # Require 3 consecutive fall detections
                    fall_detected = True
            else:
                fall_frames = max(0, fall_frames - 1)
            
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            draw_stick_figure(frame, (x, y, w, h))
            
            previous_bboxes.append(current_bbox)
        
        if fall_detected:
            cv2.putText(frame, 'Fall Detected', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, 'FALL', (int(frame.shape[1] / 2) - 50, int(frame.shape[0] / 2)), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4, cv2.LINE_AA)
        
        cv2.imshow('Elder Fall Detection', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()