def dem(message):
    def decode_helper(s, index, path, result):
        if index == len(s):
            result.append(path)
            return

        if s[index] != '0':
            num = int(s[index])
            decode_helper(s, index + 1, path + chr(64 + num), result)
        if index + 1 < len(s) and s[index] != '0':
            num = int(s[index:index + 2])
            if 1 <= num <= 26:
                decode_helper(s, index + 2, path + chr(64 + num), result)

    result = []
    decode_helper(message, 0, "", result)
    return result

em = input("Enter the message: ")
dm = dem(em)
print(f"Decoded messages for '{em}':")
for i in dm:
    print(i)