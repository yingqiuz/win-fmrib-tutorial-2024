# Import necessary modules
from psychopy import visual, core, event

# Define stimuli (text objects)
stimulus1 = visual.TextStim(text='Stimulus 1', pos=(0, 0), color='black')
stimulus2 = visual.TextStim(text='Stimulus 2', pos=(0, 0), color='black')

# Create window for displaying stimuli
win = visual.Window(size=(800, 600), color='white', units='pix')

# Display welcome message at the beginning
welcome_text = visual.TextStim(win, text='Welcome to the Visual Task!', pos=(0, 50), color='black')
welcome_text.draw()  # Draw the welcome message on the window
win.flip()  # Display the content of the window
core.wait(2)  # Wait for 2 seconds before proceeding

# Main loop for conducting the trials
for trial in range(60):  # Perform 60 trials
    # Present first stimulus
    stimulus1.draw()  # Draw the first stimulus on the window
    win.flip()  # Display the first stimulus
    core.wait(0.5)  # Wait for 500 milliseconds (0.5 seconds)

    # Present second stimulus
    stimulus2.draw()  # Draw the second stimulus on the window
    win.flip()  # Display the second stimulus
    core.wait(0.5)  # Wait for 500 milliseconds (0.5 seconds)

    # Wait for participant response
    keys = event.waitKeys(keyList=['1', '2'])  # Accepts either 1 or 2 as response from the keyboard
    response = keys[0]  # Record the participant's response

    # Print participant response for testing (can be removed in final version)
    print(f'Trial {trial+1}: Participant responded with {response}')

# Display completion message at the end
completion_text = visual.TextStim(win, text='Task done, thanks!', pos=(0, 50), color='black')
completion_text.draw()  # Draw the completion message on the window
win.flip()  # Display the completion message
core.wait(2)  # Wait for 2 seconds before closing the window

# Close the window
win.close()