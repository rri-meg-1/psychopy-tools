# vendor imports
from psychopy import visual, event, core, data, gui
from psychopy.hardware import keyboard

# imports
from rri_utilities.megprojector import RotmanMegProjector
from rri_utilities.escaper import EscapeDetector
projector = RotmanMegProjector()
meg_window = projector.window

# initialize clock
clock = core.Clock()

# initialize keyboard
kb = keyboard.Keyboard(clock=clock)
allowed_keys = ['1', '2', '3', '4', '6', '7', '8', '9']

#initialize fixation cross
fixation = visual.Circle(meg_window, size = 10,
    lineColor = 'white', fillColor = [255, 255, 255], colorSpace='rgb255')

# initialize instructions text
ready_text = visual.TextStim(meg_window, text='Experimenter: Press any key to start',
    color='white', height=20, pos=(0, 50), anchorVert='bottom')
participant_countdown_text = visual.TextStim(meg_window, text='Ready, set...',
    color='white', height=30)
button_press_text = visual.TextStim(meg_window, text='Press a button now!',
    color='white', height=30, pos=(0, 0), anchorVert='bottom')

# initialize magix pixel
start_recording_magic_pix = projector.make_magic_pixel(255, size_px=10)
start_trial_magic_pix = projector.make_magic_pixel(128, size_px=10)
countdown_magic_pix = projector.make_magic_pixel(64, size_px=10)

COUNTDOWN_TIME_FRAMES = projector.convert_seconds_to_frames(2.0)
def show_countdown():
    """Show countdown before trial starts."""
    countdown_time_sec = 2.0
    countdown_start = core.getTime()
    for frame_number in range(COUNTDOWN_TIME_FRAMES):
        countdown_magic_pix.draw()
        participant_countdown_text.draw()
        meg_window.flip()
    # at the end of the countdown, check for escape press
    if escape_detector.has_pressed_escape():
        core.quit()
        return

MAX_TRIAL_TIME_FRAMES = projector.convert_seconds_to_frames(10.0)
def show_trial():
    """Show button press prompt until a button is pressed."""
    kb.clearEvents()
    start_trial_magic_pix.draw()
    button_press_text.draw()
    meg_window.flip()
    clock.reset()
    for frame_number in range(MAX_TRIAL_TIME_FRAMES):
        start_trial_magic_pix.draw()
        button_press_text.draw()
        meg_window.flip()
        keys = kb.getKeys(keyList=allowed_keys, waitRelease=False)
        if keys:
            reaction_time = keys[0].rt
            print(f"Button {keys[0].name} pressed at {reaction_time:.3f} seconds after frame {frame_number} onset.")
            return
        if escape_detector.has_pressed_escape():
            core.quit()
            return

# start screen
fixation.draw()
ready_text.draw()
meg_window.flip()

escape_detector = EscapeDetector()

event.waitKeys()


# cycle through 100 trials
for trial_number in range(100):
    show_countdown()
    show_trial()
    # inter-trial interval
    core.wait(0.2)

# clean-up
meg_window.close()
core.quit()
