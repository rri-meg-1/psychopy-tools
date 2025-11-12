# python imports
import queue

# vendor imports
from psychopy import core
from psychopy import event

class EscapeDetector:
    """Class to handle escape key presses during experiments."""

    def __init__(self, escape_key='escape'):
        self._has_pressed_escape_queue = queue.Queue()
        self._escape_key = escape_key
        event.globalKeys.add(key=self._escape_key,
            func=self._set_escape_press_state)

    def _set_escape_press_state(self):
        self._has_pressed_escape_queue.put(True)

    def has_pressed_escape(self):
        """Check if the escape key has been pressed."""
        if not self._has_pressed_escape_queue.empty():
            return True
        return False
