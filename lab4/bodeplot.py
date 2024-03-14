import csv
import matplotlib.pyplot as plt

header = []
data = []


filename = "test2.csv"
with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvreader)
 
    for datapoint in csvreader:
  
        values = [float(value) for value in datapoint]
        data.append(values)
           

f = [p[0] for p in data]
ch1 = [p[1] for p in data]
ch2 = [p[2] for p in data]


#plt.plot(f, ch1, color = "hotpink")
plt.plot(f, ch2, color = "hotpink")
plt.vlines(3.5, 0, 20, color = "orange")
plt.vlines(4800, 0, 20, "orange")
plt.hlines(17, 0.5, 40000, "mediumblue")
plt.xscale('log')
plt.xlabel("frequency, log scale")
plt.ylabel("Mignitude i dB")
plt.show()