# AirSign Recorder ✍🏼✨

Welcome to the AirSign Recorder repository! 
This project introduces an approach to capturing and verifying airborne signatures. Leveraging the capabilities of finger tracking, our implementation allows users to draw signatures in the air. The recorded signatures are then subjected to an automatic signature matching process.

## Implementation Overview

The implementation utilizes the finger tracking approach, continuously analyzing camera images to determine the position and posture of individual fingers. Python was chosen as the programming language due to the availability of extensive and free libraries such as NumPy, OpenCV, and Mediapipe.


## How to Use the Program

To use the application, only one hand is required. When the camera image (Canvas) appears to the user, they can move their open hand into the frame. The successful detection of their hand is indicated by the displayed "Landmarks." The user can then create a signature.

The application distinguishes between a movement and a drawing mode to accommodate situations where a signature cannot be created continuously. The user can interrupt drawing and continue at another position in the canvas. The mode is determined by the posture of the fingers:

- Drawing Mode: Only the index finger is extended.
- Movement Mode: Hand is open.

A "Retry" button in the upper right corner of the canvas allows users to reset the canvas without restarting the program. Another "Finish" button in the upper left corner allows users to mark the created signature as complete without disrupting the program flow or requiring an additional input device (e.g., mouse, keyboard). After creating two AirSignatures, the canvas closes, and the user is presented with the comparison result in a new window.

## How to Run the Program:

1. Install dependencies: `pip install -r requirements.txt`
2. Run the main program: `python main.py`
3. Create 2 signatures with the index finger.
4. After finishing a signature, hover over the green checkmark in the top left corner with the index finger.
5. When the two signatures are displayed, press 'Space' to see the result.

Enjoy using the AirSign Recorder!
