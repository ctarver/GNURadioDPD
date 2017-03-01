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

class MemorylessPA(gr.sync_block):
    """
    docstring for block MemorylessPA
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="MemorylessPA",
            in_sig=[numpy.complex64],
            out_sig=[numpy.complex64])
        self.beta_one =  numpy.complex(0.9512,-0.0946)
        self.beta_thr =  numpy.complex(0.0239,0.1632)
        self.beta_fiv =  numpy.complex(0.0082,-0.0727)
        self.beta_sev =  numpy.complex(-0.0016,0.0147)
        self.beta_nin =  numpy.complex(-0.0001,-0.0011)

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        Epsi_1 = in0
        Epsi_3 = in0 * numpy.power(numpy.absolute(in0),2)
        Epsi_5 = in0 * numpy.power(numpy.absolute(in0),4)
        Epsi_7 = in0 * numpy.power(numpy.absolute(in0),6)
        Epsi_9 = in0 * numpy.power(numpy.absolute(in0),8)

        out[:] = self.beta_one*Epsi_1 + self.beta_thr*Epsi_3 + self.beta_fiv*Epsi_5 + self.beta_sev*Epsi_7 + self.beta_nin*Epsi_9
        return len(output_items[0])

