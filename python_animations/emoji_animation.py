import os, time

frames = [
    "🐰🥕",
    "🐰  🥕",
    "🐰   🥕",
    "🐰=>🥕",
    "🐰💥🥕",
    "🐰😋"
]

while True:
    for f in frames:
        os.system('cls')
        print(f.center(40))
        time.sleep(0.3)
