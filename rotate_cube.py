#!/usr/bin/env python
import load_cube as cr
import numpy as np
from scipy import ndimage 

b=cr.CUBE()
b.read_cube('si_plus.cube')
b.data=ndimage.rotate(b.data,45,axes=(0,2),mode='wrap')
#b.data=ndimage.shift(b.data,[0,0,75],mode='wrap')
c=open('test.cube','w')
b.dump(c)
c.close()


