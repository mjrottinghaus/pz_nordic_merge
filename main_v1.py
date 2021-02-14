import matplotlib.pyplot as plt
import crop_image
import pandas as pd
from PIL import Image

# put the nordic track data here and the power zone image
nordic_data = '60PZE-MW-2020-12-05.csv'
power_zone_image = 'PZE60_MW_2020-12-05.jpg'

# crop the power zome image down so that we have a consistent image to plot on
power_zone_image = crop_image.crop_image(power_zone_image, "power_zone_image.png")

# load in the power zone image here and create the initial plot with the image as the background
# read the image
im = Image.open(power_zone_image)

# store the nordic track data in a data frame
nordic_df = pd.read_csv(nordic_data, skiprows=2)

# apply offsets to the data to get it to line up with image chart
nordic_df["Watts"] += 50
df1 = nordic_df[nordic_df.index % 5 != 0]  # Excludes every 5th row starting from 0

# flip image
#out = im.transpose(Image.FLIP_TOP_BOTTOM)
#out.save(power_zone_image)
img = plt.imread(power_zone_image)
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, len(df1), 0, 500])
ax.set_ylim(0, 500)

# plot the nordic track data on the plot with the necessary offsets
plt.plot(df1["Time"], df1["Watts"])

# save the plot as an image
plt.savefig("output1.png")
