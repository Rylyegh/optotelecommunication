import math
from sympy import symbols, Eq, solve
#code takes values "RZ" or "NRZ"
code = "RZ"
#Bitrate in Mbps
Bit_rate = 2488.32
#values in dBm
min_Ptx_value = -10
max_Ptx_value = 0

min_sens_Prx = -34

path_penalty = 1

#value in nm
min_op_wavelength = 1450
max_op_wavelength = 1580

center_frequency = 1550

dispersion_slope = 0.095
attenuation_fiber = 0.25

#spectral width in nm
RMS = 4

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
print("delta_f in ps = ", delta_tf / 10 ** -12)
D_min = (dispersion_slope / 4) * (min_op_wavelength - (center_frequency ** 4 / min_op_wavelength ** 3)) + (
            dispersion_slope / 2) * RMS
D_max = (dispersion_slope / 4) * (max_op_wavelength - (center_frequency ** 4 / max_op_wavelength ** 3)) + (
            dispersion_slope / 2) * RMS
L_bandwidth_min = (delta_tf / 10 ** -12) / (abs(D_min) * RMS)
L_bandwidth_max = (delta_tf / 10 ** -12) / (abs(D_max) * RMS)





L_power_min = (min_Ptx_value - min_sens_Prx - 3 - path_penalty - 2 * 0.5) / (attenuation_fiber)
L_power_max = (max_Ptx_value - min_sens_Prx - 3 - path_penalty - 2 * 0.5) / (attenuation_fiber)



print("Bandwidth system[MHz] = ", Bsystem)
print("Bandwidth transmitter and receiver[MHz] = ", Btx)
print("Minimum Power length[km]: ", L_power_min)
print("Maximum Power length[km]: ", L_power_max)
print("Minimum Bandwidth length[km]: ", L_bandwidth_min)
print("Maximum Bandwidth length[km]: ", L_bandwidth_max)