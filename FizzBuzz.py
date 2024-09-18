def es_multiplo(numero,multiplo):
  return numero % multiplo == 0

for i in range(1,101):
  output = ""
  if es_multiplo(i, 3):
    output += "Fizz"
  if es_multiplo(i, 5):
    output += "Buzz"

  print(output or i)