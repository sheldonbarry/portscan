import ipaddress
import socket

class ScanIP:

    default_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 
        445, 587, 993, 1433, 3306, 3389, 5900, 8080]

    def __init__(self, ip):
        self.ip = format(ipaddress.ip_address(ip))

    def scan_port(self, port, timeout=2):
        """scan a  single TCP port"""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            s.connect((self.ip, port))
            print ("Port %d: OPEN" % (port,))
            return True
        except (ConnectionRefusedError, socket.timeout) as e:
            return False
        finally:
            s.close()
            
    def scan(self, ports=default_ports):
        """scan a list of TCP ports"""
        open_ports = {}
        for port in ports:
            portscan = self.scan_port(port)
            open_ports[port] = portscan
        return open_ports

if __name__ == "__main__":

    target = ScanIP("192.168.0.1")

    # using default ports
    result = target.scan()
    
    print(result)