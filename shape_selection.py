#checks the user has entered a string, and that the string is in the list of shapes
def valid_shape(question):
  error = ("Error, please enter square, rectangle, circle, triangle or  parallelogram")
  while True:
    try:
      shape_selected = input(question).strip().lower()
    except ValueError:
      print(error)

    if shape_selected in shape_list:
      print("You have selected:{}".format(shape_selected))
    else:
      print(error)


shape_list = ["square", "rectangle", "circle", "triangle", "parallelogram"]

#asks the user to select a shape from the list
valid_shape("""Select the shape you would like to know the 
perimeter and area for: square, rectangle, triangle, circle or parallelogram 
""")

