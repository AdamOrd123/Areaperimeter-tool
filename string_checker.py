#ensures user enters a valid response (y/n)
def string_check(question):
  while True:
    error = "You must enter yes/y or no/n"
    try:
      response = input(question).lower().strip()
    except ValueError:
      print(error)
  
    if response == "yes" or response == "y":
      print("Display instructions here")
    elif response == "no" or response == "n":
      continue
    else:
      print(error)


# asks the user if they would like instructions
string_check("Would you like to see the instructions? y/n ")