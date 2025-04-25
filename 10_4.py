import numpy as np
def adjust_string_lengths(arr, length=15):
    centered = np.char.center(arr, length, fillchar='_')
    left_justified = np.char.ljust(arr, length, fillchar='_')
    right_justified = np.char.rjust(arr, length, fillchar='_')
    return centered, left_justified, right_justified
strings = np.array(["apple", "banana", "cherry", "date"])
centered, left_justified, right_justified = adjust_string_lengths(strings)
print("Original Array:")
print(strings)
print("\nCentered (15 chars):")
print(centered)
print("\nLeft-justified (15 chars):")
print(left_justified)
print("\nRight-justified (15 chars):")
print(right_justified)