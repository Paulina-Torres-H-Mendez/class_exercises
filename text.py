fp=open("text.txt") # r is default
print(fp.read())
fp.close()


with open("text.txt") as f:
    print(f.read())


print("Read the file line by line")
line_number = 1
with open("text.txt", "r") as fp:
    for line in fp:
        print(f"{line_number}: {line}", end="")

        line_number += 1
print("done printing")