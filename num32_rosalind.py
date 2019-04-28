f = open("example.txt", "r")

pattern = f.readline().strip()

f.close()


print(sorted(pattern))
