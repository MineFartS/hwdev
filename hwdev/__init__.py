from typing import Literal
from .hardware import *

NAME: str

OS: Literal['windows', 'unix']

def __getattr__(attr:str) -> str:
    from socket import gethostname
    import os

    match attr:

        case 'OS':
            return 'windows' if (os.name == 'nt') else 'unix'
        
        case 'NAME':
            return gethostname()
        
    raise AttributeError(f"module '{__name__}' has no attribute '{attr}'")

