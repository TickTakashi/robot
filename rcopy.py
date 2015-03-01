#!/usr/bin/python
import os
import sys
from connect import *


def main(command_line):
  find_machines()
  ips = get_ips(ROBOT_MAC)
  args = ''

  for i in range(1, len(command_line)):
    args = args + command_line[i] + ' '

  if len(ips) == 0:
    print("WARNING! Robot IP Not Found. Is the robot on?\nTry Turning the robot OFF and ON again and waiting 5 minutes.\nIf you keep getting this error, tell Charles!")
  else:
    os.system('scp -r {0}pi@{1}:~/robotics'.format(args, ips[0]))


if __name__ == '__main__':
  main(sys.argv)

