#calculates the area and perimeter
def calculator(question):
  Area_list = ["w*l", "w*w", "0.5b*h", "2*3.14*(r*r)", "s*b"]
  Perimeter_list = ["2w+2l", "4w", "2b+2s", "a+b+c", "2*3.14*r"]
  a = 0
  b = 0
  c = 0
  h = 0
  r = 0
  s = 0
  l = 0
  w = 0
  
  try: 
    if shape_selected == "circle":
      r = float(input("What is the radius? "))
      
        
    elif shape_selected == "triangle":
      b = float(input("What is the length of the base? "))
      h = float(input("What is the height? "))
      a = float(input("What is the length of one of the sides? "))
      c = float(input("What is the length of the other side? "))
      
    
    elif shape_selected == "square":
      w = float(input("What is the width? "))

    
    elif shape_selected == "rectangle":
      w = float(input("What is the width? "))
      l = float(input("What is the length? "))
      
    
    else:
      b = float(input("What is the length of the base? "))
      h = float(input("What is the height? "))
      s = float(input("What is the length of one of the sides? "))
      
  
  except ValueError:
    print("You must enter a number")
  

  Area_list = [w*l, w*w, 0.5*b*h, 2*3.14*(r*r), s*b]
  Perimeter_list = [(2*w)+(2*l), 4*w, (2*b)+(2*s), a+b+c, 2*3.14*r]
  if shape_selected == "circle":
    perimeter = format(Perimeter_list[4], ".2f")
    area = format(Area_list[3], ".2f")
    print("Area = {}, perimeter = {}".format(area, perimeter))
      
  elif shape_selected == "square":
    perimeter = format(Perimeter_list[1], ".2f")
    area = format(Area_list[1], ".2f")
    print("Area = {}, perimeter = {}".format(area, perimeter))
      
  elif shape_selected == "rectangle":
    perimeter = format(Perimeter_list[0], ".2f")
    area = format(Area_list[0], ".2f")
    print("Area = {}, perimeter = {}".format(area, perimeter))
  
  elif shape_selected == "triangle":
    perimeter = format(Perimeter_list[3], ".2f")
    area = format(Area_list[2], ".2f")
    print("Area = {}, perimeter = {}".format(area, perimeter))
  
  elif shape_selected == "parallelogram":
    perimeter = format(Perimeter_list[2], ".2f")
    area = format(Area_list[4], ".2f")
    print("Area = {}, perimeter = {}".format(area, perimeter))
  else:
    print("")

      
while True:    
  shape_selected = input("Shape: ")
  calculator(shape_selected)