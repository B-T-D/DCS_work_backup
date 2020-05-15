#!/usr/bin/env python3

import image

def color2gray(color):
    """Convert a color to a shade a gray.

    Parameter:
        color: a tuple representing an RGB color

    Return value: a tuple representing an equivalent gray
    """

    average = sum(color) // 3
    return (average, average, average)
    
def rotate90(photo):
    """Rotate an image 90 degrees clockwise.

    Parameter:
        photo: an Image object

    Return value: a new rotated Image object
    """
    
    width = photo.width()
    height = photo.height()
    newPhoto = image.Image(height, width, title = 'Rotated image')
    for y in range(height):
        for x in range(width):
            color = photo.get(x, y)
            newPhoto.set(height - y - 1, x, color)
    return newPhoto
    
def reduce(photo):
    """Reduce an image to one quarter of its size.

    Parameter:
        photo: an Image object

    Return value: a new reduced Image object
    """
    
    width = photo.width()
    height = photo.height()
    newPhoto = image.Image(width // 2, height // 2, title = 'Reduced image')
    for y in range(0, height, 2):
        for x in range(0, width, 2):
            color = photo.get(x, y)
            newPhoto.set(x // 2, y // 2, color)
    return newPhoto

def grayscale(photo):
    """Convert a color image to grayscale.

    Parameter:
        photo: an Image object

    Return value: a new grayscale Image object
    """

    width = photo.width()
    height = photo.height()
    newPhoto = image.Image(width, height, title = 'Grayscale image')
    for y in range(height):
        for x in range(width):
            color = photo.get(x, y)
            newPhoto.set(x, y, color2gray(color))
    return newPhoto
    
def main():
    penguin = image.Image(file = 'penguin.gif', title = 'Penguin')
    penguinSmall = reduce(penguin)
    penguinGray = grayscale(penguinSmall)
    penguinRotate1 = rotate90(penguinGray)
    penguinRotate2 = rotate90(penguinRotate1)
    penguinRotate2.show()
    image.mainloop()
	
main()
