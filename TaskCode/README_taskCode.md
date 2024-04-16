# Psychopy Task README

## Overview

This repository contains a Python script for a simple Psychopy task. The task involves presenting two stimuli sequentially on a visual window and collecting participant responses. The stimuli are presented alternately with a fixed duration, and participants are required to respond with a key press.

## Task Description

The provided Python script (`task_code_Open_science.py`) implements the following steps:

1. **Initializing Stimuli**: Two text stimuli (`stim1` and `stim2`) are created with predefined text, position, and color attributes.

2. **Creating Window**: A visual window (`win`) is initialized using Psychopy's `visual.Window` class. The window size, background color, and units are specified.

3. **Presenting Welcome Message**: A welcome message is displayed on the window using a text stimulus (`wtext`), and the window is flipped to show the message to the participant.

4. **Running Trials**: The main loop iterates 60 times, presenting `stim1` followed by `stim2` alternately. Each stimulus presentation lasts for 0.5 seconds. After each presentation, the participant's key press response is recorded.

5. **Printing Trial Information**: Trial number and participant responses are printed to the console.

6. **Task Completion**: After completing all trials, a task completion message is displayed on the window (`ctext`), and the window is flipped to show the message to the participant.

7. **Closing Window**: Finally, the window is closed.

## Usage

To run the Psychopy task (do not run it):

1. Ensure you have Psychopy installed in your Python environment.
2. Copy the provided Python script (`task_code_Open_science.py`) to your local machine.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the Python script.
5. Run the script using the command: `python task_code_Open_science.py`.

## Dependencies

- Psychopy: Ensure you have Psychopy installed in your Python environment to run the task script.

## Notes

- This task script is intended for educational purposes and serves as a basic example of using Psychopy for experimental psychology tasks.
- You can modify the script to customize stimuli, trial parameters, and response collection methods according to your specific experimental design.

## License

TCC BY-NC-SA 4.0 Deed Attribution-NonCommercial-ShareAlike 4.0 International

This license enables reusers to distribute, remix, adapt, and build upon the material in any medium or format for noncommercial purposes only, and only so long as attribution is given to the creator. If you remix, adapt, or build upon the material, you must license the modified material under identical terms. CC BY-NC-SA includes the following elements:

BY: credit must be given to the creator. NC: Only noncommercial uses of the work are permitted. SA: Adaptations must be shared under the same terms.

**Note:** Remember to respect intellectual property rights and ethical guidelines when using real datasets and protocols in your projects.

Feel free to explore, modify, and use the provided script for your educational or research purposes!

For any questions or issues, please don't hesitate to contact the repository owners.

Happy experimenting!
