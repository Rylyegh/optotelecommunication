

#L in km
import math

L = 130
Lx = 1

num_splices = 129

#values in dB
RLs = -65
ILc = 0.5
RLc = -40
RLrx = -14

Ptx = 0
#Rayleigh backscatter
RSF = 3e-6
#wavelength nm
lam = 1310

#attenuation in dB/km
attenuation_fiber = 0.4

#min EXT
min_ext = 8.2

Ptx_watts = (10**(Ptx/10))/1000

def connectorPowerLevel():
    Pconncetor = Ptx-2*attenuation_fiber*L+RLc
    return Pconncetor

def receiverPowerLevel():
    Prx = Ptx-2*attenuation_fiber*L-2*ILc+RLrx
    return Prx
def splicePowerLevel():

    Ps = Ptx_watts * (10**((-2*attenuation_fiber*Lx)/10)) * \
         10**(RLs/10)*((1-10**((-2*num_splices*attenuation_fiber*Lx)/10))/(1-10**((-2*attenuation_fiber*Lx)/10)))
    Ps = 10*math.log10(Ps)

    return Ps

def backscatter():
    Pf = Ptx_watts*RSF*(10/(2*attenuation_fiber*math.log(10)))\
         *(1-math.exp((-2*attenuation_fiber*L*math.log(10))/10))
    return Pf

def ORL():
    Pconnector_watt = (10**(connectorPowerLevel()/10))/1000
    Prx_watt = (10**(receiverPowerLevel()/10))/1000
    Ps_watt = (10**(splicePowerLevel()/10))/1000

    ORL = 10*math.log10(Ptx_watts/(Pconnector_watt+Prx_watt+Ps_watt))

    ORL_harder = 10*math.log10(Ptx_watts/(Pconnector_watt+Prx_watt+Ps_watt+backscatter()))

    return ORL, ORL_harder

def extinction():
    Pout_temp1 = Ptx-attenuation_fiber*L-ILc
    Pout1 = (10**(Pout_temp1/10))/1000+2*backscatter()

    Pout_temp0 = Ptx-min_ext-attenuation_fiber*L-ILc
    Pout0 = (10**(Pout_temp0/10))/1000+2*backscatter()

    ext_out = 10*math.log10(Pout1/Pout0)

    return ext_out



print("Power level of reflection from connector[dBm]: ",connectorPowerLevel())
print("Power level of reflection from reveiver[dBm]: ",receiverPowerLevel())
print("Power level of reflection from splices[dBm]: " ,splicePowerLevel())

print("ORL - receiver, connector and splices[dB]: ", ORL()[0])

print("Power level from Rayleigh backscatter[dBm]: " ,10*math.log(backscatter()))

print("ORL - receiver, connector, splices and backscatter[dB]: ", ORL()[1])

print("The decrease of extinction coefficient in EXTin-EXTout[dB]: ", extinction())
