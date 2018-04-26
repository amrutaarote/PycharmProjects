number = [1, 2, 3, 4, 5, 10, 15, 20]
for item in number:
    print("The item number is", item)


run = True
current = 1

while run:
    if current == 100:
        run = False
    else:
        print(current)
        current += 1



