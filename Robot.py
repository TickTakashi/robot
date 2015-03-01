import BrickPi

BrickPi.BrickPiSetup()

VERBOSE = False

NUM_INFO = 0
NUM_WARNING = 0

WARNING = '\033[93m' + '\033[1m' + 'WARN: \t'
END_MESSAGE = '\033[0m'
GREEN = '\033[92m'
INFO = 'INFO: \t'

LOG = ""

POWER_L = 1.0
POWER_R = 1.0

MOTORS = [BrickPi.PORT_B, BrickPi.PORT_C]


def set_logging(verbose):
  global VERBOSE
  VERBOSE += verbose


def print_info(message, is_green=False):
  global NUM_INFO
  global LOG
  NUM_INFO += 1 
  line = INFO + message
  if is_green:
    line = GREEN + line + END_MESSAGE
  LOG += line + '\n'

  if VERBOSE:
    print line


def print_warning(message):
  global NUM_WARNING
  global LOG
  NUM_WARNING += 1 
  line = WARNING + message + END_MESSAGE
  LOG += line + '\n'
  print line


def print_log():
  print LOG


def set_power_levels(left, right):
  global POWER_L
  global POWER_R

  if right > 1 or left > 1:
    print_warning("You can't set the power levels above 100%!")
  if left > 1:
    left = 1
  if right > 1:
    right = 1

  print_info('Setting Power Levels to {}%, {}%'.format(
    int(left * 100), int(right * 100)), True)

  POWER_L = left
  POWER_R = right


def turn_motors(left, right):
  print_info('Rotating Motors by {}, {} degrees'.format(left, right))
  BrickPi.motorRotateDegree([int(255 * POWER_L), int(255 * POWER_R)],
                            [left, right], MOTORS)
