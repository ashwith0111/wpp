import numpy as np
def generate_magic_square(N):
    if N % 2 != 0:
        return generate_odd_magic_square(N)
    elif N % 4 == 0:
        return generate_doubly_even_magic_square(N)
    else:
        return generate_singly_even_magic_square(N)
def generate_odd_magic_square(N):
    magic_square = np.zeros((N, N), dtype=int)
    i, j = 0, N // 2
    for num in range(1, N * N + 1):
        magic_square[i, j] = num
        new_i, new_j = (i - 1) % N, (j + 1) % N
        if magic_square[new_i, new_j]:
            i += 1
        else:
            i, j = new_i, new_j
    return magic_square
def generate_doubly_even_magic_square(N):
    magic_square = np.zeros((N, N), dtype=int)
    num = 1
    for i in range(0, N, 4):
        for j in range(0, N, 4):
            block = np.array([[1, 2, 3, 4], [12, 13, 14, 15], [11, 16, 17, 18], [10, 9, 8, 7]])
            magic_square[i:i+4, j:j+4] = block + num - 1
            num += 16
    return magic_square
def generate_singly_even_magic_square(N):
    magic_square = np.zeros((N, N), dtype=int)
    num = 1
    for i in range(N):
        for j in range(N):
            magic_square[i, j] = num
            num += 1
    return magic_square
def print_magic_square(square):
    for row in square:
        print(' '.join([str(num).rjust(3) for num in row]))
    print()
for N in [4, 5, 6, 7, 8]:
    print(f"Magic Square for N = {N}:")
    magic_square = generate_magic_square(N)
    print_magic_square(magic_square)