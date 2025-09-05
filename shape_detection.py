'''
# Team ID:          eYRC#4686
# Theme:            Krishi coBot
# Author List:      Uthkarsh Mandloi
# Filename:         shape_detection.py
# Functions:        detect_shapes, main
# Global variables: None
'''

import cv2
import numpy as np

def detect_shapes(image_path):
    '''
    Purpose:
    ---
    Detects green triangles and squares in the given image using OpenCV.
    
    Input Arguments:
    ---
    `image_path` :  [ str ]
        Path to the input image
    
    Returns:
    ---
    `triangle_count` :  [ int ]
        Number of green triangles detected in the image
    
    `square_count` :  [ int ]
        Number of green squares detected in the image
    
    Example call:
    ---
    detect_shapes("input_image.png")
    '''
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image file '{image_path}' not found or cannot be opened.")
    
    # Convert to HSV color space for better color detection
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Define green color range
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])
    
    # Mask the green regions
    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    triangle_count = 0
    square_count = 0
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 200:  # Filter out small contours (noise)
            continue
        # Approximate the contour shape
        approx = cv2.approxPolyDP(cnt, 0.03*cv2.arcLength(cnt, True), True)
        # Count triangles
        if len(approx) == 3:
            triangle_count += 1
        # Count squares / rectangles
        elif len(approx) == 4:
            # Check aspect ratio to confirm square
            x, y, w, h = cv2.boundingRect(approx)
            ar = w / float(h)
            # Check if all angles are close to 90 degrees
            def angle(pt1, pt2, pt0):
                dx1 = pt1[0][0] - pt0[0][0]
                dy1 = pt1[0][1] - pt0[0][1]
                dx2 = pt2[0][0] - pt0[0][0]
                dy2 = pt2[0][1] - pt0[0][1]
                return (dx1*dx2 + dy1*dy2) / (np.sqrt((dx1*dx1 + dy1*dy1) * (dx2*dx2 + dy2*dy2)) + 1e-10)
            angles = [angle(approx[i], approx[(i+2)%4], approx[(i+1)%4]) for i in range(4)]
            # Check if all sides are nearly equal
            def side_length(pt1, pt2):
                return float(np.linalg.norm(pt1[0] - pt2[0]))
            sides = [side_length(approx[i], approx[(i+1)%4]) for i in range(4)]
            max_side = max(sides)
            min_side = min(sides)
            # Stricter checks for square: aspect ratio, angles, and side equality
            if 0.98 <= ar <= 1.02 and all(abs(a) < 0.15 for a in angles) and (min_side / max_side) > 0.95:
                square_count += 1
    
    return triangle_count, square_count

def main():
    '''
    Purpose:
    ---
    Main function to read the input image, call detect_shapes, and print results.
    
    Input Arguments:
    ---
    None
    
    Returns:
    ---
    None
    
    Example call:
    ---
    Called automatically when script is run
    '''
    image_path = "color-shapes.jpg"
    triangles, squares = detect_shapes(image_path)
    
    print("Number of green triangles:", triangles)
    print("Number of green squares:", squares)

if __name__ == "__main__":
    main()
