#asks user for the appropriate dimensions
def dimensions(question):

    
    try: 
      if shape_selected == "circle":
        r = int(input("What is the radius? "))
        
      elif shape_selected == "triangle":
        b = int(input("What is the length of the base? "))
        h = int(input("What is the height? "))
        a = int(input("What is the length of one of the sides? "))
        c = int(input("What is the length of the other side? "))
    
      elif shape_selected == "square":
        w = int(input("What is the width? "))
    
      elif shape_selected == "rectangle":
        w = int(input("What is the width? "))
        l = int(input("What is the length? "))
    
      else:
        b = int(input("What is the length of the base? "))
        h = int(input("What is the height? "))
        s = int(input("What is the length of one of the sides? "))
  
    except ValueError:
      print("You must enter a number")
    


while True:
  shape_selected = input("Shape: ")
  dimensions(shape_selected)