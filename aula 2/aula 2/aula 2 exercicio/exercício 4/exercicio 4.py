import math
base= float(input("digite a base do retângulo:"))
altura = float (input("digite a altura do retângulo:"))

area = base * altura
perimetro = 2 * (base+altura)
diagonal = math.sqrt(base**2 + altura**2)

print(f"área = {area:.2f} - perímetro = {perimetro:.2f} - diagonal = {diagonal:.2f}")