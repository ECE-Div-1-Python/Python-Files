
            # Convert to lowercase by adding 32 to the ASCII value
            result += chr(ord(char) + 32)
        else:
            result += char
    return result
