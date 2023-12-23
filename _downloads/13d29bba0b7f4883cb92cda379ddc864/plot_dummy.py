"""
==============
A dummy script
==============

Dummy script to illustrate structure of examples folder 
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
plt.plot(t, ca, 'r-')
plt.plot(t, 0*t, 'k-')
plt.xlabel('Time (sec)')
plt.ylabel('Plasma concentration (mM)')
plt.show()

# %%
# The bolus arrival time (BAT) defaults to 30s. What happens if we change it? Let's try, by changing it in steps of 30s:

ca = dcmri.aif_parker(t, BAT=0)
plt.plot(t, ca, 'b-', label='BAT = 0s')
ca = dcmri.aif_parker(t, BAT=30)
plt.plot(t, ca, 'r-', label='BAT = 30s')
ca = dcmri.aif_parker(t, BAT=60)
plt.plot(t, ca, 'g-', label='BAT = 60s')
ca = dcmri.aif_parker(t, BAT=90)
plt.plot(t, ca, 'm-', label='BAT = 90s')
plt.xlabel('Time (sec)')
plt.ylabel('Plasma concentration (mM)')
plt.legend()
plt.show()

# %%
# the dose defaults to 0.1- what happens if we change it too?

'''
Commenting this out for now as 'dose' is no longer defined as an argument
in aif_parker function and this prevents docs GH action from running.
ca = dcmri.aif_parker(t, BAT=0, dose=0.05)
plt.plot(t, ca, 'b-', label='BAT = 0s, dose = 0.05')
ca = dcmri.aif_parker(t, BAT=30, dose=0.1)
plt.plot(t, ca, 'r-', label='BAT = 30s, dose = 0.1')
ca = dcmri.aif_parker(t, BAT=60, dose=0.2)
plt.plot(t, ca, 'g-', label='BAT = 60s, dose = 0.2')
ca = dcmri.aif_parker(t, BAT=90, dose=0.3)
plt.plot(t, ca, 'm-', label='BAT = 90s, dose = 0.3')
plt.xlabel('Time (sec)')
plt.ylabel('Plasma concentration (mM)')
plt.legend()
plt.show()
'''

# Choose the last image as a thumbnail for the gallery
# sphinx_gallery_thumbnail_number = -1
