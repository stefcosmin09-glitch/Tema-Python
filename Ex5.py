with open("logs.txt", "r") as file:
    for numar, line in enumerate(file):
        if "ERROR" in line:                                    
            print(f"Error gasit la linia {numar + 1}: {line.strip()}")  