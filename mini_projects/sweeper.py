import subprocess
from concurrent.futures import ThreadPoolExecutor,as_completed



def ip_generator(start, end):
    targets = []
    for i in range(start, end + 1):
        targets.append(f"192.168.29.{i}")
    return targets


def ip_responder(target):
    
    result = subprocess.run(["ping", "-c", "1", target], capture_output=True, text=True)
    if result.returncode == 0:
        for line in result.stdout.splitlines():
            if "time=" in line:
                rtt = line.split("time=")[1].split(" ")[0]
                return f"{target} |  reachable  | response time: {rtt} ms"
    else:
        return f"{target} |  not reachable | response time: N/A"

ip = ip_generator(1, 254)
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = []
    print("    IP       |   Status    | Response Time")
    for i in ip:
       future = executor.submit(ip_responder, i)
       futures.append(future)

    for future in as_completed(futures):
        result = future.result()
        print(result)









    

