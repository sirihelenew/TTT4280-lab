import numpy as np

puls = [80.035, 79.959, 83.606, 88.165, 94.373]
puls_auto = [78.26, 75, 81.818, 81.818, 90]
#puls_klokke = [80, 75, 80, 85, 85] 

# puls_klokke_snitt = 0

# for i in range(len(puls_klokke)):
#     puls_klokke_snitt += puls_klokke[i]/len(puls_klokke)

#std med std funk:
puls_std1 = np.std(puls)

#std regne ut:
# puls_var = 0

# for i in range(len(puls)):
#     puls_var += (puls[i]-puls_klokke_snitt)**2/len(puls)
    
puls_std2 = np.sqrt(puls_var)

print("Standardavvik funnet med np.std(): ", puls_std1)
print("Gjennomsnittelig puls målt med klokke: ", puls_klokke_snitt)
print("Standardavvik: ", puls_std2)
