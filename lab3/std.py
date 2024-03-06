import numpy as np

puls = []
puls_klokke = [] 

puls_klokke_snitt = 0

for i in range(len(puls_klokke)):
    puls_klokke_snitt += puls_klokke[i]/len(puls_klokke)

#std med std funk:
puls_std1 = np.std(puls)

#std regne ut:
puls_var = 0

for i in range(len(puls)):
    puls_var += (puls[i]-puls_klokke_snitt)^2/len(puls)
    
puls_std2 = puls_var/2

print("Standardavvik funnet med np.std(): ", puls_std1)
print("Gjennomsnittelig puls målt med klokke: ", puls_klokke_snitt)
print("Standardavvik: ", puls_std2)



    

    
    


