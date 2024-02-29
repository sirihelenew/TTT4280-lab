import numpy as np

muabo = np.genfromtxt("./muabo.txt", delimiter=",")
muabd = np.genfromtxt("./muabd.txt", delimiter=",")

red_wavelength = 675 # Replace with wavelength in nanometres
green_wavelength = 525 # Replace with wavelength in nanometres
blue_wavelength = 450 # Replace with wavelength in nanometres

wavelength = np.array([red_wavelength, green_wavelength, blue_wavelength])

def mua_blood_oxy(x): return np.interp(x, muabo[:, 0], muabo[:, 1])
def mua_blood_deoxy(x): return np.interp(x, muabd[:, 0], muabd[:, 1])

bvf = 0.01 # Blood volume fraction, average blood amount in tissue
oxy = 0.8 # Blood oxygenation

# Absorption coefficient ($\mu_a$ in lab text)
# Units: 1/m
mua_other = 25 # Background absorption due to collagen, et cetera
mua_blood = (mua_blood_oxy(wavelength)*oxy # Absorption due to
            + mua_blood_deoxy(wavelength)*(1-oxy)) # pure blood
mua = mua_blood*bvf + mua_other

# reduced scattering coefficient ($\mu_s^\prime$ in lab text)
# the numerical constants are thanks to N. Bashkatov, E. A. Genina and
# V. V. Tuchin. Optical properties of skin, subcutaneous and muscle
# tissues: A review. In: J. Innov. Opt. Health Sci., 4(1):9-38, 2011.
# Units: 1/m
musr = 100 * (17.6*(wavelength/500)**-4 + 18.78*(wavelength/500)**-0.22)

# mua and musr are now available as shape (3,) arrays
# Red, green and blue correspond to indexes 0, 1 and 2, respectively

# TODO calculate penetration depth
p_finger = np.sqrt(1/(3*(mua+musr)*mua))
p_blod = np.sqrt(1/(3*(mua_blood+musr)*mua_blood))
d_finger = 8.45e-3
d_blodåre = 300e-6
T_blod = np.exp(-(1/p_blod)*d_blodåre)*100
T_vev = np.exp(-(1/p_finger)*d_blodåre)*100
T_finger = np.exp(-(1/p_finger)*d_finger)*100

K = (T_finger-T_blod)/T_blod

print("penetrasjonsdybde: ", p_finger)
print("Transmisjonskoeffisient: ", T_finger)

print("Transmisjonskoeffisient i vev: ", T_vev)
print("Transmisjonskoeffisient i blodåre: ", T_blod)
print("Kontrast: ", K)