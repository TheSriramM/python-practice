
def redeem_prizes(points):
  # Finish the function to convert buckets of cookie dough to prizes
  points_needed = 5
  count = 1
  no = 0
  while True:
    if int(points) > points_needed:
      if count < 2:
        count += 1
      no += 1
      points_needed = points_needed * count
    elif int(points) < points_needed:
      return no

    elif int(points) < 5:
       return count - 1

    elif int(points) == points_needed:
        return count
    


# Write the rest of your program here
print("COOKIE DOUGH SALES POINTS AND PRIZES TRACKER")
name = input("Name: ")
dictio = {}
# pdb.set_trace()
while name:
    name = name.title()
    sold = int(input("Cookie dough sold: "))
    try:
      if sold <= 0:
          print("Please enter a valid integer for the cookie not dough sold.")
          sold = input("Cookie dough sold: ")
    except ValueError:
        print("Please enter a valid integer for the cookie dough sold.")
        sold = input("Cookie dough sold: ")     
            
    if name not in dictio:
        dictio[name] = sold
        name = input("Name: ")
        if name == False:
          break
    else:
        dictio[name] = dictio[name] + sold
        name = input("Name: ")
        if name == False:
            break

print("Selling over! Let's see how everyone did!")
for name, points in dictio.items():
  print(name + " has " + str(points) + " points and can redeem " + str(redeem_prizes(points)) + " prize(s).")