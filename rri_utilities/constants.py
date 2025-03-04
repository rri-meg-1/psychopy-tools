# python imports
from dataclasses import dataclass

@dataclass
class ProjectorSpecs:
    name: str
    width_px: int
    height_px: int
    refresh_rate_hz: int

PROPIXX_PROJECTOR_SPEC = ProjectorSpecs(name="propixx", 
    width_px=1920, height_px=1080, refresh_rate_hz=60)
