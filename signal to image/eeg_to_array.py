from BCI2kReader import BCI2kReader as b2k
import numpy as np
from PIL import Image as im
import cv2

#baca data sinyal eeg
filename = "./dataset - Copy/autism/Bader_Autism_24_11_2011S001R01.dat"
with b2k.BCI2kReader(filename) as test:
        my_states = test.read(-1)
        my_signals, stateslice = test[100:5000]


#ubah sinyal ke citra
#backtorgb = cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)
my_signals = my_signals.astype(np.uint8)

#my_signals2 = cv2.cvtColor(my_signals,cv2.COLOR_GRAY2RGB)
#data = im.fromarray(my_signals)
image = cv2.applyColorMap(my_signals, cv2.COLORMAP_PLASMA)
my_image = image.astype(np.uint8)
data2 = im.fromarray(my_image)
#simpan citra
data2.save('eeg_signal_ke_citra.png')