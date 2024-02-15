import ipaddress

ip = '192.168.0.1'
network = '192.168.0.0/24'

address = ipaddress.ip_address(ip)
network_range = ipaddress.ip_network(network, strict=False)

print(address + 257)
for ip in network_range:
    print(ip)
