#!/usr/bin/python3
from math import *

f = lambda x: (x+1) * sin(x)
ddf = lambda x: 2*cos(x) - (x + 1) * sin(x)
integral = lambda x: sin(x) - (x + 1) * cos(x)

a = 2
b = 5

rules = {
  1: [(0, 2)],
  2: [
    (sqrt(1 / 3), 1), 
    (-sqrt(1 / 3), 1)
  ],
  3: [
    (0, 8 / 9),
    (sqrt(3 / 5), 5 / 9),
    (-sqrt(3 / 5), 5 / 9)
  ],
  4: [
    ( sqrt(3 / 7 - 2 / 7 * sqrt(6 / 5)), (18 + sqrt(30)) / 36),
    (-sqrt(3 / 7 - 2 / 7 * sqrt(6 / 5)), (18 + sqrt(30)) / 36),
    ( sqrt(3 / 7 + 2 / 7 * sqrt(6 / 5)), (18 - sqrt(30)) / 36),
    (-sqrt(3 / 7 + 2 / 7 * sqrt(6 / 5)), (18 - sqrt(30)) / 36)
  ],
  5: [
    (0, 128 / 225),
    ( 1 / 3 * sqrt(5 - 2 * sqrt(10 / 7)), (322 + 13 * sqrt(70)) / 900),
    (-1 / 3 * sqrt(5 - 2 * sqrt(10 / 7)), (322 + 13 * sqrt(70)) / 900),
    ( 1 / 3 * sqrt(5 + 2 * sqrt(10 / 7)), (322 - 13 * sqrt(70)) / 900),
    (-1 / 3 * sqrt(5 + 2 * sqrt(10 / 7)), (322 - 13 * sqrt(70)) / 900)
  ]
}

def segs():
  accuracy = 1e-4;
  tmp_max = ddf(a);
  i = a
  while i <= b:
    tmp_max = max(tmp_max, abs(ddf(i)))
    i += accuracy
  mx = tmp_max
  residual_part = lambda arg: (b - a) ** 3 * mx / 12 / arg
  segments = 2
  while abs(residual_part(segments)) > accuracy:
    segments *= 2
  return segments

# simpson
def simpson():
  print('Simpson\'s method')
  segments = segs()
  print('Segments: ', segments)
  h = (b - a) / segments
  z = a
  w = a + h
  result = 0.
  while w < b:
    result += h / 6 * (f(z) + 4*f((z+w)/2) + f(w))
    z += h
    w += h

  real = integral(b) - integral(a)
  print('Calculated: ', result)
  print('Real: ', real)
  print('Diff: ', abs(real - result))
  print()
  print()


def gauss():
  print("Gauss quadrature method:");
  for n in rules:
    result = 0
    for x, w in rules[n]:
      result += w * f((b - a) / 2 * x + (a + b) / 2)
    result *= (b - a) / 2
    real = integral(b) - integral(a)
    print("N: ", n)
    print("Calculated: ", result)
    print("Real: ", real)
    print("Diff: ", abs(real - result))
    print()

simpson()
gauss()
