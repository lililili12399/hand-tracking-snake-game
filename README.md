# Hand-Tracking Snake Game

A webcam-controlled Snake game built with Python, OpenCV, and cvzone. The snake follows the detected index fingertip. Collecting the donut increases the score and the allowed snake length; touching the snake body ends the round.

This repository was prepared from a team course project. Team roles are listed in [CONTRIBUTORS.md](CONTRIBUTORS.md).

## Features

- Real-time webcam input
- Single-hand landmark detection
- Index-finger control
- Random food placement, score counting, and snake growth
- Self-collision game-over state
- Keyboard reset and exit controls

## Requirements

- Python 3
- A working webcam
- Camera permission for the terminal or IDE running the program

Install the Python dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\activate
```

## Run

Run the command from the repository root so that `donut.png` can be found:

```bash
python3 main.py
```

Controls:

- Move your index finger to guide the snake.
- Press `R` to reset the game.
- Press `Q` or `Esc` to quit.
- Closing the game window also exits the program.

## Project structure

```text
.
├── main.py
├── donut.png
├── requirements.txt
├── docs/
│   ├── course_report.docx
│   └── screenshots/
│       └── README.md
├── models/
│   └── hand_landmarker.task
├── CONTRIBUTORS.md
├── LICENSE
├── THIRD_PARTY_NOTICES.md
└── UPLOAD.md
```

`models/hand_landmarker.task` is retained as a project asset but is not referenced by the current `main.py`, which uses cvzone's `HandDetector`. The course report is included as historical project documentation; performance figures in that report were not independently benchmarked during this repository preparation.

## Known limitations

- The camera index is fixed to `0`.
- Rendering and food placement assume a 1280 × 720 capture area.
- Collision detection is a geometric heuristic and can vary with hand movement.
- Scores are not saved between sessions.

## Screenshots and privacy

The available demonstration recording shows an identifiable person and a private indoor environment, so it is intentionally excluded. Add only screenshots or video for which every visible person has agreed to public sharing. See [docs/screenshots/README.md](docs/screenshots/README.md).

## License

The team project is released under the [MIT License](LICENSE). Third-party packages and the included MediaPipe model remain under their respective licenses; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

