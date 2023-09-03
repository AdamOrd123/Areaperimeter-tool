#functions
#ensures user enters a valid response (y/n)
def string_check(question):
  while True:
    error = "You must enter yes/y or no/n"
    try:
      response = input(question).lower().strip()
      if response == "yes" or response == "y" or response == "n" or response == "no":
        return response
        break
      else:
        print(error)
    except ValueError:
      print(error)

#checks the user has entered a string, and that the string is in the list of shapes
def valid_shape(question):
  while True:
    error = ("Error, please enter square, rectangle, circle, triangle or  parallelogram")
    try:
      response = input(question).strip().lower()
    except ValueError:
      print(error)
  
    if response in shape_list:
      print("You have selected:{}".format(response))
      return response
      break
    else:
      print(error)
      continue

#checks that the user has entered a valid unit
def valid_unit(question):
  while True:
    error = ("Error, you must enter a valid, metric unit (m, cm, mm)")
    try:
      response = input(question).strip().lower()
    except ValueError:
      print(error)
    if response in units:
      print("You have selected: {}".format(response))
      return response
      break
    else:
      print(error)
      continue
  
#displays the correct equation for the shape
def equation_selector(question):
  Area_list = ["w*l", "w*w", "0.5b*h", "2*3.14*(r*r)", "h*b"]
  Perimeter_list = ["2w+2l", "4w", "2b+2s", "a+b+c", "2*3.14*r"]
  shape_selected = question 
  
  
  if shape_selected == "circle":
    perimeter = (Perimeter_list[4])
    area = (Area_list[3])
    print("Area = {}, perimeter = {}".format(area, perimeter))
      
  elif shape_selected == "square":
    perimeter = (Perimeter_list[1])
    area = (Area_list[1])
    print("Area = {}, perimeter = {}".format(area, perimeter))
      
  elif shape_selected == "rectangle":
    perimeter = (Perimeter_list[0])
    area = (Area_list[0])
    print("Area = {}, perimeter = {}".format(area, perimeter))
  
  elif shape_selected == "triangle":
    perimeter = (Perimeter_list[3])
    area = (Area_list[2])
    print("Area = {}, perimeter = {}".format(area, perimeter))
  
  elif shape_selected == "parallelogram":
    perimeter = (Perimeter_list[2])
    area = (Area_list[4])
    print("Area = {}, perimeter = {}".format(area, perimeter))
  else:
    print("")
 

#calculates the area and perimeter
def calculator(question):
  while True:
    shape_selected = (question)
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
  
      if lowest_number <= h and not (b <= 0 or h <= 0 or a <= 0 or c <= 0):
        size_error = "true"
      elif b <= 0 or h <= 0 or a <= 0 or c <= 0:
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
        return area, perimeter
        break
        
    elif shape_selected == "square":
      perimeter = format(Perimeter_list[1], ".2f")
      area = format(Area_list[1], ".2f")
      if area == 0:
        print("")
      else:
        print("Area = {}, perimeter = {}".format(area, perimeter))
        return area, perimeter
        break
        
    elif shape_selected == "rectangle":
      perimeter = format(Perimeter_list[0], ".2f")
      area = format(Area_list[0], ".2f")
      if area == 0:
        print("")
      else:
        print("Area = {}, perimeter = {}".format(area, perimeter))
        return area, perimeter
        break
    
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
        return area, perimeter
        break
    
    elif shape_selected == "parallelogram":
      perimeter = format(Perimeter_list[2], ".2f")
      area = format(Area_list[4], ".2f")
      if size_error == "true":
        print("The height of a parallelogram must be smaller than the length of one side")
      elif size_error == "zero":
        print("")
      else:
        print("Area = {}, perimeter = {}".format(area, perimeter))
        return area, perimeter
        break
    else:
      print("")



#lists
units = ["millimetres", "centimetres", "metres", "m", "cm", "mm"]
shape_list = ["square", "rectangle", "circle", "triangle", "parallelogram"]

#main routine
#asks the user if they want instructions
want_instructions = string_check("Would you like to see the instructions? y/n ")

if want_instructions == "yes" or want_instructions == "y":
  print("""Welcome to the area/perimeter tool!
To use this tool, follow these steps:
    - First, you must enter the shape you want to calculate
      the area and perimeter for
    - Next, you must enter the units you want
    - Finally, you must enter the required dimensions
The program will then display the area and perimeter""")
  print("")

#asks the user to select a shape
shape_selected = valid_shape("""Select the shape you would like to know the 
perimeter and area for: square, rectangle, triangle, circle or  parallelogram 
""")


#asks the user to select a unit
selected_unit = valid_unit("Pick a unit: metres, centimetres or millimetres: ")

print("")
# selects the correct equation for the shape 
equation_selector(shape_selected)

#calculates the area and perimeter
area_perimeter = calculator(shape_selected)

print("")
#returns the results to the user
print("The area of the {} is {}{} and the perimeter of the  {} is {}{}".format(shape_selected, area_perimeter[0], selected_unit, shape_selected,  area_perimeter[1], selected_unit))

