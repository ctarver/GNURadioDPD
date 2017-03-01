#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2016 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class BiSimpleShift(gr.sync_block):
    """
    docstring for block BiSimpleShift
    """
    def __init__(self, direction):
        gr.sync_block.__init__(self,
            name="BiSimpleShift",
            in_sig=None,
            out_sig=[numpy.complex64])
        self.direction = direction  #1 = positive. #-1 is negative
        self.ShiftAmount = 3000000 #Hardcode as 3MHz
        self.n = 0       #Start counter at 0
        self.SystemFS = 38400000 #Hardcode as 38.4 MHz


    def work(self, input_items, output_items):
        out = output_items[0]
        length = len(out)
        # <+signal processing here+>
        array = numpy.linspace(self.n,self.n+length-1,length)
        self.n = self.n+length     #Update counter for next time
        out[:] =  numpy.exp(self.direction*numpy.pi*1j*array*self.ShiftAmount/self.SystemFS)
        return len(output_items[0])

