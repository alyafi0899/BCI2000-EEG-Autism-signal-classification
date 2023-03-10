import pywt
from BCI2kReader import BCI2kReader as b2k
import numpy as np
import matplotlib.pyplot as plt

i = 0
j = 100
nama = 1

for nama in range(10):
        #baca data sinyal eeg
        filename = "Dhelal_Normal_15_6_2011S001R02.dat"
        with b2k.BCI2kReader(filename) as test:
                my_signals, stateslice = test[i:j]
                
        coeffs = pywt.dwt2(my_signals, 'haar')
        cA, (cH, cV, cD) = coeffs

        my_data2 = cA.astype(np.uint8)

        plt.figure(figsize=(100,50))
        plt.pcolormesh(my_data2, cmap='jet')
        plt.yscale('linear')
        plt.axis('off')
        plt.savefig(f'{nama}.png', transparent = True, bbox_inches='tight')
        i=i+100
        j=j+100
        print(f"i = {i}      ------      j={j}")

