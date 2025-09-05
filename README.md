
# eyrc2025_task0
# Task 0 - Image Processing (Krishi coBot)

## Team Details
- **Team ID:** eYRC#4686  
- **Theme:** Krishi coBot  
- **Author:** Uthkarsh Mandloi  

## Task Description
This task involves detecting **green triangles and squares** in an image using OpenCV.  
The objective is to prepare for upcoming robotics tasks involving computer vision.

**Input:** An image containing colored shapes (`color-shapes.jpg`).  
**Output:** Number of green triangles and green squares detected.

---

## Files
- `shape_detection.py` : Python script to detect green triangles and squares.  
- `color-shapes.jpg` : Sample input image.  

---

## Requirements
- Python 3.x  
- OpenCV (`cv2`)  
- NumPy  


Install dependencies using pip:

```bash
pip install opencv-python numpy
```

---

## How to Run

# Run the script from the command line:
```bash
python3 shape_detection.py
```
# The script will print the number of green triangles and green squares:
```bash
Number of green triangles: X
Number of green squares: Y
```

---

#
## Functions

### detect_shapes(image_path)

Detects green triangles and squares in a given image.

**Input Arguments:**

- `image_path` : [str] Path to the input image.

**Returns:**

- `triangle_count` : [int] Number of green triangles detected.
- `square_count` : [int] Number of green squares detected.

**Example:**

```python
triangles, squares = detect_shapes("color-shapes.jpg")
```

### main()

Calls detect_shapes on the input image and prints the results.

**Input Arguments:** None
**Returns:** None

**Example:**

```bash
python3 shape_detection.py
```

## Notes

- The script uses HSV color space to detect green shapes.
- Small contours (area < 200) are ignored to reduce noise.
- Squares are confirmed by checking side lengths, angles, and aspect ratio.

