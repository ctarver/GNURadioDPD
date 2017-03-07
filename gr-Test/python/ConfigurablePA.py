#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
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

class ConfigurablePA(gr.sync_block):
    """
    docstring for block ConfigurablePA
    """
    def __init__(self, beta1,beta3,beta5,beta7,beta9):
        gr.sync_block.__init__(self,
            name="ConfigurablePA",
            in_sig=[numpy.complex64],
            out_sig=[numpy.complex64])
        self.beta1 = beta1
        self.beta3 = beta3
        self.beta5 = beta5
        self.beta7 = beta7
        self.beta9 = beta9

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        # <+signal processing here+>
        Epsi_1 = in0
        Epsi_3 = in0 * numpy.power(numpy.absolute(in0),2) 
        Epsi_5 = in0 * numpy.power(numpy.absolute(in0),4)  
        Epsi_7 = in0 * numpy.power(numpy.absolute(in0),6) 
        Epsi_9 = in0 * numpy.power(numpy.absolute(in0),8) 

        out[:] = self.beta1*Epsi_1 + self.beta3*Epsi_3 + self.beta5*Epsi_5 + self.beta7*Epsi_7 + self.beta9*Epsi_9
        return len(output_items[0])

    def set_beta1(self,beta1):
        self.beta1 = beta1
    def set_beta3(self,beta3):
        self.beta3 = beta3
    def set_beta5(self,beta5):
        self.beta5 = beta5
    def set_beta7(self,beta7):
        self.beta7 = beta7
    def set_beta9(self,beta9):
        self.beta9 = beta9
