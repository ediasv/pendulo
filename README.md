# Pendulum Motion Analysis

Experimental Physics II project that uses video processing to analyze the motion of a damped simple pendulum.

The experiment consists of recording a pendulum in motion, tracking the horizontal position of its mass over time, and using the resulting data to study the damped harmonic oscillator and determine the system's quality factor.

## Experiment

A simple pendulum was assembled using a mass of approximately **100 g** attached to a string approximately **0.5 m** long. The pendulum was released from an initial angle slightly greater than **10°** and recorded for approximately one minute against a contrasting background.

The recorded video was then processed frame by frame to determine the horizontal position of the pendulum mass throughout the experiment.

## Workflow

1. Record the pendulum oscillating.
2. Process the video frame by frame.
3. Apply color-based filtering to locate the pendulum mass.
4. Store each frame timestamp and corresponding horizontal position.
5. Plot the experimental data.
6. Fit the damped harmonic oscillator model to the measurements.
7. Determine the quality factor of the system.

## Repository Structure

```text
.
├── get_data.py    # Extracts position data from the recorded experiment
├── plot.py        # Plots the collected data
├── output/        # Generated experimental output
└── README.md
```

## Results

The extracted position data can be visualized over time to observe the oscillatory motion and the gradual reduction in amplitude caused by damping.

![Experimental pendulum data](https://github.com/ediasv/pendulo/assets/142503604/3b0b0c02-e343-46d5-aec1-fd72fa8430af)

### Experiment video

https://github.com/ediasv/pendulo/assets/142503604/fc2210a8-9284-4475-805c-ec923d61ca27

A presentation of the complete experiment and analysis is also available on [YouTube](https://youtu.be/rHrgEify1PU?si=S-0SSjtIsMe18HF6).

## Assignment Requirements

This project was developed for a **Physics II** course. The assignment required:

* assembling a simple pendulum on a fixed base;
* recording approximately one minute of oscillation;
* extracting frames from the video and locating the pendulum mass using color filtering;
* recording the timestamp and horizontal position for each frame;
* fitting the damped harmonic oscillator equation to the experimental data;
* determining the system's quality factor;
* presenting the complete process in a video.
