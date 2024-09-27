import socket
import re
import common_ports

ports_and_services = common_ports.ports_and_services

def get_open_ports(target, port_range, verbose=False):
    open_ports = []
    x = range(port_range[0], port_range[1] + 1)
    
    try:
        host = socket.gethostbyname(target)
    except:
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", target):
            return "Error: Invalid IP address"
        else:
            return "Error: Invalid hostname"
    
    try: 
        host_name = socket.gethostbyaddr(target)[0]
    except:
        host_name = False
        
    for i in x:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, i))
        if result == 0:
            open_ports.append(i)
        sock.close()
    
    if not open_ports:  # Check if the list of open ports is empty
        return "No open ports found"
    
    if verbose:
        host_string = f'{host_name} ({host})' if host_name else host
        header_string = f'Open ports for {host_string}\nPORT     SERVICE'
        ports_string = ''
        for port in open_ports:
            ports_string += f'\n{str(port).ljust(9)}{ports_and_services.get(port, "Unknown")}'
        return header_string + ports_string
    else:
        return open_ports


# Function to prompt the user for inputs
def user_interaction():
    # Asking the user for the target (IP address or URL)
    target = input("Enter the target (IP address or domain): ")
    
    # Asking the user for the port range
    port_start = int(input("Enter the start of the port range: "))
    port_end = int(input("Enter the end of the port range: "))
    
    # Asking the user if they want verbose output (y/n)
    verbose_choice = input("Do you want a detailed verbose output? (y/n): ").lower()
    verbose = True if verbose_choice == 'y' else False
    
    # Running the port scan with the provided inputs
    result = get_open_ports(target, [port_start, port_end], verbose)
    
    # Display the result
    print(result)


# Run the user interaction function
if __name__ == "__main__":
    user_interaction()
