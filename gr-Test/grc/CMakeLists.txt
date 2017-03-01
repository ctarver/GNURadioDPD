# Copyright 2011 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
install(FILES
    Test_test.xml
    Test_FreqShift.xml
    Test_Freq2.xml
    Test_SimpleFreqShift.xml
    Test_BiSimpleShift.xml
    Test_TotalFreqShift.xml
    Test_MemorylessPA.xml
    Test_MeanCorrelation.xml
    Test_W_LMS.xml
    Test_alpha.xml DESTINATION share/gnuradio/grc/blocks
)
