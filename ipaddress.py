import math

def AND(ip, mask):
    return [x & y for x,y in zip(ip, mask)]


def printIP(ip):
    print(f"{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}")


def ADD(ip, number):
    stringip = ip[0]*(2**24)+ip[1]*(2**16)+ip[2]*(2**8)+ip[3]
    stringip += number
    return [(stringip >> 24) & 0xFF, (stringip >> 16) & 0xFF, (stringip >> 8) & 0xFF, (stringip) & 0xFF]

ip = input("Enter the ip address : ")
bytes = [int(x) for x in ip.split(".")]
if bytes[0] < 128:
    ipclass = 'A'
elif bytes[0] < 192:
    ipclass = 'B'
elif bytes[0] < 224:
    ipclass = 'C'
elif bytes[0] < 240:
    ipclass = 'D'
else:
    ipclass = 'E'

print("Class =", ipclass)
if ipclass == 'A':
    ipbits = 24
    mask=[255, 0, 0, 0]
elif ipclass == 'B':
    ipbits = 16
    mask=[255, 255, 0, 0]
elif ipclass == 'C':
    ipbits = 8
    mask=[255, 255, 255, 0]

print("Mask : ", end='')
printIP(mask)
netID = AND(bytes, mask)
print("Net ID : ", end='')
printIP(netID)
print("Number of possible IP addresses =", 2**ipbits)

n = int(input("Enter number of subnets (power of 2): "))
print("Number of bits in subnet ID : ", int(math.log2(n)))
subnet_count = 2**ipbits // n
print("IP addresses in each subnet : ", subnet_count)
subnetID = netID
for i in range(n):
    print()
    print("Subnet", i)
    print("Subnet ID : ", end='')
    printIP(subnetID)
    print("From : ", end='')
    printIP(ADD(subnetID, 1))
    print("To : ", end='')
    printIP(ADD(subnetID, subnet_count-2))
    print("Broadcast add : ", end='')
    printIP(ADD(subnetID, subnet_count-1))
    subnetID = ADD(subnetID, subnet_count)

stringmask = mask[0]*(2**24)+mask[1]*(2**16)+mask[2]*(2**8)+mask[3]
stringmask += (2**(int(math.log2(n)))-1) << (ipbits-int(math.log2(n)))  # Add required number of 1 bits to the mask
print("Subnet mask : ", end='')
printIP([(stringmask >> 24) & 0xFF, (stringmask >> 16) & 0xFF, (stringmask >> 8) & 0xFF, (stringmask) & 0xFF])
