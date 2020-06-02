def merge_sorted_files(left, right, merged):
    """Merges two sorted files into one sorted file.

    Don't use any lists.

    Only one item from each input file assigned to a variable at any one time.

    Args:
        left (file object): A file object with sorted contents
        right (file object): a second file object with sorted contents
        merged (file object): an empty file object to which the merged file will
            be written

    """

    leftfile = open(left, 'r', encoding='utf-8')
    rightfile = open(right, 'r', encoding='utf-8')
    mergedfile = open(merged, 'w', encoding='utf-8')

    left_item = leftfile.readline().rstrip()
    right_item = rightfile.readline().rstrip()
    while left_item != '' and right_item != '':
        # Either of those would mean you'd reached the end of that file.
        #   This is this algorithm's equivalent of the book's mergesort's
        #   while left_index < len(left)... condition.
        #   Can't call len() on the file and get back the number of lines.
        #   (You can do len(file.readlines()), but that will read to the end
        #   of the file, so further file.readline() calls will return empty
        #   strings).
        print(f"left_item = {left_item}, right_item = {right_item}")
        if left_item <= right_item:
            mergedfile.write(left_item + '\n') # left value is smaller
            left_item = leftfile.readline().rstrip()
        else:
            mergedfile.write(right_item + '\n') # right value is smaller
            right_item = rightfile.readline().rstrip()

    if left_item == '': # left.txt ran out of lines first, so lines remain in right
        mergedfile.write(right_item + '\n')
        for right_item in rightfile:
            mergedfile.write(right_item + '\n')
    else: # right ran out first
        mergedfile.write(left_item + '\n')
        for left_item in leftfile:
            mergedfile.write(left_item + '\n')

    leftfile.close()
    rightfile.close()
    mergedfile.close()
            

def main():
    merge_sorted_files('left.txt', 'right.txt', 'merged.txt')

if __name__ == '__main__':
    main()
