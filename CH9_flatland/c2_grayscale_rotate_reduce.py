import image # the book's simple Image object class, from book website

def color_to_gray(color):
    """Convert a color to a shade of gray.

    Args:
        color (tuple): Tuple representing an RGB color

    Returns:
        (tuple): tuple representing an equivalent gray
    """
    brightness = (color[0] + color[1] + color[2]) // 3 # mean
    return (brightness, brightness, brightness) # Why not just return one int?

def grayscale(photo):
    """Convert an image to grayscale.

    Args:
        photo (Image): an Image object, i.e. an instance of the book's simplified
            Image class.

    Returns:
        (Image): New grayscale Image object.
    """
    width = photo.width()
    height = photo.height()
    new_photo = image.Image(width, height, title='Grayscale image')
    for y in range(height):
        for x in range(width):
            color = photo.get(x, y)
            new_photo.set(x, y, color_to_gray(color))
    return new_photo

def rotate_90(photo):
    """Rotate an image 90 degrees clockwise.

    Args:
        photo (Image): An Image object.

    Returns:
        (Image): New rotated Image object.
    """

    width = photo.width()
    height = photo.height()
    new_photo = image.Image(height, width, title='Rotated image')
    for y in range(height):
        for x in range(width):
            color = photo.get(x, y)
            new_photo.set(height - y - 1, x, color)
    return new_photo

def reduce(photo):
    """Reduce an image to one quarter of its size.

    Args:
        photo (Image): An Image object

    Returns:
        (Image): New, reduced Image object.
    """
    # Simplistic algorithm that doesn't average the RGB values of the reduced
    #   pixels.
    width = photo.width()
    height = photo.height()
    new_photo = image.Image(width // 2, height // 2, title='Reduced image')
    for y in range(0, height, 2):
        for x in range(0, width, 2):
            color = photo.get(x, y)
            new_photo.set(x // 2, y // 2, color)
    return new_photo

def main():
    file = 'penguin.gif'
    title = 'Penguin'
    photo = image.Image(file=file, title=title)
    photo_gray = grayscale(photo)
    photo_rotated = rotate_90(photo)
    photo_reduced = reduce(photo)
    photo.show()
    photo_gray.show()
    
    photo_rotated.show()
    photo_reduced.show()
    image.mainloop()

    # combine grayscale, rotate, and reduce on a single image:
    photo_multi = reduce(photo_gray)
    photo_multi = rotate_90(photo_multi)
    photo_multi = rotate_90(photo_multi)
    photo_multi.show()

if __name__ == '__main__':
    main()
    
