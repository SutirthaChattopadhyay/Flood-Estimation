import cv2
import numpy as np

# Load the image
image = cv2.imread('E:\Only-CO-Lang\Python Code\CODE-py\Flood Ai\mine\srm\SRM\srm1.tif')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define the threshold value (adjust this according to your image characteristics)
threshold_value = 150
threshold1 = 100  # Adjust this value based on your image characteristics
threshold2 = 200  # Adjust this value based on your image characteristics

# Define the lower and upper bounds for the blue, green, and red channels
lower_blue = 100  # Adjust these values based on your color characteristics
lower_green = 300
lower_red = 300
upper_blue = 200
upper_green = 200
upper_red = 200

lower_bound = np.array([lower_blue, lower_green, lower_red])
upper_bound = np.array([upper_blue, upper_green, upper_red])

# Apply Canny edge detection
edges = cv2.Canny(gray_image, threshold1, threshold2)

# Define color ranges for water
lower_bound = (lower_blue, lower_green, lower_red)
upper_bound = (upper_blue, upper_green, upper_red)

# Create a mask for the water color range
mask = cv2.inRange(image, lower_bound, upper_bound)

# Define the kernel size for morphological operations
kernel_size = 5  # Adjust this value based on your needs

# Apply morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
opened_mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# Find contours of detected water regions
contours, _ = cv2.findContours(opened_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Display the result
cv2.imshow('Water Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()





