import socket
from concurrent.futures import ThreadPoolExecutor

# Function to scan a single port
def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # short timeout
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        sock.close()
    except Exception as e:
        pass  # handle silently for now

# Main function
def run_scanner():
    print("=== Port Scanner ===")
    target = input("Enter target IP or domain: ")
    print(f"Scanning {target} for open ports...\n")

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(1, 1025):  # scanning ports 1 to 1024
            executor.submit(scan_port, target, port)

if __name__ == "__main__":
    run_scanner()
