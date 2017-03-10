#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Mar 10 10:02:34 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import Test
import sip
import sys


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.beta3_real = beta3_real = 0.02
        self.beta3_imag = beta3_imag = 0.01
        self.systemfs = systemfs = 38400000
        self.samp_rate = samp_rate = 38400000
        self.mu = mu = 0.0005
        self.f3 = f3 = 2.1
        self.f2 = f2 = 0
        self.f1 = f1 = -3
        self.dpd13_real = dpd13_real = -beta3_real
        self.dpd13_imag = dpd13_imag = -beta3_imag
        self.beta7_real = beta7_real = 0
        self.beta7_imag = beta7_imag = 0
        self.beta5_real = beta5_real = 0
        self.beta5_imag = beta5_imag = 0
        self.beta1_real = beta1_real = 1
        self.beta1_imag = beta1_imag = 0
        self.alpha_real = alpha_real = 0
        self.alpha_imag = alpha_imag = 0
        self.a3 = a3 = 1
        self.a2 = a2 = 1
        self.a1 = a1 = 1
        self.ScalingForPA = ScalingForPA = 5.485960502027843
        self.LoopDelay = LoopDelay = 51
        self.DPD32_3 = DPD32_3 = 0
        self.DPD31_3 = DPD31_3 = 0
        self.DPD23_3 = DPD23_3 = 0
        self.DPD21_3 = DPD21_3 = 0
        self.DPD13_3 = DPD13_3 = 0
        self.DPD12_3 = DPD12_3 = 0

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, "Carrier Positions and Amplitudes")
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, "PA Paramters")
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, "DPD")
        self.top_grid_layout.addWidget(self.tab, 1, 0, 3,4)
        self._beta3_real_range = Range(-0.5, 0.5, 0.001, 0.02, 200)
        self._beta3_real_win = RangeWidget(self._beta3_real_range, self.set_beta3_real, "beta3_real", "counter_slider", float)
        self.tab_grid_layout_1.addWidget(self._beta3_real_win,  0, 1, 1, 1)
        self._beta3_imag_range = Range(-1, 1, 0.001, 0.01, 200)
        self._beta3_imag_win = RangeWidget(self._beta3_imag_range, self.set_beta3_imag, "beta3_imag", "counter_slider", float)
        self.tab_grid_layout_1.addWidget(self._beta3_imag_win,  1, 1, 1, 1)
        self._f3_range = Range(-20, 20, 0.1, 2.1, 200)
        self._f3_win = RangeWidget(self._f3_range, self.set_f3, "f3", "counter_slider", float)
        self.tab_grid_layout_0.addWidget(self._f3_win,  0, 2, 1, 1)
        self._f2_range = Range(-20, 20, 0.1, 0, 200)
        self._f2_win = RangeWidget(self._f2_range, self.set_f2, "f2", "counter_slider", float)
        self.tab_grid_layout_0.addWidget(self._f2_win,  0, 1, 1, 1)
        self._f1_range = Range(-20, 20, 0.1, -3, 200)
        self._f1_win = RangeWidget(self._f1_range, self.set_f1, "f1", "counter_slider", float)
        self.tab_grid_layout_0.addWidget(self._f1_win,  0, 0, 1, 1)
        self._dpd13_real_range = Range(-0.1, 0.1, 0.0001, -beta3_real, 200)
        self._dpd13_real_win = RangeWidget(self._dpd13_real_range, self.set_dpd13_real, "dpd13_real", "counter_slider", float)
        self.tab_grid_layout_2.addWidget(self._dpd13_real_win,  0, 0, 1, 1)
        self._dpd13_imag_range = Range(-0.1, 0.1, 0.0001, -beta3_imag, 200)
        self._dpd13_imag_win = RangeWidget(self._dpd13_imag_range, self.set_dpd13_imag, "dpd13_imag", "counter_slider", float)
        self.tab_grid_layout_2.addWidget(self._dpd13_imag_win,  1, 0, 1, 1)
        self._beta7_real_range = Range(-0.1, 0.1, 0.0001, 0, 200)
        self._beta7_real_win = RangeWidget(self._beta7_real_range, self.set_beta7_real, "beta7_real", "counter_slider", float)
        self.tab_grid_layout_1.addWidget(self._beta7_real_win,  0, 3, 1, 1)
        self._beta7_imag_range = Range(-0.1, 0.1, 0.0001, 0, 200)
        self._beta7_imag_win = RangeWidget(self._beta7_imag_range, self.set_beta7_imag, "beta7_imag", "counter_slider", float)
        self.tab_grid_layout_1.addWidget(self._beta7_imag_win,  1, 3, 1, 1)
        self._beta5_real_range = Range(-0.1, 0.1, 0.0001, 0, 200)
        self._beta5_real_win = RangeWidget(self._beta5_real_range, self.set_beta5_real, "beta5_real", "counter_slider", float)
        self.tab_grid_layout_1.addWidget(self._beta5_real_win,  0, 2, 1, 1)
        self._beta5_imag_range = Range(-1, 1, 0.0001, 0, 200)
        self._beta5_imag_win = RangeWidget(self._beta5_imag_range, self.set_beta5_imag, "beta5_imag", "counter_slider", float)
        self.tab_grid_layout_1.addWidget(self._beta5_imag_win,  1, 2, 1, 1)
        self._beta1_real_range = Range(-1, 1, 0.01, 1, 200)
        self._beta1_real_win = RangeWidget(self._beta1_real_range, self.set_beta1_real, "beta1_real", "counter_slider", float)
        self.tab_grid_layout_1.addWidget(self._beta1_real_win,  0, 0, 1, 1)
        self._beta1_imag_range = Range(-1, 1, 0.01, 0, 200)
        self._beta1_imag_win = RangeWidget(self._beta1_imag_range, self.set_beta1_imag, "beta1_imag", "counter_slider", float)
        self.tab_grid_layout_1.addWidget(self._beta1_imag_win,  1, 0, 1, 1)
        self._a3_range = Range(0, 2, 0.01, 1, 200)
        self._a3_win = RangeWidget(self._a3_range, self.set_a3, "a3", "counter_slider", float)
        self.tab_grid_layout_0.addWidget(self._a3_win,  1, 2, 1, 1)
        self._a2_range = Range(0, 2, 0.01, 1, 200)
        self._a2_win = RangeWidget(self._a2_range, self.set_a2, "a2", "counter_slider", float)
        self.tab_grid_layout_0.addWidget(self._a2_win,  1, 1, 1, 1)
        self._a1_range = Range(0, 2, 0.01, 1, 200)
        self._a1_win = RangeWidget(self._a1_range, self.set_a1, "a1", "counter_slider", float)
        self.tab_grid_layout_0.addWidget(self._a1_win,  1, 0, 1, 1)
        _DPD32_3_check_box = Qt.QCheckBox("Carrier 2,3 IM3-")
        self._DPD32_3_choices = {True: 1, False: 0}
        self._DPD32_3_choices_inv = dict((v,k) for k,v in self._DPD32_3_choices.iteritems())
        self._DPD32_3_callback = lambda i: Qt.QMetaObject.invokeMethod(_DPD32_3_check_box, "setChecked", Qt.Q_ARG("bool", self._DPD32_3_choices_inv[i]))
        self._DPD32_3_callback(self.DPD32_3)
        _DPD32_3_check_box.stateChanged.connect(lambda i: self.set_DPD32_3(self._DPD32_3_choices[bool(i)]))
        self.tab_grid_layout_2.addWidget(_DPD32_3_check_box,  1, 2, 1, 1)
        _DPD31_3_check_box = Qt.QCheckBox("Carrier 1,3 IM3-")
        self._DPD31_3_choices = {True: 1, False: 0}
        self._DPD31_3_choices_inv = dict((v,k) for k,v in self._DPD31_3_choices.iteritems())
        self._DPD31_3_callback = lambda i: Qt.QMetaObject.invokeMethod(_DPD31_3_check_box, "setChecked", Qt.Q_ARG("bool", self._DPD31_3_choices_inv[i]))
        self._DPD31_3_callback(self.DPD31_3)
        _DPD31_3_check_box.stateChanged.connect(lambda i: self.set_DPD31_3(self._DPD31_3_choices[bool(i)]))
        self.tab_grid_layout_2.addWidget(_DPD31_3_check_box,  1, 1, 1, 1)
        _DPD23_3_check_box = Qt.QCheckBox("Carrier 2,3 IM3+")
        self._DPD23_3_choices = {True: 1, False: 0}
        self._DPD23_3_choices_inv = dict((v,k) for k,v in self._DPD23_3_choices.iteritems())
        self._DPD23_3_callback = lambda i: Qt.QMetaObject.invokeMethod(_DPD23_3_check_box, "setChecked", Qt.Q_ARG("bool", self._DPD23_3_choices_inv[i]))
        self._DPD23_3_callback(self.DPD23_3)
        _DPD23_3_check_box.stateChanged.connect(lambda i: self.set_DPD23_3(self._DPD23_3_choices[bool(i)]))
        self.tab_grid_layout_2.addWidget(_DPD23_3_check_box,  0, 2, 1, 1)
        _DPD21_3_check_box = Qt.QCheckBox("Carrier 1,2 IM3-")
        self._DPD21_3_choices = {True: 1, False: 0}
        self._DPD21_3_choices_inv = dict((v,k) for k,v in self._DPD21_3_choices.iteritems())
        self._DPD21_3_callback = lambda i: Qt.QMetaObject.invokeMethod(_DPD21_3_check_box, "setChecked", Qt.Q_ARG("bool", self._DPD21_3_choices_inv[i]))
        self._DPD21_3_callback(self.DPD21_3)
        _DPD21_3_check_box.stateChanged.connect(lambda i: self.set_DPD21_3(self._DPD21_3_choices[bool(i)]))
        self.tab_grid_layout_2.addWidget(_DPD21_3_check_box,  1, 3, 1, 1)
        _DPD13_3_check_box = Qt.QCheckBox("Carrier 1,3 IM3+")
        self._DPD13_3_choices = {True: 1, False: 0}
        self._DPD13_3_choices_inv = dict((v,k) for k,v in self._DPD13_3_choices.iteritems())
        self._DPD13_3_callback = lambda i: Qt.QMetaObject.invokeMethod(_DPD13_3_check_box, "setChecked", Qt.Q_ARG("bool", self._DPD13_3_choices_inv[i]))
        self._DPD13_3_callback(self.DPD13_3)
        _DPD13_3_check_box.stateChanged.connect(lambda i: self.set_DPD13_3(self._DPD13_3_choices[bool(i)]))
        self.tab_grid_layout_2.addWidget(_DPD13_3_check_box,  0, 1, 1, 1)
        _DPD12_3_check_box = Qt.QCheckBox("Carrier 1,2 IM3+")
        self._DPD12_3_choices = {True: 1, False: 0}
        self._DPD12_3_choices_inv = dict((v,k) for k,v in self._DPD12_3_choices.iteritems())
        self._DPD12_3_callback = lambda i: Qt.QMetaObject.invokeMethod(_DPD12_3_check_box, "setChecked", Qt.Q_ARG("bool", self._DPD12_3_choices_inv[i]))
        self._DPD12_3_callback(self.DPD12_3)
        _DPD12_3_check_box.stateChanged.connect(lambda i: self.set_DPD12_3(self._DPD12_3_choices[bool(i)]))
        self.tab_grid_layout_2.addWidget(_DPD12_3_check_box,  0, 3, 1, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_HAMMING, #wintype
        	0, #fc
        	samp_rate, #bw
        	"IM3+ DPD Spectrum", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-100, -15)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["Without DPD", "With DPD", "With DPD", "WithoutDPD", "",
                  "", "", "", "", ""]
        widths = [2, 2, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["red", "dark green", "green", "red", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,4)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_xx_4_0_0_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_4_0_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_4_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_4_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_4_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_4 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_3_0_1_0_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_3_0_1_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_3_0_1_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_3_0_1_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_3_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_3_0_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_3_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_3_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_3_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_2_0_0_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_2_0_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_2_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_2_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_2_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_2 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1_0_0_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1_0_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_2_2_0 = blocks.multiply_const_vcc((a1, ))
        self.blocks_multiply_const_vxx_2_1 = blocks.multiply_const_vcc((a2, ))
        self.blocks_multiply_const_vxx_2_0 = blocks.multiply_const_vcc((a3, ))
        self.blocks_multiply_const_vxx_0_1_0_0_0_0_0 = blocks.multiply_const_vcc((ScalingForPA*DPD21_3, ))
        self.blocks_multiply_const_vxx_0_1_0_0_0_0 = blocks.multiply_const_vcc((ScalingForPA*DPD32_3, ))
        self.blocks_multiply_const_vxx_0_1_0_0_0 = blocks.multiply_const_vcc((ScalingForPA*DPD31_3, ))
        self.blocks_multiply_const_vxx_0_1_0_0 = blocks.multiply_const_vcc((ScalingForPA*DPD12_3, ))
        self.blocks_multiply_const_vxx_0_1_0 = blocks.multiply_const_vcc((ScalingForPA*DPD23_3, ))
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vcc((ScalingForPA*DPD13_3, ))
        self.blocks_multiply_const_vxx_0_0_0_0_0_0_0 = blocks.multiply_const_vcc((ScalingForPA*DPD21_3, ))
        self.blocks_multiply_const_vxx_0_0_0_0_0_0 = blocks.multiply_const_vcc((ScalingForPA*DPD32_3, ))
        self.blocks_multiply_const_vxx_0_0_0_0_0 = blocks.multiply_const_vcc((ScalingForPA*DPD31_3, ))
        self.blocks_multiply_const_vxx_0_0_0_0 = blocks.multiply_const_vcc((ScalingForPA*DPD12_3, ))
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vcc((ScalingForPA*DPD23_3, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vcc((ScalingForPA*DPD13_3, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((ScalingForPA, ))
        self.blocks_float_to_complex_1_0_0_0_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_1_0_0_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_1_0_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_1_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_1_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0_1_0 = blocks.file_source(gr.sizeof_float*1, "/home/chance/Documents/Git/GNURadioDPD/InputData/CC3_real.bin", True)
        self.blocks_file_source_0_1 = blocks.file_source(gr.sizeof_float*1, "/home/chance/Documents/Git/GNURadioDPD/InputData/CC2_real.bin", True)
        self.blocks_file_source_0_0_1 = blocks.file_source(gr.sizeof_float*1, "/home/chance/Documents/Git/GNURadioDPD/InputData/CC3_imag.bin", True)
        self.blocks_file_source_0_0_0 = blocks.file_source(gr.sizeof_float*1, "/home/chance/Documents/Git/GNURadioDPD/InputData/CC1_imag.bin", True)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_float*1, "/home/chance/Documents/Git/GNURadioDPD/InputData/CC1_imag.bin", True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, "/home/chance/Documents/Git/GNURadioDPD/InputData/CC1_real.bin", True)
        self.blocks_conjugate_cc_0_0_0_0_0_0 = blocks.conjugate_cc()
        self.blocks_conjugate_cc_0_0_0_0_0 = blocks.conjugate_cc()
        self.blocks_conjugate_cc_0_0_0_0 = blocks.conjugate_cc()
        self.blocks_conjugate_cc_0_0_0 = blocks.conjugate_cc()
        self.blocks_conjugate_cc_0_0 = blocks.conjugate_cc()
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_const_source_x_0_1_0_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, dpd13_real)
        self.analog_const_source_x_0_1_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, dpd13_real)
        self.analog_const_source_x_0_1_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, dpd13_real)
        self.analog_const_source_x_0_1_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, dpd13_real)
        self.analog_const_source_x_0_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, dpd13_real)
        self.analog_const_source_x_0_0_0_0_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, dpd13_imag)
        self.analog_const_source_x_0_0_0_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, dpd13_imag)
        self.analog_const_source_x_0_0_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, dpd13_imag)
        self.analog_const_source_x_0_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, dpd13_imag)
        self.analog_const_source_x_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, dpd13_imag)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, dpd13_imag)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, dpd13_real)
        self.Test_TotalFreqShift_0_1 = Test.TotalFreqShift(f1*1000000, samp_rate, 1)
        self.Test_TotalFreqShift_0_0_0_0_0_0_0_0_0 = Test.TotalFreqShift((2*f1-f2)*1000000, systemfs, 1)
        self.Test_TotalFreqShift_0_0_0_0_0_0_0_0 = Test.TotalFreqShift((2*f2-f3)*1000000, systemfs, 1)
        self.Test_TotalFreqShift_0_0_0_0_0_0_0 = Test.TotalFreqShift((2*f1-f3)*1000000, systemfs, 1)
        self.Test_TotalFreqShift_0_0_0_0_0_0 = Test.TotalFreqShift((2*f2-f1)*1000000, systemfs, 1)
        self.Test_TotalFreqShift_0_0_0_0_0 = Test.TotalFreqShift((2*f3-f2)*1000000, systemfs, 1)
        self.Test_TotalFreqShift_0_0_0_0 = Test.TotalFreqShift((2*f3-f1)*1000000, systemfs, 1)
        self.Test_TotalFreqShift_0_0 = Test.TotalFreqShift(f2*1000000, samp_rate, 1)
        self.Test_TotalFreqShift_0 = Test.TotalFreqShift(f3*1000000, samp_rate, 1)
        self.Test_ConfigurablePA_0_0 = Test.ConfigurablePA(complex(beta1_real,beta1_imag), complex(beta3_real,beta3_imag), complex(beta5_real,beta5_imag), complex(beta7_real,beta7_imag), 0)
        self.Test_ConfigurablePA_0 = Test.ConfigurablePA(complex(beta1_real,beta1_imag), complex(beta3_real,beta3_imag), complex(beta5_real,beta5_imag), complex(beta7_real,beta7_imag), 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.Test_ConfigurablePA_0, 0), (self.qtgui_freq_sink_x_0, 1))    
        self.connect((self.Test_ConfigurablePA_0_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.Test_TotalFreqShift_0, 0), (self.blocks_multiply_xx_3_0_0, 1))    
        self.connect((self.Test_TotalFreqShift_0_0, 0), (self.blocks_multiply_xx_3_0_0_0, 1))    
        self.connect((self.Test_TotalFreqShift_0_0_0_0, 0), (self.blocks_multiply_xx_3_0, 1))    
        self.connect((self.Test_TotalFreqShift_0_0_0_0_0, 0), (self.blocks_multiply_xx_3_0_1, 1))    
        self.connect((self.Test_TotalFreqShift_0_0_0_0_0_0, 0), (self.blocks_multiply_xx_3_0_1_0, 1))    
        self.connect((self.Test_TotalFreqShift_0_0_0_0_0_0_0, 0), (self.blocks_multiply_xx_3_0_1_0_0, 1))    
        self.connect((self.Test_TotalFreqShift_0_0_0_0_0_0_0_0, 0), (self.blocks_multiply_xx_3_0_1_0_0_0, 1))    
        self.connect((self.Test_TotalFreqShift_0_0_0_0_0_0_0_0_0, 0), (self.blocks_multiply_xx_3_0_1_0_0_0_0, 1))    
        self.connect((self.Test_TotalFreqShift_0_1, 0), (self.blocks_multiply_xx_3_0_0_1, 1))    
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_1, 0))    
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_float_to_complex_1, 1))    
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.blocks_float_to_complex_1_0, 1))    
        self.connect((self.analog_const_source_x_0_0_0_0, 0), (self.blocks_float_to_complex_1_0_0, 1))    
        self.connect((self.analog_const_source_x_0_0_0_0_0, 0), (self.blocks_float_to_complex_1_0_0_0, 1))    
        self.connect((self.analog_const_source_x_0_0_0_0_0_0, 0), (self.blocks_float_to_complex_1_0_0_0_0, 1))    
        self.connect((self.analog_const_source_x_0_0_0_0_0_0_0, 0), (self.blocks_float_to_complex_1_0_0_0_0_0, 1))    
        self.connect((self.analog_const_source_x_0_1, 0), (self.blocks_float_to_complex_1_0, 0))    
        self.connect((self.analog_const_source_x_0_1_0, 0), (self.blocks_float_to_complex_1_0_0, 0))    
        self.connect((self.analog_const_source_x_0_1_0_0, 0), (self.blocks_float_to_complex_1_0_0_0, 0))    
        self.connect((self.analog_const_source_x_0_1_0_0_0, 0), (self.blocks_float_to_complex_1_0_0_0_0, 0))    
        self.connect((self.analog_const_source_x_0_1_0_0_0_0, 0), (self.blocks_float_to_complex_1_0_0_0_0_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_add_xx_0_0, 0), (self.Test_ConfigurablePA_0, 0))    
        self.connect((self.blocks_conjugate_cc_0, 0), (self.blocks_multiply_xx_2, 1))    
        self.connect((self.blocks_conjugate_cc_0_0, 0), (self.blocks_multiply_xx_2_0, 1))    
        self.connect((self.blocks_conjugate_cc_0_0_0, 0), (self.blocks_multiply_xx_2_0_0, 1))    
        self.connect((self.blocks_conjugate_cc_0_0_0_0, 0), (self.blocks_multiply_xx_2_0_0_0, 1))    
        self.connect((self.blocks_conjugate_cc_0_0_0_0_0, 0), (self.blocks_multiply_xx_2_0_0_0_0, 1))    
        self.connect((self.blocks_conjugate_cc_0_0_0_0_0_0, 0), (self.blocks_multiply_xx_2_0_0_0_0_0, 1))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.blocks_file_source_0_0_0, 0), (self.blocks_float_to_complex_0_0, 1))    
        self.connect((self.blocks_file_source_0_0_1, 0), (self.blocks_float_to_complex_0_0_0, 1))    
        self.connect((self.blocks_file_source_0_1, 0), (self.blocks_float_to_complex_0_0, 0))    
        self.connect((self.blocks_file_source_0_1_0, 0), (self.blocks_float_to_complex_0_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_const_vxx_0_0_0_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_const_vxx_0_0_0_0_0_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_const_vxx_0_1, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_const_vxx_0_1_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_3_0_0_1, 0))    
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0_0_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.blocks_multiply_const_vxx_0_1_0, 0))    
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.blocks_multiply_const_vxx_0_1_0_0_0_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.blocks_multiply_xx_3_0_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0_0_0, 0), (self.blocks_multiply_const_vxx_0_1_0_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0_0_0, 0), (self.blocks_multiply_const_vxx_0_1_0_0_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0_0_0, 0), (self.blocks_multiply_xx_3_0_0, 0))    
        self.connect((self.blocks_float_to_complex_1, 0), (self.blocks_multiply_xx_4, 0))    
        self.connect((self.blocks_float_to_complex_1_0, 0), (self.blocks_multiply_xx_4_0, 0))    
        self.connect((self.blocks_float_to_complex_1_0_0, 0), (self.blocks_multiply_xx_4_0_0, 0))    
        self.connect((self.blocks_float_to_complex_1_0_0_0, 0), (self.blocks_multiply_xx_4_0_0_0, 0))    
        self.connect((self.blocks_float_to_complex_1_0_0_0_0, 0), (self.blocks_multiply_xx_4_0_0_0_0, 0))    
        self.connect((self.blocks_float_to_complex_1_0_0_0_0_0, 0), (self.blocks_multiply_xx_4_0_0_0_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_multiply_xx_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_multiply_xx_1, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_multiply_xx_1_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_multiply_xx_1_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0, 0), (self.blocks_multiply_xx_1_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0, 0), (self.blocks_multiply_xx_1_0_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0_0, 0), (self.blocks_multiply_xx_1_0_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0_0, 0), (self.blocks_multiply_xx_1_0_0_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0_0_0, 0), (self.blocks_multiply_xx_1_0_0_0_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0_0_0, 0), (self.blocks_multiply_xx_1_0_0_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0_0_0_0, 0), (self.blocks_multiply_xx_1_0_0_0_0_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0_0_0_0, 0), (self.blocks_multiply_xx_1_0_0_0_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_conjugate_cc_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_1_0, 0), (self.blocks_conjugate_cc_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_1_0_0, 0), (self.blocks_conjugate_cc_0_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_1_0_0_0, 0), (self.blocks_conjugate_cc_0_0_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_1_0_0_0_0, 0), (self.blocks_conjugate_cc_0_0_0_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_1_0_0_0_0_0, 0), (self.blocks_conjugate_cc_0_0_0_0_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_2_0, 0), (self.blocks_add_xx_0, 2))    
        self.connect((self.blocks_multiply_const_vxx_2_1, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_2_2_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_multiply_xx_2, 0))    
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.blocks_multiply_xx_2_0, 0))    
        self.connect((self.blocks_multiply_xx_1_0_0, 0), (self.blocks_multiply_xx_2_0_0, 0))    
        self.connect((self.blocks_multiply_xx_1_0_0_0, 0), (self.blocks_multiply_xx_2_0_0_0, 0))    
        self.connect((self.blocks_multiply_xx_1_0_0_0_0, 0), (self.blocks_multiply_xx_2_0_0_0_0, 0))    
        self.connect((self.blocks_multiply_xx_1_0_0_0_0_0, 0), (self.blocks_multiply_xx_2_0_0_0_0_0, 0))    
        self.connect((self.blocks_multiply_xx_2, 0), (self.blocks_multiply_xx_4, 1))    
        self.connect((self.blocks_multiply_xx_2_0, 0), (self.blocks_multiply_xx_4_0, 1))    
        self.connect((self.blocks_multiply_xx_2_0_0, 0), (self.blocks_multiply_xx_4_0_0, 1))    
        self.connect((self.blocks_multiply_xx_2_0_0_0, 0), (self.blocks_multiply_xx_4_0_0_0, 1))    
        self.connect((self.blocks_multiply_xx_2_0_0_0_0, 0), (self.blocks_multiply_xx_4_0_0_0_0, 1))    
        self.connect((self.blocks_multiply_xx_2_0_0_0_0_0, 0), (self.blocks_multiply_xx_4_0_0_0_0_0, 1))    
        self.connect((self.blocks_multiply_xx_3_0, 0), (self.blocks_add_xx_0_0, 1))    
        self.connect((self.blocks_multiply_xx_3_0_0, 0), (self.blocks_multiply_const_vxx_2_0, 0))    
        self.connect((self.blocks_multiply_xx_3_0_0_0, 0), (self.blocks_multiply_const_vxx_2_1, 0))    
        self.connect((self.blocks_multiply_xx_3_0_0_1, 0), (self.blocks_multiply_const_vxx_2_2_0, 0))    
        self.connect((self.blocks_multiply_xx_3_0_1, 0), (self.blocks_add_xx_0_0, 3))    
        self.connect((self.blocks_multiply_xx_3_0_1_0, 0), (self.blocks_add_xx_0_0, 2))    
        self.connect((self.blocks_multiply_xx_3_0_1_0_0, 0), (self.blocks_add_xx_0_0, 4))    
        self.connect((self.blocks_multiply_xx_3_0_1_0_0_0, 0), (self.blocks_add_xx_0_0, 5))    
        self.connect((self.blocks_multiply_xx_3_0_1_0_0_0_0, 0), (self.blocks_add_xx_0_0, 6))    
        self.connect((self.blocks_multiply_xx_4, 0), (self.blocks_multiply_xx_3_0, 0))    
        self.connect((self.blocks_multiply_xx_4_0, 0), (self.blocks_multiply_xx_3_0_1, 0))    
        self.connect((self.blocks_multiply_xx_4_0_0, 0), (self.blocks_multiply_xx_3_0_1_0, 0))    
        self.connect((self.blocks_multiply_xx_4_0_0_0, 0), (self.blocks_multiply_xx_3_0_1_0_0, 0))    
        self.connect((self.blocks_multiply_xx_4_0_0_0_0, 0), (self.blocks_multiply_xx_3_0_1_0_0_0, 0))    
        self.connect((self.blocks_multiply_xx_4_0_0_0_0_0, 0), (self.blocks_multiply_xx_3_0_1_0_0_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.Test_ConfigurablePA_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_add_xx_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_beta3_real(self):
        return self.beta3_real

    def set_beta3_real(self, beta3_real):
        self.beta3_real = beta3_real
        self.set_dpd13_real(-self.beta3_real)
        self.Test_ConfigurablePA_0. set_beta3(complex(self.beta3_real,self.beta3_imag))
        self.Test_ConfigurablePA_0_0. set_beta3(complex(self.beta3_real,self.beta3_imag))

    def get_beta3_imag(self):
        return self.beta3_imag

    def set_beta3_imag(self, beta3_imag):
        self.beta3_imag = beta3_imag
        self.set_dpd13_imag(-self.beta3_imag)
        self.Test_ConfigurablePA_0. set_beta3(complex(self.beta3_real,self.beta3_imag))
        self.Test_ConfigurablePA_0_0. set_beta3(complex(self.beta3_real,self.beta3_imag))

    def get_systemfs(self):
        return self.systemfs

    def set_systemfs(self, systemfs):
        self.systemfs = systemfs

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_mu(self):
        return self.mu

    def set_mu(self, mu):
        self.mu = mu

    def get_f3(self):
        return self.f3

    def set_f3(self, f3):
        self.f3 = f3
        self.Test_TotalFreqShift_0. set_shift_freq(self.f3*1000000) 
        self.Test_TotalFreqShift_0_0_0_0. set_shift_freq((2*self.f3-self.f1)*1000000) 
        self.Test_TotalFreqShift_0_0_0_0_0. set_shift_freq((2*self.f3-self.f2)*1000000) 
        self.Test_TotalFreqShift_0_0_0_0_0_0_0. set_shift_freq((2*self.f1-self.f3)*1000000) 
        self.Test_TotalFreqShift_0_0_0_0_0_0_0_0. set_shift_freq((2*self.f2-self.f3)*1000000) 

    def get_f2(self):
        return self.f2

    def set_f2(self, f2):
        self.f2 = f2
        self.Test_TotalFreqShift_0_0. set_shift_freq(self.f2*1000000) 
        self.Test_TotalFreqShift_0_0_0_0_0. set_shift_freq((2*self.f3-self.f2)*1000000) 
        self.Test_TotalFreqShift_0_0_0_0_0_0. set_shift_freq((2*self.f2-self.f1)*1000000) 
        self.Test_TotalFreqShift_0_0_0_0_0_0_0_0. set_shift_freq((2*self.f2-self.f3)*1000000) 
        self.Test_TotalFreqShift_0_0_0_0_0_0_0_0_0. set_shift_freq((2*self.f1-self.f2)*1000000) 

    def get_f1(self):
        return self.f1

    def set_f1(self, f1):
        self.f1 = f1
        self.Test_TotalFreqShift_0_0_0_0. set_shift_freq((2*self.f3-self.f1)*1000000) 
        self.Test_TotalFreqShift_0_0_0_0_0_0. set_shift_freq((2*self.f2-self.f1)*1000000) 
        self.Test_TotalFreqShift_0_0_0_0_0_0_0. set_shift_freq((2*self.f1-self.f3)*1000000) 
        self.Test_TotalFreqShift_0_1. set_shift_freq(self.f1*1000000) 
        self.Test_TotalFreqShift_0_0_0_0_0_0_0_0_0. set_shift_freq((2*self.f1-self.f2)*1000000) 

    def get_dpd13_real(self):
        return self.dpd13_real

    def set_dpd13_real(self, dpd13_real):
        self.dpd13_real = dpd13_real
        self.analog_const_source_x_0.set_offset(self.dpd13_real)
        self.analog_const_source_x_0_1.set_offset(self.dpd13_real)
        self.analog_const_source_x_0_1_0.set_offset(self.dpd13_real)
        self.analog_const_source_x_0_1_0_0.set_offset(self.dpd13_real)
        self.analog_const_source_x_0_1_0_0_0.set_offset(self.dpd13_real)
        self.analog_const_source_x_0_1_0_0_0_0.set_offset(self.dpd13_real)

    def get_dpd13_imag(self):
        return self.dpd13_imag

    def set_dpd13_imag(self, dpd13_imag):
        self.dpd13_imag = dpd13_imag
        self.analog_const_source_x_0_0.set_offset(self.dpd13_imag)
        self.analog_const_source_x_0_0_0.set_offset(self.dpd13_imag)
        self.analog_const_source_x_0_0_0_0.set_offset(self.dpd13_imag)
        self.analog_const_source_x_0_0_0_0_0.set_offset(self.dpd13_imag)
        self.analog_const_source_x_0_0_0_0_0_0.set_offset(self.dpd13_imag)
        self.analog_const_source_x_0_0_0_0_0_0_0.set_offset(self.dpd13_imag)

    def get_beta7_real(self):
        return self.beta7_real

    def set_beta7_real(self, beta7_real):
        self.beta7_real = beta7_real
        self.Test_ConfigurablePA_0. set_beta7(complex(self.beta7_real,self.beta7_imag))
        self.Test_ConfigurablePA_0_0. set_beta7(complex(self.beta7_real,self.beta7_imag))

    def get_beta7_imag(self):
        return self.beta7_imag

    def set_beta7_imag(self, beta7_imag):
        self.beta7_imag = beta7_imag
        self.Test_ConfigurablePA_0. set_beta7(complex(self.beta7_real,self.beta7_imag))
        self.Test_ConfigurablePA_0_0. set_beta7(complex(self.beta7_real,self.beta7_imag))

    def get_beta5_real(self):
        return self.beta5_real

    def set_beta5_real(self, beta5_real):
        self.beta5_real = beta5_real
        self.Test_ConfigurablePA_0. set_beta5(complex(self.beta5_real,self.beta5_imag))
        self.Test_ConfigurablePA_0_0. set_beta5(complex(self.beta5_real,self.beta5_imag))

    def get_beta5_imag(self):
        return self.beta5_imag

    def set_beta5_imag(self, beta5_imag):
        self.beta5_imag = beta5_imag
        self.Test_ConfigurablePA_0. set_beta5(complex(self.beta5_real,self.beta5_imag))
        self.Test_ConfigurablePA_0_0. set_beta5(complex(self.beta5_real,self.beta5_imag))

    def get_beta1_real(self):
        return self.beta1_real

    def set_beta1_real(self, beta1_real):
        self.beta1_real = beta1_real
        self.Test_ConfigurablePA_0. set_beta1(complex(self.beta1_real,self.beta1_imag))
        self.Test_ConfigurablePA_0_0. set_beta1(complex(self.beta1_real,self.beta1_imag))

    def get_beta1_imag(self):
        return self.beta1_imag

    def set_beta1_imag(self, beta1_imag):
        self.beta1_imag = beta1_imag
        self.Test_ConfigurablePA_0. set_beta1(complex(self.beta1_real,self.beta1_imag))
        self.Test_ConfigurablePA_0_0. set_beta1(complex(self.beta1_real,self.beta1_imag))

    def get_alpha_real(self):
        return self.alpha_real

    def set_alpha_real(self, alpha_real):
        self.alpha_real = alpha_real

    def get_alpha_imag(self):
        return self.alpha_imag

    def set_alpha_imag(self, alpha_imag):
        self.alpha_imag = alpha_imag

    def get_a3(self):
        return self.a3

    def set_a3(self, a3):
        self.a3 = a3
        self.blocks_multiply_const_vxx_2_0.set_k((self.a3, ))

    def get_a2(self):
        return self.a2

    def set_a2(self, a2):
        self.a2 = a2
        self.blocks_multiply_const_vxx_2_1.set_k((self.a2, ))

    def get_a1(self):
        return self.a1

    def set_a1(self, a1):
        self.a1 = a1
        self.blocks_multiply_const_vxx_2_2_0.set_k((self.a1, ))

    def get_ScalingForPA(self):
        return self.ScalingForPA

    def set_ScalingForPA(self, ScalingForPA):
        self.ScalingForPA = ScalingForPA
        self.blocks_multiply_const_vxx_0.set_k((self.ScalingForPA, ))
        self.blocks_multiply_const_vxx_0_0.set_k((self.ScalingForPA*self.DPD13_3, ))
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.ScalingForPA*self.DPD23_3, ))
        self.blocks_multiply_const_vxx_0_0_0_0.set_k((self.ScalingForPA*self.DPD12_3, ))
        self.blocks_multiply_const_vxx_0_0_0_0_0.set_k((self.ScalingForPA*self.DPD31_3, ))
        self.blocks_multiply_const_vxx_0_1.set_k((self.ScalingForPA*self.DPD13_3, ))
        self.blocks_multiply_const_vxx_0_1_0.set_k((self.ScalingForPA*self.DPD23_3, ))
        self.blocks_multiply_const_vxx_0_1_0_0.set_k((self.ScalingForPA*self.DPD12_3, ))
        self.blocks_multiply_const_vxx_0_1_0_0_0.set_k((self.ScalingForPA*self.DPD31_3, ))
        self.blocks_multiply_const_vxx_0_1_0_0_0_0.set_k((self.ScalingForPA*self.DPD32_3, ))
        self.blocks_multiply_const_vxx_0_0_0_0_0_0.set_k((self.ScalingForPA*self.DPD32_3, ))
        self.blocks_multiply_const_vxx_0_1_0_0_0_0_0.set_k((self.ScalingForPA*self.DPD21_3, ))
        self.blocks_multiply_const_vxx_0_0_0_0_0_0_0.set_k((self.ScalingForPA*self.DPD21_3, ))

    def get_LoopDelay(self):
        return self.LoopDelay

    def set_LoopDelay(self, LoopDelay):
        self.LoopDelay = LoopDelay

    def get_DPD32_3(self):
        return self.DPD32_3

    def set_DPD32_3(self, DPD32_3):
        self.DPD32_3 = DPD32_3
        self.blocks_multiply_const_vxx_0_1_0_0_0_0.set_k((self.ScalingForPA*self.DPD32_3, ))
        self.blocks_multiply_const_vxx_0_0_0_0_0_0.set_k((self.ScalingForPA*self.DPD32_3, ))
        self._DPD32_3_callback(self.DPD32_3)

    def get_DPD31_3(self):
        return self.DPD31_3

    def set_DPD31_3(self, DPD31_3):
        self.DPD31_3 = DPD31_3
        self._DPD31_3_callback(self.DPD31_3)
        self.blocks_multiply_const_vxx_0_0_0_0_0.set_k((self.ScalingForPA*self.DPD31_3, ))
        self.blocks_multiply_const_vxx_0_1_0_0_0.set_k((self.ScalingForPA*self.DPD31_3, ))

    def get_DPD23_3(self):
        return self.DPD23_3

    def set_DPD23_3(self, DPD23_3):
        self.DPD23_3 = DPD23_3
        self._DPD23_3_callback(self.DPD23_3)
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.ScalingForPA*self.DPD23_3, ))
        self.blocks_multiply_const_vxx_0_1_0.set_k((self.ScalingForPA*self.DPD23_3, ))

    def get_DPD21_3(self):
        return self.DPD21_3

    def set_DPD21_3(self, DPD21_3):
        self.DPD21_3 = DPD21_3
        self.blocks_multiply_const_vxx_0_1_0_0_0_0_0.set_k((self.ScalingForPA*self.DPD21_3, ))
        self.blocks_multiply_const_vxx_0_0_0_0_0_0_0.set_k((self.ScalingForPA*self.DPD21_3, ))
        self._DPD21_3_callback(self.DPD21_3)

    def get_DPD13_3(self):
        return self.DPD13_3

    def set_DPD13_3(self, DPD13_3):
        self.DPD13_3 = DPD13_3
        self._DPD13_3_callback(self.DPD13_3)
        self.blocks_multiply_const_vxx_0_0.set_k((self.ScalingForPA*self.DPD13_3, ))
        self.blocks_multiply_const_vxx_0_1.set_k((self.ScalingForPA*self.DPD13_3, ))

    def get_DPD12_3(self):
        return self.DPD12_3

    def set_DPD12_3(self, DPD12_3):
        self.DPD12_3 = DPD12_3
        self._DPD12_3_callback(self.DPD12_3)
        self.blocks_multiply_const_vxx_0_0_0_0.set_k((self.ScalingForPA*self.DPD12_3, ))
        self.blocks_multiply_const_vxx_0_1_0_0.set_k((self.ScalingForPA*self.DPD12_3, ))


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
