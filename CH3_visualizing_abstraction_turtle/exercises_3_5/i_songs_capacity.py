"""
Exercise 3.5.9
2020-03-28 20:14
"""


def songs(capacity, bitrate):
        """Returns the number of 4-minute songs that can fit on a storage device
        with a given capacity.

        Args:
            capacity (int): Capacity of the storage device in gigabytes.
            bitrate (int): Sampling rate of each 4 minute song, in kilobits per
                second.

        Returns:
            (int): The number of complete songs that can fit on the device.
        """
        song_size = get_song_bits(bitrate)
        capacity_in_bits = capacity * (2 ** 30) * 8 # Convert GB to bytes, then bytes to bits
        songs = capacity_in_bits // song_size # Floor division--fractional song isn't playable 
        return songs

def get_song_bits(bitrate):
        """Returns the number of bits in a 4-minute song of given bitrate.

        Args:
            bitrate(int): Sampling rate of the 4 minute song, in kilobits per
                second.

        Returns:
            (float): The number of gigabytes in the song.
        """
        seconds = 4 * 60 # Get number of seconds in a 4 minute song.    
        bits = seconds * bitrate * (2 ** 10) # Number of seconds multiplied by bits per second, i.e. the bitrate
        return bits

def main():
    capacity = float(input("Capacity of the storage device in GB: "))
    bitrate = float(input("Bitrate in kilobits per second: "))
    print(f"The device can hold {songs(capacity, bitrate)} songs")

main()
