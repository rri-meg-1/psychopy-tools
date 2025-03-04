# vendor imports
from psychopy import visual, event, core, data, gui

# imports
from rri_utilities.megprojector import RotmanMegProjector

projector = RotmanMegProjector()
meg_window = projector.window

#initialise some stimuli
fixation = visual.Circle(meg_window, size = 10,
    lineColor = 'white', fillColor = 'lightGrey')

magic_pix = projector.make_magic_pixel(255, size_px=10)

frame_count = projector.convert_seconds_to_frames(2.0)

for frame_number in range(frame_count):
    fixation.draw()
    magic_pix.draw()
    meg_window.flip()

meg_window.close()
