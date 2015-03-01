#!/usr/bin/python

import os
import re
import sys

ROBOT_MAC = 'e8:4e:06:1f:fe:6f'
CATHERINE_MAC = '00:13:ef:ca:04:28'
CHARLES_MAC = '00:13:ef:c0:11:b6'
VM_MAC = '00:0c:29:83:24:69'
slow = False

def get_ips(mac):
  arp = os.popen('arp -a').read()
  arp_line = os.popen('echo \'{0}\' | grep \'{1}\''.format(arp, mac)).read()
  return re.findall( r'[0-9]+(?:\.[0-9]+){3}', arp_line)


def find_machines():
  print("Couldn't find machine, scanning... (This could take a while.)")
  if slow:
    os.popen("nmap -PE 192.168.0.0-255")
  else:
    os.popen("nmap -sP 192.168.0.0-255")


def main():
  MAC = ROBOT_MAC

  if 'robot' in sys.argv :
    MAC = ROBOT_MAC
  if 'charles' in sys.argv:
    MAC = CHARLES_MAC
  if 'catherine' in sys.argv:
    MAC = CATHERINE_MAC

  global slow
  slow = 'slow' in sys.argv or '-slow' in sys.argv

  ip = get_ips(MAC)

  if len(ip) == 0:
    find_machines()

  ip = get_ips(MAC)

  if len(ip) == 0:
    print("WARNING! IP Not Found. If you get this error, tell Charles!")
  else:
    os.system('ssh pi@' + ip[0])

if __name__ == '__main__':
  main()

