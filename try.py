user_name = input("What's your name: ")
sex = input("What's your sex, male(m) or female(f): ").lower()
while True:
  if user_name == "" or sex == "":
    print("Error, one of the requirements or both left blank")
    break
  elif sex == "male" or sex == "m":
    greeting = input(f'Hello Mr.{user_name} ').lower()
  elif sex == "female" or sex == "f":
    greeting = input(f'Hello Miss.{user_name} ').lower()

  if "bye" in greeting or "gtg" in greeting or "au revoir"in greeting or "cya" in greeting:
    print("Have a good day")
    break
  else:
    continue
