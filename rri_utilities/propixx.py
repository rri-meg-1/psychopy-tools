# python imports
import math
import warnings

# vendor imports
import numpy as np
from pypixxlib.propixx import PROPixx

class ProPixxDriver:
    def __init__(self):
        self._brightness = -1
        self._allowed_brightness_levels = np.array([
            6.25, 12.5, 25.0, 50.0, 100.0
        ])
        self._ppx = PROPixx()

    def get_brightness(self):
        #Initialize PROPixx
        brightness = self._ppx.getLedIntensity() 
        #Pass command to hardware
        self._ppx.writeRegisterCache()
        return brightness

    def _set_brightness(self, brightness):
        self._ppx.setLedIntensity(f"{brightness:.1f} %")
        #Pass command to hardware
        self._ppx.writeRegisterCache()

    def _find_next_low_brightness(self, brightness):
        # check if there is a match
        index = np.argwhere(
            np.isclose(self._allowed_brightness_levels,
                       np.full_like(self._allowed_brightness_levels, brightness))
            )
        if index.size == 0:
            # no match
            raise ValueError(f"{brightness} not listed")
        matched_index = index[0, 0]
        if matched_index > 0:
            # return the next low
            return self._allowed_brightness_levels[matched_index - 1]
        # otherwise, the provided value is already the min
        warnings.warn(f"{brightness} is already the min brightness.")
        return self._allowed_brightness_levels[0]

    def is_at_min_brightness(self):
        self._brightness = self.get_brightness()
        return math.isclose(self._brightness, self._allowed_brightness_levels[0])

    def dim_step(self):
        if self.is_at_min_brightness():
            warnings.warn("Already at min brightness. Won't dim again.")
            return
        self._brightness = self.get_brightness()
        if (self._brightness == -1):
            warnings.warn("unable to read brightness. nothing done.")
            return
        new_level = self._find_next_low_brightness(self._brightness)
        self._set_brightness(new_level)
   
    def reset_to_full_brightness(self):
        self._set_brightness(self._allowed_brightness_levels[-1])
