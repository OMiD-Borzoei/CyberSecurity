from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from time import sleep 

CONST = 0.01

# Get the default audio device
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

# Cast the interface to IAudioEndpointVolume
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Get the current volume range
volume_range = volume.GetVolumeRange()
current_volume = 0

while True:
    
    # Increase the volume
    prev_volume = current_volume
    current_volume = volume.GetMasterVolumeLevel()
    
    if abs((current_volume - prev_volume) - CONST) < 1e-5:
        print(1, 'detected')
    elif abs((prev_volume - current_volume) - CONST) < 1e-5:
        print(0, 'detected')
