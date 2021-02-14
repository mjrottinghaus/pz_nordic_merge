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
# each color change is a new zone (this will be converted for plotting the data)
im = Image.open(power_zone_image)
pixels = im.load()

# go to aprox. the middle column of the image file
im_width, im_height = im.size
mid_column = im_width // 2

# read through until we find 7 different colors and record where those pixels are at
zone_color_rows = []
for row in range(10, im_height - 10):
    # get the current pixel
    current_pixel = pixels[mid_column, row]
    # check to see if is substantially different the the 10 values behind it
    total_difference = 0
    for i in range(row - 10, row):
        prev_pixel = pixels[mid_column, i]
        for j in range(0, 3):
            difference = abs(1 - abs((current_pixel[j] + 1) / (prev_pixel[j] + 1)))
            total_difference += difference
    print(row, current_pixel, total_difference)
    if total_difference > 8:
        in_data = False
        for k in range(5 - row, row + 5):
            if k in zone_color_rows:
                in_data = True
        if not in_data:
            zone_color_rows.append(row)

print(zone_color_rows)
# these are the corresponding pixel values for the zones

# TODO convert the watts values into the necessary values for the plot
# load in the data from the csv file
# create a new column that represents the pixel value on the chart

# TODO create the plot and make the original powerzone image the background image
# fit the image to the plot that we are looking at (this is based off of how many rows in the data frame)

# TODO plot the data from nordic track

# TODO save the plot to an image for viewing
