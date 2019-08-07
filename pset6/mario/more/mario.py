height = input("Height: ")

if( height.isdigit()):
    height = int(height)
else:
    height = input("Height: ")

if height < 1 or height > 8:
    height = int(input("Height: "))

for x in range(1, height + 1):
    blocks = ""
    for y in range(x):
        blocks += "#"
    spaces = ""
    spacesInt = height - x
    for z in range(spacesInt):
        spaces += " "
    print(spaces + blocks + "  " + blocks)

