import math
co = int(input("Digite o cateto oposto: "))
ca = int(input("Digite o cateto adjascente: "))
hip = ((ca*ca)+(co*co))
result = math.sqrt(hip)
print("A hipotenusa vale {} ".format(result))