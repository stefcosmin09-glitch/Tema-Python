import subprocess
import time

process_name = "my-script.sh"

while True:
    process_check = subprocess.run(["pgrep", "-f", process_name],
                                    capture_output=True, text=True)
    
    if process_check.returncode != 0:
        print("Procesul nu ruleaza. Pornind procesul...")
        subprocess.run([f"./{process_name}"])
    
    time.sleep(3)