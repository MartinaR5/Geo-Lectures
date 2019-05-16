# Lecture 5: Snuffler exercise functions 
# 
# author: Eva Eibl eva.eibl@uni-potsdam.de
# SS 2019: Module MGPW02
# 16.5.2019
# -----------------------------
import Lec5_geyserEx_functions as h
import matplotlib.pyplot as plt
import numpy as np



# -- import the snuffler marker file, time in julian days --
julianday, evclass = h.read_snuffler_marker("geyser_markers.txt", length=0)
julianday = np.sort(julianday)
print(julianday)
plt.plot(julianday)
plt.show()



# -- calculate the waiting time after eruption/ duration of bursts in minutes --  

tdiff_easy = np.diff(julianday) *24*60
print(tdiff_easy)

l = len(julianday)
tdiff = np.zeros(l-1)
for i in range(l-1):
	tdiff[i] = (julianday[i+1] - julianday[i]) *24*60
print(tdiff)
plt.plot(tdiff)
plt.show()


# -- calculate mean time --



# -- plot waiting time after eruptions/ duration of bursts vs. time --
plot


# -- plot histogram of the intereruption times (1 h bins) -- 
hist













