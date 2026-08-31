from colorama import Fore,Style
import subprocess
while True:
    try:
        subprocess.run("cls", shell=True)
        edad = int(input("Edad: "))
        print("Edad registrada: ", edad)
        break
    except ValueError:
        print(Fore.RED + "Ingresa un valor numerico", Style.RESET_ALL)
        subprocess("pause")