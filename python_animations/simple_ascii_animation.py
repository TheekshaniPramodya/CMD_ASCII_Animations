import os
import time
from colorama import Fore, Style, init

init(autoreset=True)

frames = [
    Fore.CYAN + r"""
      (\_/)
      ( •_•)
    />🍪   GIMME COOKIE!
    """,

    Fore.YELLOW + r"""
      (\_/)
      ( •_•)
    🍪<\    YUMMY!
    """,

    Fore.RED + r"""
      (\_/)
      ( •_•)
     /   \   NO COOKIE?
    """,

    Fore.GREEN + r"""
      (\_/)
      ( ^_^)
     /🍪\   YAY!!
    """
]


while True:
    for frame in frames:
        os.system('cls')  # clear screen (Windows)
        print(frame)
        time.sleep(0.5)


