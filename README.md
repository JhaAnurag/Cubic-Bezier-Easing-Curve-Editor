# Custom Easing Curve Implementation with Bezier Curves in Pygame

This Python script uses Pygame to visualize a custom easing animation driven by a cubic Bezier curve. You can interactively adjust the control points of the curve and see how it affects the animation of a red circle.
This is a project I made as a way to learn how easing works within After Effects, Alight Motion, and similar tools.

## Features

*   **Visualizes Bezier Curve:** Displays a green Bezier curve that defines the easing function.
*   **Interactive Control Points:** Allows you to manipulate the two inner control points of the Bezier curve using the keyboard.
*   **Animated Circle:**  A red circle moves horizontally across the screen, and its vertical position is determined by the Bezier curve.
*   **Tracker Rectangle:** A green rectangle follows the vertical movement of the circle, providing a visual link between the circle's position and the curve.
*   **Real-time Adjustment:** Changes to the control points are reflected immediately in the curve and subsequent animations.

## How to Use

1. **Prerequisites:**
    *   Make sure you have Python installed on your system.
    *   Install the Pygame library:
        ```bash
        pip install pygame
        ```

2. **Run the script:**
    Save the provided Python code as a `.py` file (e.g., `main.py`) and run it from your terminal:
    ```bash
    python main.py
    ```

3. **Interact with the animation:**
    *   **Select Control Points:**
        *   Press `1` to select the first control point of the Bezier curve.
        *   Press `2` to select the second control point.
    *   **Move Control Points:**
        *   Once a control point is selected, use the **arrow keys** (Left, Right, Up, Down) to adjust its position.
    *   **Start Animation:**
        *   Press the **spacebar** to start the animation. The red circle will move from left to right, and its vertical position will follow the Bezier curve.

## Understanding the Code

*   **Bezier Curve:** The core of the animation is the cubic Bezier curve defined by four control points (C1, V1), (C2, V2), (C3, V3), and (C4, V4). The script allows you to manipulate (C2, V2) and (C3, V3).
*   **Easing Function:** The Bezier curve acts as an easing function, mapping the horizontal progress of the animation (0 to 1) to the vertical movement (0 to 1). This creates different acceleration and deceleration effects.
*   **`bezier` function:** This function calculates a point on the Bezier curve for a given `t` value (ranging from 0 to 1).
*   **`draw_bezier_curve` function:** This function draws the green Bezier curve on the screen.
*   **`solve_t_for_x` function:** This function uses a binary search approach to find the `t` value on the Bezier curve that corresponds to a given horizontal position (`x_target`) of the circle. This is crucial for synchronizing the circle's horizontal movement with the easing defined by the curve.

## Potential Improvements

*   **Graphical Interface for Control Points:** Instead of using keyboard input, allow dragging the control points directly on the screen.
*   **Presets for Common Easing Functions:** Implement options to select pre-defined easing functions (e.g., ease-in, ease-out, ease-in-out).
*   **More Control Points:** Experiment with higher-order Bezier curves or other easing functions.
*   **Saving and Loading Curves:** Add functionality to save and load custom Bezier curves.

This script provides a basic framework for understanding and experimenting with custom easing animations using Bezier curves in Pygame. Feel free to modify and expand upon it!
