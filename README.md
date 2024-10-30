# Hand Tracking with Mediapipe

This project implements hand tracking using the Mediapipe library and OpenCV. The script captures video from the webcam, processes the frames to detect hands, and visualizes the hand landmarks and connections in real-time.

## Features

- Real-time hand tracking using Mediapipe.
- Visualization of hand landmarks and connections.
- Displays frames per second (FPS) for performance monitoring.
- Highlights the wrist (landmark ID 0) with a circle.

## Future Enhancements

- **Gesture Recognition**: Implement gesture recognition to perform actions based on detected hand movements (e.g., swipes, pinches)..
- **Integration with Applications**: Use hand tracking for controlling applications or games, enabling a hands-free user interface.
- **User Interface Improvements**: Develop a graphical user interface (GUI) for better user interaction and configuration options.

## Requirements

- **Python 3.x**
- **OpenCV**: To install OpenCV, use the following command:
  ```bash
  pip install opencv-python
  ```
- **Mediapipe**: To install Mediapipe, use the following command:
  ```bash
  pip install mediapipe
  ```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/hand-tracking.git
   ```
2. Navigate to the project directory:
   ```bash
   cd hand-tracking
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the script and start tracking hand landmarks, execute the following command:

```bash
python hand_tracking.py
```

The program will display a window showing the webcam feed with hand landmarks and their connections. The FPS will be displayed in the top left corner or may be in the task bar(When open in background).


## Contributing

Contributions are welcome! If you have suggestions or improvements, please feel free to submit a pull request.
