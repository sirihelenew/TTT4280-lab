# import numpy as np 
# import matplotlib.pyplot as plt

# #def diskret signal 1
# #def diskret signal 2
# #tidsforskyvning l, uttrykt i antall samples

# #def krysskorrelasjon(x, y, l):
# # 


# def krysskorrelasjon(x, y):
#     N = len(x)
#     M = len(y)
#     L = N + M - 1
#     z = np.zeros(L)
#     for n in range(L):
#         for m in range(M):
#             if n - m >= 0 and n - m < N:
#                 z[n] += x[n - m] * y[m]
#     return z




# # signal1, signal2 = ...

# # Beregn krysskorrelasjonen
# cross_correlation = np.correlate(signal1, signal2, mode='full')

# # Finn indeksen til maksimalverdien i krysskorrelasjonen
# max_index = np.argmax(np.abs(cross_correlation))

# # Beregn forsinkelsen
# # Siden resultatet fra np.correlate med mode='full' er 2*N-1 lang, der N er lengden på signalene,
# # er midtpunktet (null forskyvning) ved indeks N-1. Dermed er forsinkelsen max_index - (N-1).
# delay_samples = max_index - (len(signal1) - 1)

# # Konverter forsinkelsen fra prøver til sekunder
# delay_seconds = delay_samples / fs
# return delay_seconds

# print(f"Effektiv forsinkelse: {delay_seconds} sekunder")

# # (Valgfritt) Plot krysskorrelasjonen for å visualisere
# plt.figure()
# plt.plot(cross_correlation)
# plt.title("Krysskorrelasjon mellom de to signalene")
# plt.xlabel("Forskyvning (prøver)")
# plt.ylabel("Krysskorrelasjon")
# plt.show()
