#https://cs50.harvard.edu/x/2025/psets/1/mario/less/

while True:
    try:
        height = int(input("Height: "))
        spaces = ""
        hash_count = 1
        while height <= 0:
            height = int(input("Height: "))
        count = height - 1
        for num in range(height):
            spaces += count * " "
            print(spaces + hash_count * "#")
            hash_count += 1
            count -= 1
            spaces = ""
        break
    except ValueError:
        height = input("Height: ")