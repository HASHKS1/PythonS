from socket import *
import time


def timer(start_time):
    return str(time.time() - start_time)


def scan_ports(target_host, start_port, end_port):

    target_IP = gethostbyname(target_host)

    print(f"Start Scanning ports on {target_IP}...")

    for port in range(start_port,end_port+1):
        s = socket(AF_INET, SOCK_STREAM)

        # Set a connection timeout
        s.settimeout(1)

        conn = s.connect_ex((target_host,port))

        if conn == 0:
            print(f"Port {port} is open")
        
        s.close()

def main():
    target_hosts = input("Enter the hostname to be scanned: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    scan_ports(target_hosts, start_port, end_port)

if __name__ == '__main__':
    startTime = time.time()
    main()
    print("Time taken: "+timer(startTime))