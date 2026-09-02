from colorama import Fore,Style
import subprocess
while True:
    try:
        subprocess.run("cls", shell=True)
        edad = int(input("Edad: "))
        print(Fore.GREEN + "Edad registrada:",edad, Style.RESET_ALL)
        break
    except ValueError:
        print(Fore.RED + "Ingresa un valor numerico", Style.RESET_ALL)
        subprocess.run("pause", shell=True)

