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

valid_unit("Pick a unit: metres, centimetres, millimetres: ")