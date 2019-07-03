"""Scapy sniff ARP packets, must run as sudo!"""
from scapy.all import sniff
pkts = sniff(filter="arp", count=10)
print(pkts.summary())
