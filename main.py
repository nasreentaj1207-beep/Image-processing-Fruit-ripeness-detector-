import cv2
import numpy as np
import matplotlib.pyplot as plt


# ==========================================
# FUNCTION TO DISPLAY IMAGE
# ==========================================

def display_image(image, title):

    plt.figure(figsize=(6, 5))

    # OpenCV uses BGR, matplotlib uses RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.imshow(image_rgb)
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


# ==========================================
# READ IMAGE
# ==========================================

image_path = input("Enter image path: ")

image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
    exit()


# ==========================================
# CONVERT IMAGE TO HSV
# ==========================================

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


# ==========================================
# GREEN COLOR - UNRIPE
# ==========================================

lower_green = np.array([35, 40, 40])
upper_green = np.array([90, 255, 255])

green_mask = cv2.inRange(
    hsv,
    lower_green,
    upper_green
)


# ==========================================
# YELLOW COLOR - RIPE
# ==========================================

lower_yellow = np.array([20, 40, 40])
upper_yellow = np.array([35, 255, 255])

yellow_mask = cv2.inRange(
    hsv,
    lower_yellow,
    upper_yellow
)


# ==========================================
# RED COLOR - RIPE
# ==========================================

lower_red1 = np.array([0, 40, 40])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([170, 40, 40])
upper_red2 = np.array([180, 255, 255])

red_mask1 = cv2.inRange(
    hsv,
    lower_red1,
    upper_red1
)

red_mask2 = cv2.inRange(
    hsv,
    lower_red2,
    upper_red2
)

red_mask = red_mask1 + red_mask2


# ==========================================
# COUNT PIXELS
# ==========================================

green_pixels = cv2.countNonZero(green_mask)
yellow_pixels = cv2.countNonZero(yellow_mask)
red_pixels = cv2.countNonZero(red_mask)


# ==========================================
# CALCULATE TOTAL COLOR PIXELS
# ==========================================

total_pixels = (
    green_pixels +
    yellow_pixels +
    red_pixels
)


if total_pixels == 0:

    print("No fruit color detected!")
    exit()


# ==========================================
# CALCULATE PERCENTAGES
# ==========================================

green_percentage = (
    green_pixels / total_pixels
) * 100

yellow_percentage = (
    yellow_pixels / total_pixels
) * 100

red_percentage = (
    red_pixels / total_pixels
) * 100


# ==========================================
# RIPE COLOR
# ==========================================

ripe_percentage = (
    yellow_percentage +
    red_percentage
)


# ==========================================
# IDENTIFY FRUIT
# ==========================================

if green_percentage > ripe_percentage:

    result = "UNRIPE FRUIT"

else:

    result = "RIPE FRUIT"


# ==========================================
# PRINT RESULT
# ==========================================

print("\n==============================")
print("   FRUIT RIPENESS DETECTION")
print("==============================")

print("Green  :", round(green_percentage, 2), "%")
print("Yellow :", round(yellow_percentage, 2), "%")
print("Red    :", round(red_percentage, 2), "%")

print("------------------------------")
print("RESULT :", result)
print("==============================")


# ==========================================
# DISPLAY ORIGINAL IMAGE
# WITH RESULT AS TITLE
# ==========================================

display_image(image, result)
