def compare(a, b):
    if len(a) > len(b):
        a = b
        b = a

    if b.count(a) == 1:
        return a


if __name__ == "__main__":
    print(compare("AKA", "AKASHI"))  # AKA
    print(compare("KANGOORO", "KANG"))  # KANG
    print(compare("KI", "KIJANG"))  # KI
    print(compare("KUPU-KUPU", "KUPU"))  # KUPU
    print(compare("ILALANG", "ILA"))  # ILA
