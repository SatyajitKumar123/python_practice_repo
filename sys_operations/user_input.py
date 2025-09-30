import sys

## Check if enough arguments are provided
if len(sys.argv) < 4:
    print("Usage: python main.py name age address")
    sys.exit(1)

name = sys.argv[1]
age = int(sys.argv[2])
address = sys.argv[3]

info = {"name": name, "age": age, "address": address}

for key, value in info.items():
    print(f"{key}: {value}")
