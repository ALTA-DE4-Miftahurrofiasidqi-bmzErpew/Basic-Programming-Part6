def caesar(offset, input_str):
    alfabets = "abcdefghijklmnopqrstuvwxyz"
    split = offset % len(alfabets)
    shifted_alphabets = alfabets[split:] + alfabets[:split]

    alfabets_dict = {}
    for i, value in enumerate(shifted_alphabets):
        alfabets_dict[alfabets[i]] = value

    result = ""
    for i, v in enumerate(input_str):
        if v == " ":
            result += " "
        else:
            result += alfabets_dict[v]
    return result


if __name__ == "__main__":
    print(caesar(3, "abc"))  # def
    # print(caesar(2, "alta"))  # cnvc
    # print(caesar(10, "alterraacademy"))  # kvdobbkkmknowi
    # print(caesar(1, "abcdefghijklmnopqrstuvwxyz"))  # bcdefghijklmnopqrstuvwxyza
    # print(caesar(1000, "abcdefghijklmnopqrstuvwxyz"))  # mnopqrstuvwxyzabcdefghijkl
