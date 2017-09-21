import sys
# -*- coding: utf-8 -*-
weight = input('Weight: ')
height = input('Height: ')
height = height/100
indexBody = float(weight) / (height*height)
print('Your Weight index' + ' ' + str(indexBody))


