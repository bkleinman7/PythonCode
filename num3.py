def reverse_string(string):
    for c in reversed(string):
        if c == "T":
            c = "A"
        elif c == "A":
            c = "T"
        elif c == "C":
            c = "G"
        elif c == "G":
            c = "C"
    return c
