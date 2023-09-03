#asks user for the appropriate dimensions
def dimensions(question):
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

while True:
  shape_selected = input("Shape: ")
  dimensions(shape_selected)