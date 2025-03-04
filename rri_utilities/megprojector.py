# python imports
import math
import warnings

# numpy/scipy imports
import numpy as np

# vendor imports
from psychopy import monitors, visual

#imports
from .constants import PROPIXX_PROJECTOR_SPEC

class RotmanMegProjector:
    _monitor = monitors.Monitor(PROPIXX_PROJECTOR_SPEC.name)
    _resolution = np.array([PROPIXX_PROJECTOR_SPEC.width_px, PROPIXX_PROJECTOR_SPEC.height_px], 
        dtype=np.int32) # px
    _refresh_rate = PROPIXX_PROJECTOR_SPEC.refresh_rate_hz # Hz

    def __init__(self):
        self.window = visual.Window(size=self._resolution, fullscr=True, 
            monitor=self._monitor, units='pix')
    
    def make_magic_pixel(self, green_value, size_px=20):
        # top left: x-coord = 0 - width/2, y-coord = 0 + height/2
        top_left = np.add(np.array([0, 0]),
            np.floor_divide(self._resolution, np.array([-2, 2])))
        return visual.Rect(win = self.window, size=size_px, 
            pos=top_left, color = (0, green_value, 0), colorSpace='rgb255')
    
    def convert_seconds_to_frames(self, seconds):
        frames = self._refresh_rate * seconds
        frames_floor = math.floor(frames)
        if not math.isclose(frames, frames_floor):
            warnings.warn(f"{seconds} can't be converted to exact frames. "
                "Rounded to {frames_floor}")
        return frames_floor
