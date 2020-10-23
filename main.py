#basic menu; prompts reader to select a math calculator
print("")
print("Select Operation.")
print("")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponent")
print("6.Square Root")
print("7.Sine")
print("8.Cosine")
print("9.Tangent")
print("")

choice = input("Select Operation: ")
#importing the different files for the calculator
if choice == "1":
  from Scientific_Calculator import Addition
  Addition.Sum()

if choice == "2":
  from Scientific_Calculator import Subtraction
  Subtraction.Subraction()

if choice == "3":
  from Scientific_Calculator import Multiplication
  Multiplication.multiply()

if choice == "4":
  from Scientific_Calculator import Division
  Division.Divide()

if choice == "5":
  from Scientific_Calculator import Exponent
  Exponent.Exponent()

if choice == "6":
  from Scientific_Calculator import sqrt
  sqrt.sqrt()

if choice == "7":
  from Scientific_Calculator import Sine
  Sine.sine()

if choice == "8":
  from Scientific_Calculator import Cosine
  Cosine.cosine()

if choice == "9":
  from Scientific_Calculator import Tangent
  Tangent.tangent()