cidr = int(input("enter cidr: " )) #user enter cidr
network_bit = 32-cidr #we find total network and host bit
total_ip = 2**network_bit # we find total useable ip addresses 

print(total_ip) # printing total ip address 

input("cn")
