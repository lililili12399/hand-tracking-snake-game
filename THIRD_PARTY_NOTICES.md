# Third-party notices

This project imports the following third-party packages. They are not relicensed by this repository:

- [cvzone](https://github.com/cvzone/cvzone) — MIT License.
- [MediaPipe](https://github.com/google-ai-edge/mediapipe) — Apache License 2.0.
- [NumPy](https://github.com/numpy/numpy) — BSD 3-Clause License.
- [OpenCV](https://github.com/opencv/opencv) and the `opencv-python` distribution — review their included license notices for the installed version.

The current program uses cvzone's `HandDetector`, which in turn uses MediaPipe for hand landmarks.

## Included MediaPipe model

`models/hand_landmarker.task` is a MediaPipe Hand Landmarker model bundle and remains subject to the MediaPipe/Apache 2.0 terms. It is retained from the project files but is not referenced by the current `main.py`.

## Donut asset

`donut.png` is included with the project owner's confirmation that the project materials may be uploaded. The original source URL was not recorded in the local files.

## Tutorial/code provenance

The game structure resembles publicly circulated cvzone hand-tracking Snake examples. The exact tutorial source used by the team was not recorded in the local files. If it is identified later, add the relevant upstream attribution without removing the notices above.

