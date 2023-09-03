#calculates the area and perimeter
def calculator(question):
  #error incase one of the values is equal to or less than 0
  zero_error = ("Error, the height and all sides of a shape must be more than zero")
  
  Area_list = ["w*l", "w*w", "0.5b*h", "2*3.14*(r*r)", "h*b"]
  Perimeter_list = ["2w+2l", "4w", "2b+2s", "a+b+c", "2*3.14*r"]
  a = 0
  b = 0
  c = 0
  h = 0
  r = 0
  s = 0
  l = 0
  w = 0

  #gets dimensions from user and checks that they are more than 0
  try: 
    if shape_selected == "circle":
      r = float(input("What is the radius? "))
      if r <= 0:
        print(zero_error)
      
        
    elif shape_selected == "triangle":
      b = float(input("What is the length of the base? "))
      h = float(input("What is the height? "))
      a = float(input("What is the length of one of the sides? "))
      c = float(input("What is the length of the other side? "))
      if a <= 0 or h <= 0 or b <= 0 or c <= 0:
        print(zero_error)
      
    
    elif shape_selected == "square":
      w = float(input("What is the width? "))
      if w <= 0:
        print(zero_error)

    
    elif shape_selected == "rectangle":
      w = float(input("What is the width? "))
      l = float(input("What is the length? "))
      if w <= 0 or l <= 0:
        print(zero_error)
      
    
    else:
      b = float(input("What is the length of the base? "))
      h = float(input("What is the height? "))
      s = float(input("What is the length of one of the sides? "))
      if b <= 0 or h <= 0 or s <= 0:
        print(zero_error)
  
  except ValueError:
    print("You must enter a number")

  #range checker for the height of a triangle/parallelogram
  if shape_selected == "triangle":
    number = a - c
    if number <= 0:
      lowest_number = a
    else:
      lowest_number = c

    if lowest_number <= h and not (b == 0 or h == 0 or a == 0 or c == 0):
      size_error = "true"
    elif b == 0 or h == 0 or a == 0 or c == 0:
      size_error = "zero"
    else:
      size_error = "false"
      
      
    

  if shape_selected == "parallelogram":
    if s <= h and not (b <= 0 or h <= 0 or s <= 0):
      size_error = "true"
    elif b <= 0 or h <= 0 or s <= 0:
      size_error = "zero"
    else:
      size_error = "false"
       
  # calculates the area and perimeter of the chosen shape
  Area_list = [w*l, w*w, 0.5*b*h, 2*3.14*(r*r), h*b]
  Perimeter_list = [(2*w)+(2*l), 4*w, (2*b)+(2*s), a+b+c, 2*3.14*r]
  if shape_selected == "circle":
    perimeter = format(Perimeter_list[4], ".2f")
    area = format(Area_list[3], ".2f")
    if area == 0:
      print("")
    else:
      print("Area = {}, perimeter = {}".format(area, perimeter))
      
  elif shape_selected == "square":
    perimeter = format(Perimeter_list[1], ".2f")
    area = format(Area_list[1], ".2f")
    if area == 0:
      print("")
    else:
      print("Area = {}, perimeter = {}".format(area, perimeter))
      
  elif shape_selected == "rectangle":
    perimeter = format(Perimeter_list[0], ".2f")
    area = format(Area_list[0], ".2f")
    if area == 0:
      print("")
    else:
      print("Area = {}, perimeter = {}".format(area, perimeter))
  
  elif shape_selected == "triangle":
    perimeter = format(Perimeter_list[3], ".2f")
    area = format(Area_list[2], ".2f")
    # for triangle and parallelogram, if height is bigger than the smallest side, tells the user it cannot be
    if size_error == "true":
      print("The height of a triangle must be smaller than the length of the smallest side")
    elif size_error == "zero":
      print("")
    else:
      print("Area = {}, perimeter = {}".format(area, perimeter))
  
  elif shape_selected == "parallelogram":
    perimeter = format(Perimeter_list[2], ".2f")
    area = format(Area_list[4], ".2f")
    if size_error == "true":
      print("The height of a parallelogram must be smaller than the      length of one side")
    elif size_error == "zero":
      print("")
    else:
      print("Area = {}, perimeter = {}".format(area, perimeter))
  else:
    print("")

      
while True:    
  shape_selected = input("Shape: ")
  calculator(shape_selected)