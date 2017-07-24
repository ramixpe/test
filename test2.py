#!/usr/bin/python

a = int(raw_input('Please insert the fisrt number : '))
b = int(raw_input('Please enter the seconf number : '))
c = raw_input('What operation you want to excute + - x / ?: ')

if c == '+':
    print int(a+b)
  elif '-':
    print int(a-b)
#elif '*':
#    print int(a*b)
#elif '/':
#    print int(a/b)
else:
    print "your choices are limited to ' + - x /' "
