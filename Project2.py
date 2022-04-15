

#L in km
import math
import numpy as np
L = 140
Lx = 1

num_splices = 139

#values in dB
RLs = -80
ILc = 0.2
RLc = -40
RLrx = -27

Ptx = 0
#Rayleigh backscatter
RSF = 3*10**(-6)
#wavelength nm
lam = 1310

#attenuation in dB/km
attenuation_fiber = 0.4

#min EXT
min_ext = 10

Ptx_watts = 0.001


def connectorPowerLevel():
    Pconncetor = Ptx-2*attenuation_fiber*L+RLc
    return Pconncetor

def receiverPowerLevel():
    Prx = Ptx-2*attenuation_fiber*L-2*ILc+RLrx
    return Prx
def splicePowerLevel():

    Ps = Ptx_watts * (10**((-2*attenuation_fiber*Lx)/10)) * \
         10**(RLs/10)*((1-10**((-2*num_splices*attenuation_fiber*Lx)/10))/(1-10**((-2*attenuation_fiber*Lx)/10)))

    return Ps

def backscatter():
    Pf = Ptx_watts*(RSF)*(10/(2*attenuation_fiber*math.log(10)))*(1-math.exp((-2*attenuation_fiber*L*math.log(10))/10))

    return Pf

def ORL():
    Pconnector_watt = (10 ** (connectorPowerLevel() / 10))/1000
    Prx_watt = (10 ** (receiverPowerLevel() / 10))/1000
    #Ps_watt = 10 ** (splicePowerLevel() / 10)

    #print(Pconnector_watt)
    #print(Prx_watt)
    #print(Ps_watt)

    ORL = 10*math.log10(Ptx_watts/(Pconnector_watt+Prx_watt+splicePowerLevel()))



    return ORL

def ORLharder():
    Pconnector_watt = (10 ** (connectorPowerLevel() / 10)) / 1000
    Prx_watt = (10 ** (receiverPowerLevel() / 10)) / 1000
    #Ps_watt = 10 ** (splicePowerLevel() / 10)
    ORL_harder = 10 * math.log10(Ptx_watts / (Pconnector_watt + Prx_watt + splicePowerLevel() + backscatter()))

    return ORL_harder


def extinction():
    Pout_temp1 = Ptx-attenuation_fiber*L-ILc
    Pout1 = (10**(Pout_temp1/10))/1000+2*backscatter()

    Pout_temp0 = Ptx-min_ext-attenuation_fiber*L-ILc
    Pout0 = (10**(Pout_temp0/10))/1000+2*backscatter()

    ext_out = 10*math.log10(Pout1/Pout0)

    ext_final = min_ext-ext_out
    return ext_final



print("Power level of reflection from connector[dBm]: ",connectorPowerLevel())
print("Power level of reflection from reveiver[dBm]: ",receiverPowerLevel())
print("Power level of reflection from splices[dBm]: " ,10*math.log10((1000*splicePowerLevel())/1))

print("ORL - receiver, connector and splices[dB]: ", ORL())

print("Power level from Rayleigh backscatter[dBm]: " ,10*math.log10((1000*backscatter())/1))

print("ORL - receiver, connector, splices and backscatter[dB]: ", ORLharder())

print("The decrease of extinction coefficient in EXTin-EXTout[dB]: ", extinction())
