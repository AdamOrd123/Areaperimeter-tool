def range_checker(question):
  if shape_selected == "triangle":
    number = a - c:
    if number <= 0:
      lowest_number = a
    else:
      lowest_number = c

    if lowest_number <= h:
      print("The height of a triangle must be smaller than the length of the smallest side")
    

  if shape_selected == "parallelogram":
    if s <= h:
      print("The height of a parallelogram must be smaller than the length of one side")


shape_selected = input("Shape: ")
range_checker(shape_selected)
  
    