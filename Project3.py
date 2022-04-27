import math
import numpy as np


#value in km
L1 = 5
L2 = 75
#value in nm
fiber1_wavelength = 1500
fiber2_wavelength = 1580
center_frequency1 = 1300
center_frequency2 = 1500
wavelength_range = np.linspace(fiber1_wavelength,fiber2_wavelength,(fiber2_wavelength-fiber1_wavelength))
total_dispersion = []
dispersion_slope1 = 0.095
dispersion_slope2 = 0.09

def dispersion(wavelength, c_freq, slope):
    D = (slope/4)*(wavelength-((c_freq**4)/(wavelength**3)))
    return D

d1 = dispersion(fiber1_wavelength,center_frequency1,dispersion_slope1)
d2 = dispersion(fiber2_wavelength,center_frequency2,dispersion_slope2)
Dispersion = d1*L1 + d2*L2
print(d1)
print(d2)
print(Dispersion)


#TODO total dispersion D of 2 fibers
#TODO rms = del_tf/Dispersion
#signals in MHz
if code == "RZ":
    Bsig = Bit_rate
else:
    Bsig = Bit_rate*0.5



Bsystem = Bsig * 1.1

Btx = Bsystem * 1.9

delta_ttx = 0.35 / (Btx * 10 ** 6)
delta_tch = 0.35 / (Bsystem * 10 ** 6)
delta_tf = math.sqrt((delta_tch) ** 2 - 2 * (delta_ttx) ** 2)

