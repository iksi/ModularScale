from __future__ import division
import math

ratios = {
  'doubleOctave': 4 / 1,                # 4
  'majorTwelfth': 3 / 1,                # 3
  'majorEleventh': 8 / 3,               # 2.667
  'majorTenth': 5 / 2,                  # 2.5
  'octave': 2 / 1,                      # 2
  'majorSeventh': 15 / 8,               # 1.875
  'minorSeventh': 16 / 9,               # 1.778
  'majorSixth': 5 / 3,                  # 1.667
  'golden': 1 / 2 + math.sqrt(5) / 2,   # 1.618
  'minorSixth': 8 / 5,                  # 1.6
  'fifth': 3 / 2,                       # 1.5
  'augmentedFourth': math.sqrt(2) / 1,  # 1.414
  'fourth': 4 / 3,                      # 1.333
  'majorThird': 5 / 4,                  # 1.25
  'minorThird': 6 / 5,                  # 1.2
  'majorSecond': 9 / 8,                 # 1.125
  'minorSecond': 16 / 15,               # 1.067
}

base = 16
ratio = ratios['majorThird']
steps = 7
rem = True

for step in range(0, steps):
  number = base * math.pow(ratio, step)
  number = int(number)
  if rem:
    number = number / 16
    if number.is_integer():
      number = int(number)
  print '{}: {}'.format(step + 1, number)
