import numpy as np


L = 100e-3 
C1 = 100e-6  
C2 = 470e-6  
C3 = 100e-9  

C_total = C2 + C3

f_c = 1 / (2 * np.pi * np.sqrt(L * C_total))

print(f_c)  
