#checks that the user has entered a valid unit
def valid_unit(question):
  error = ("Error, you must enter a valid, metric unit (m, cm, mm)")
  while True:
    try:
      unit_selected = input(question)
    except ValueError:
      print(error)
    if unit_selected in units:
      print("You have selected: {}".format(unit_selected))
    else:
      print(error)


units = ["millimetres", "centimetres", "metres", "m", "cm", "mm"]

#asks the user to choose a unit
valid_unit("Pick a unit: metres, centimetres, millimetres: ")