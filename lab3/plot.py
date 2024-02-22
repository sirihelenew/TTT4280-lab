import matplotlib.pyplot as plt
import numpy as np

def import_video(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    result = []
    for x in lines:
        result.append(x.split(' ')[1])
    f.close()


