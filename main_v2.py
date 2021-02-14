import matplotlib.pyplot as plt
import crop_image
import pandas as pd
from PIL import Image

# put the nordic track data here and the power zone image
nordic_data = '60PZE-MW-2020-12-05.csv'
power_zone_image = 'PZE60_MW_2020-12-05.jpg'
ftp = 134

# calculate the zones from the ftp input (0 is the bottom, index 1 is the first zone, etc.
zone_thresholds = (0, int(0.56 * ftp), int(0.76 * ftp), int(0.91 * ftp),
                   int(1.06 * ftp), int(1.21 * ftp), int(1.51 * ftp))

# TODO read the image input and determine where the color changes are.

# TODO each color change is a new zone (this will be converted for plotting the data)

# TODO convert the watts values into the necessary values for the plot

# TODO create the plot and make the original powerzone image the background image

# TODO plot the data from nordic track

# TODO save the plot to an image for viewing
