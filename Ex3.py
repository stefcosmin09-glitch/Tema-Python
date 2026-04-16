import sys
import os

if len(sys.argv) < 3:
    raise Exception("Nu au fost pasati suficienti parametri!")

utilizator = sys.argv[1]
varsta_utilizator = int(sys.argv[2])

print(f"Au fost pasati {len(sys.argv) - 1} parametri")

if varsta_utilizator > 18:
    os.makedirs(utilizator, exist_ok=True)
    print(f"Director creat pentru {utilizator}")