#!/usr/bin/env python

# renaming scapy.all as scary for ease
import scapy.all as scapy


def scan(ip):
    scapy.arping(ip)


scan('192.168.149.18')