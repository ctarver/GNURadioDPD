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

class FreqShift(gr.sync_block):
    """
    docstring for block FreqShift
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="FreqShift",
            in_sig=None,
            out_sig=numpy.complex64)
        self.counter = 0 #Counter for the complex sinusoid


    def work(self, input_items, output_items):
        out = output_items[0]
        length = len(out)
        print length
        # <+signal processing here+>
        out[:] =  5
        return len(output_items[0])

