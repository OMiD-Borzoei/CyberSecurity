from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from time import sleep 

# Amount of Change in Speaker:
CONST = 0.01

# Get the default audio device
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

# Cast the interface to IAudioEndpointVolume
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Get the current volume range
volume_range = volume.GetVolumeRange()

while True:
    # Increase the volume
    current_volume = volume.GetMasterVolumeLevel()
    volume.SetMasterVolumeLevel(current_volume + CONST, None)
    print(1, 'Sent')
    #Sleep for 1 Second
    sleep(1)
    
    # Decrease the volume
    current_volume = volume.GetMasterVolumeLevel()
    volume.SetMasterVolumeLevel(current_volume - CONST, None)
    print(0, 'Sent')
    #Sleep for 1 Second 
    sleep(1)
