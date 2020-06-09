from class_pair import Pair
import time

def splits(pairs, time):
    """
    Updates list of splits.
    
    Args:
        pairs (list): list of Pair objects
        time (int): current split time. I'm assuming the book means time
            elapsed since last split.

    Returns:
        None
    """
    pass
    # all in main. Book's way doesnt take CLI inputs. 

def main():
    splits = []
    press = input("press p to start watch\n>>>")
    if press.lower() == 'p':
        pair = Pair(0, 0)
        split_pairs = [pair]
        start = time.time()
        last_split = start
        prompt = "Press s to enter a split, q to stop the watch and quit:\n>>>"
        while press.lower() != 'q':
            if press.lower() == 's':
                split = time.time()
                split_time =round(split - last_split, 3)
                elapsed = round(split - start, 3)
                last_split = split
                new_pair = Pair(split_time, elapsed)
                split_pairs.append(new_pair)
                print(f"split: {round(split_time, 3)},\
total elapsed: {round(elapsed, 3)}")
            press = input(prompt)
    splits(split_pairs

if __name__ == '__main__':
    main()
    
    
