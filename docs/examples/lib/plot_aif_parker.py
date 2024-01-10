"""
==============
The Parker AIF
==============

Simulating a Parker AIF with different settings. 
"""

# %%
# Import necessary packages
import numpy as np
import matplotlib.pyplot as plt
import dcmri

# %%
# Generate synthetic AIF with default settings and plot the result.

# Define time points in units of seconds - in this case we use a time resolution of 0.5 sec and a total duration of 6 minutes.
t = np.arange(0, 6*60, 0.5)

# Create an AIF with default settings
ca = dcmri.aif_parker(t)

# Plot the AIF over the full range
plt.plot(t, ca*1000, 'r-')
plt.plot(t, 0*t, 'k-')
plt.xlabel('Time (sec)')
plt.ylabel('Plasma concentration (mM)')
plt.show()

# %%
# The bolus arrival time (BAT) defaults to 30s. What happens if we change it? Let's try, by changing it in steps of 30s:

ca = dcmri.aif_parker(t, BAT=0)
plt.plot(t, ca*1000, 'b-', label='BAT = 0s')
ca = dcmri.aif_parker(t, BAT=30)
plt.plot(t, ca*1000, 'r-', label='BAT = 30s')
ca = dcmri.aif_parker(t, BAT=60)
plt.plot(t, ca*1000, 'g-', label='BAT = 60s')
ca = dcmri.aif_parker(t, BAT=90)
plt.plot(t, ca*1000, 'm-', label='BAT = 90s')
plt.xlabel('Time (sec)')
plt.ylabel('Plasma concentration (mM)')
plt.legend()
plt.show()


# Choose the last image as a thumbnail for the gallery
# sphinx_gallery_thumbnail_number = -1
