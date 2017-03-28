from __future__ import division
import math

ratios = {
  'minorSecond': 16 / 15,               # 1.067
  'majorSecond': 9 / 8,                 # 1.125
  'minorThird': 6 / 5,                  # 1.2
  'majorThird': 5 / 4,                  # 1.25
  'perfectFourth': 4 / 3,               # 1.333
  'augmentedFourth': math.sqrt(2) / 1,  # 1.414
  'perfectFifth': 3 / 2,                # 1.5
  'minorSixth': 8 / 5,                  # 1.6
  'golden': 1 / 2 + math.sqrt(5) / 2,   # 1.618
  'majorSixth': 5 / 3,                  # 1.667
  'minorSeventh': 16 / 9,               # 1.778
  'majorSeventh': 15 / 8,               # 1.875
  'octave': 2 / 1,                      # 2
  'majorTenth': 5 / 2,                  # 2.5
  'majorEleventh': 8 / 3,               # 2.667
  'majorTwelfth': 3 / 1,                # 3
  'doubleOctave': 4 / 1,                # 4
}

settings = {
  'base': 14,
  'ratio': ratios['minorThird'],
  'steps': 8,
  'round': True,
}

for step in range(0, settings['steps']):
  px = settings['base'] * math.pow(settings['ratio'], step)
  if settings['round']:
    px = round(px)
  em = px / 16
  px = int(px) if px.is_integer() else px
  em = int(em) if em.is_integer() else em
  print '{}: {}px {}em'.format(step + 1, px, em)
