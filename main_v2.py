import matplotlib.pyplot as plt
import crop_image
import pandas as pd
from PIL import Image

# put the nordic track data here and the power zone image
nordic_data = '60PZE-MW-2020-12-05.csv'
power_zone_image = 'PZE60_MW_2020-12-05.jpg'
ftp = 138

# calculate the zones from the ftp input

# read the image input and determine where the color changes are.
# each color change is a new zone (this will be converted for plotting the data)

# convert the watts values into the necessary values for the plot

# create the plot and make the original powerzone image the background image

# plot the data from nordic track

# save the plot to an image for viewing
