import image # the book's simple Image object class, from book website

def warmer(photo, factor):
    """Returns an Image object that is "warmer" than the original by the factor
    passed as parameter, by ingreasing the intensities of both red and green
    channels."""
    width = photo.width()
    height = photo.height()
    new_photo = image.Image(width, height, title='Warmer image')
    for y in range(height):
        for x in range(width):
            color = photo.get(x, y)
            new_color = (max(min(int(color[0] + factor), 255), 0),
                         max(min(int(color[1] + factor), 255), 0),
                         color[2])
            new_photo.set(x, y, new_color)
    return new_photo

def color_to_gray(color):
    """Convert a color to a shade of gray.

    Args:
        color (tuple): Tuple representing an RGB color

    Returns:
        (tuple): tuple representing an equivalent gray
    """
    brightness = int((0.2126 * color[0])
                  + (0.7152 * color[1])
                  + (0.0722 * color[2]))
    return (brightness, brightness, brightness)

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
    photo_warmer = warmer(photo, -100)
    photo.show()
    photo_warmer.show()
    image.mainloop()


if __name__ == '__main__':
    main()
    
