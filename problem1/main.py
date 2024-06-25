def compare(a, b):
    if len(a) > len(b):
        a = b
        b = a

    pattern = ""
    for i, huruf in enumerate(a):
        if huruf == b[i]:
            pattern += huruf
    return pattern


if __name__ == "__main__":
    print(compare("AKA", "AKASHI"))  # AKA
    print(compare("KANGOORO", "KANG"))  # KANG
    print(compare("KI", "KIJANG"))  # KI
    print(compare("KUPU-KUPU", "KUPU"))  # KUPU
    print(compare("ILALANG", "ILA"))  # ILA
