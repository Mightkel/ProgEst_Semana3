try:
    edad = int(input("Edad: "))
    print("Edad registrada: ", edad)
except ValueError:
    print("Ingresa un valor numerico")
