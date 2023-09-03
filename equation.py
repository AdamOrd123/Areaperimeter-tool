#selects the correct equation for the shape
def equation_selector(question):
  Area_list = ["w*l", "w*w", "0.5b*h", "2*3.14*(r*r)", "h*b"]
  Perimeter_list = ["2w+2l", "4w", "2b+2s", "a+b+c", "2*3.14*r"]
  
  
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

while True:
  
  shape_selected = input("Shape: ").strip().lower()
  equation_selector(shape_selected)

