import optparse
from socket import *
from threading import Thread

def socketScan(host, port):
    """Scan a single port on the given host."""
    try:
        # Create a TCP socket
        socket_connect = socket(AF_INET, SOCK_STREAM)
        socket_connect.settimeout(5)
        
        # Attempt to connect to the target host and port
        result = socket_connect.connect((host, port))
        print(f'[+] {port}/tcp open')
    
    except Exception as exception:
        print(f'[-] {port}/tcp closed')
        print(f'[-] Reason: {str(exception)}')
    
    finally:
        # Close the socket
        socket_connect.close()

def portScanning(host, ports):
    """Scan multiple ports on the given host."""
    try:
        # Resolve the host name to an IP address
        ip = gethostbyname(host)
        print(f'[+] Scan Results for: {ip}')
    
    except:
        print(f"[-] Cannot resolve '{host}': Unknown host")
        return
    
    # Start a thread for each port to scan
    for port in ports:
        t = Thread(target=socketScan, args=(ip, int(port)))
        t.start()

# Example usage
if __name__ == "__main__":
    # Parse command-line arguments (if needed)
    parser = optparse.OptionParser('usage %prog -H <target host> -p <target port(s)>')
    parser.add_option('-H', dest='targetHost', type='string', help='specify target host')
    parser.add_option('-p', dest='targetPorts', type='string', help='specify target port(s), separated by commas')
    (options, args) = parser.parse_args()

    targetHost = options.targetHost
    targetPorts = str(options.targetPorts).split(',')

    if targetHost == None or targetPorts[0] == None:
        print(parser.usage)
        exit(0)
    
    portScanning(targetHost, targetPorts)
