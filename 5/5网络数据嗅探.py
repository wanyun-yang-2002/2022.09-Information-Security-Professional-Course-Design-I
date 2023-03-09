from scapy.all import *


# def printPacket(packet):
#     if packet.haslayer('HTTP'):
#         print("_________________________________")
#         print(packet['TCP'].sport)
#         print(packet['TCP'].dport)
#         print('laiyuan_addr:', packet['IP'].src, 'sport', packet['TCP'].sport, 'mudi_addr', packet['IP'].dst, 'deport',
#               packet['TCP'].dport)
#         print(packet.payload.payload.payload.show())


sniff(iface='WLAN', count=0, prn=lambda x : x.sprintf("{IP:%IP.src%:%IP.sport%-> %IP.dst%:%IP.dport%} IP报文长度%IP.len% "
                                                    "抓取时间 %IP.time%"))
