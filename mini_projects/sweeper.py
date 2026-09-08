import subprocess

# target1 = "192.168.29.92"
# target2 = "192.168.29.200"

def ip_generator(start, end):
    targets = []
    for i in range(start, end + 1):
        targets.append(f"192.168.29.{i}")
    return targets


def ip_responder(target):
    
    result = subprocess.run(["ping", "-c", "1", target], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{target} is reachable.")
    else:
        print(f"{target} is not reachable.")

ip = ip_generator(90, 100)

for i in ip:
    ip_responder(i)









    

