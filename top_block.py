#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Mar  8 11:57:46 2017
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
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import Test
import sip
import sys
import threading
import time


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
        self.variable_function_probe_0 = variable_function_probe_0 = 0
        self.systemfs = systemfs = 38400000
        self.samp_rate = samp_rate = 38400000
        self.mu = mu = 0.0005
        self.f3 = f3 = 4
        self.f2 = f2 = 0
        self.f1 = f1 = -4
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
        self.probe_signal = blocks.probe_signal_c()
        self._f3_range = Range(-20, 20, 0.1, 4, 200)
        self._f3_win = RangeWidget(self._f3_range, self.set_f3, "f3", "counter_slider", float)
        self.tab_grid_layout_0.addWidget(self._f3_win,  0, 2, 1, 1)
        self._f2_range = Range(-20, 20, 0.1, 0, 200)
        self._f2_win = RangeWidget(self._f2_range, self.set_f2, "f2", "counter_slider", float)
        self.tab_grid_layout_0.addWidget(self._f2_win,  0, 1, 1, 1)
        self._f1_range = Range(-20, 20, 0.1, -4, 200)
        self._f1_win = RangeWidget(self._f1_range, self.set_f1, "f1", "counter_slider", float)
        self.tab_grid_layout_0.addWidget(self._f1_win,  0, 0, 1, 1)
        self._dpd13_real_range = Range(-0.1, 0.1, 0.0001, -beta3_real, 200)
        self._dpd13_real_win = RangeWidget(self._dpd13_real_range, self.set_dpd13_real, "dpd13_real", "counter_slider", float)
        self.tab_grid_layout_2.addWidget(self._dpd13_real_win,  0, 3, 1, 1)
        self._dpd13_imag_range = Range(-0.1, 0.1, 0.0001, -beta3_imag, 200)
        self._dpd13_imag_win = RangeWidget(self._dpd13_imag_range, self.set_dpd13_imag, "dpd13_imag", "counter_slider", float)
        self.tab_grid_layout_2.addWidget(self._dpd13_imag_win,  1, 3, 1, 1)
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
        def _variable_function_probe_0_probe():
            while True:
                val = self.probe_signal.level()
                try:
                    self.set_variable_function_probe_0(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (38400000/10000))
        _variable_function_probe_0_thread = threading.Thread(target=_variable_function_probe_0_probe)
        _variable_function_probe_0_thread.daemon = True
        _variable_function_probe_0_thread.start()
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
        
        labels = ["Original", "PostPA", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
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
        self.fir_filter_xxx_1 = filter.fir_filter_ccc(4, (1, ))
        self.fir_filter_xxx_1.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(1, ([-0.00074031,-0.00033842,-0.00030921,-0.00018513,4.4823e-05,0.00037567,0.00078312,0.0012225,0.0016318,0.0019373,0.0020639,0.0019464,0.0015426,0.00084479,-0.00011139,-0.0012438,-0.0024268,-0.0035019,-0.0042951,-0.0046403,-0.0044043,-0.0035124,-0.0019696,0.00012618,0.0025822,0.0051217,0.0074091,0.0090859,0.0098156,0.0093326,0.0074905,0.0042989,-5.3308e-05,-0.0051921,-0.010575,-0.015536,-0.019337,-0.021248,-0.020626,-0.016993,-0.010107,-6.0453e-06,0.012968,0.028176,0.044727,0.061543,0.077452,0.091293,0.10202,0.10882,0.11114,0.10882,0.10202,0.091293,0.077452,0.061543,0.044727,0.028176,0.012968,-6.0453e-06,-0.010107,-0.016993,-0.020626,-0.021248,-0.019337,-0.015536,-0.010575,-0.0051921,-5.3308e-05,0.0042989,0.0074905,0.0093326,0.0098156,0.0090859,0.0074091,0.0051217,0.0025822,0.00012618,-0.0019696,-0.0035124,-0.0044043,-0.0046403,-0.0042951,-0.0035019,-0.0024268,-0.0012438,-0.00011139,0.00084479,0.0015426,0.0019464,0.0020639,0.0019373,0.0016318,0.0012225,0.00078312,0.00037567,4.4823e-05,-0.00018513,-0.00030921,-0.00033842,-0.00074031]))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_xx_4_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_4 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_3_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_3_0_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_3_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_3_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_3_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_3 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_2_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_2 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_2_1 = blocks.multiply_const_vcc((a2, ))
        self.blocks_multiply_const_vxx_2_0 = blocks.multiply_const_vcc((a3, ))
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vcc((a1, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((mu, ))
        self.blocks_multiply_const_vxx_0_1_0 = blocks.multiply_const_vcc((ScalingForPA, ))
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vcc((ScalingForPA, ))
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vcc((ScalingForPA, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vcc((ScalingForPA, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((ScalingForPA, ))
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
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, LoopDelay)
        self.blocks_conjugate_cc_2 = blocks.conjugate_cc()
        self.blocks_conjugate_cc_1 = blocks.conjugate_cc()
        self.blocks_conjugate_cc_0_0 = blocks.conjugate_cc()
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_const_source_x_0_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, dpd13_real)
        self.analog_const_source_x_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, dpd13_imag)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, dpd13_imag)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, dpd13_real)
        self.Test_W_LMS_0 = Test.W_LMS()
        self.Test_TotalFreqShift_0_1 = Test.TotalFreqShift(f1*1000000, samp_rate, 1)
        self.Test_TotalFreqShift_0_0_0_0_0 = Test.TotalFreqShift(int(2*f1-f3)*1000000, systemfs, 1)
        self.Test_TotalFreqShift_0_0_0_0 = Test.TotalFreqShift(int(2*f3-f1)*1000000, systemfs, 1)
        self.Test_TotalFreqShift_0_0_0 = Test.TotalFreqShift(int((f3-f1)*1000000), systemfs, -1)
        self.Test_TotalFreqShift_0_0 = Test.TotalFreqShift(f2*1000000, samp_rate, 1)
        self.Test_TotalFreqShift_0 = Test.TotalFreqShift(f3*1000000, samp_rate, 1)
        self.Test_MeanCorrelation_0 = Test.MeanCorrelation()
        self.Test_ConfigurablePA_0 = Test.ConfigurablePA(complex(beta1_real,beta1_imag), complex(beta3_real,beta3_imag), complex(beta5_real,beta5_imag), complex(beta7_real,beta7_imag), 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.Test_ConfigurablePA_0, 0), (self.blocks_multiply_xx_3, 0))    
        self.connect((self.Test_ConfigurablePA_0, 0), (self.qtgui_freq_sink_x_0, 1))    
        self.connect((self.Test_MeanCorrelation_0, 0), (self.fir_filter_xxx_1, 0))    
        self.connect((self.Test_TotalFreqShift_0, 0), (self.blocks_multiply_xx_3_0_0, 1))    
        self.connect((self.Test_TotalFreqShift_0_0, 0), (self.blocks_multiply_xx_3_0_0_0, 1))    
        self.connect((self.Test_TotalFreqShift_0_0_0, 0), (self.blocks_multiply_xx_3, 1))    
        self.connect((self.Test_TotalFreqShift_0_0_0_0, 0), (self.blocks_multiply_xx_3_0, 1))    
        self.connect((self.Test_TotalFreqShift_0_0_0_0_0, 0), (self.blocks_multiply_xx_3_0_1, 1))    
        self.connect((self.Test_TotalFreqShift_0_1, 0), (self.blocks_multiply_xx_3_0_0_1, 1))    
        self.connect((self.Test_W_LMS_0, 0), (self.blocks_conjugate_cc_2, 0))    
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_1, 0))    
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_float_to_complex_1, 1))    
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.blocks_float_to_complex_1_0, 1))    
        self.connect((self.analog_const_source_x_0_1, 0), (self.blocks_float_to_complex_1_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_add_xx_0_0, 0), (self.Test_ConfigurablePA_0, 0))    
        self.connect((self.blocks_add_xx_0_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.blocks_conjugate_cc_0, 0), (self.blocks_multiply_xx_2, 1))    
        self.connect((self.blocks_conjugate_cc_0_0, 0), (self.blocks_multiply_xx_2_0, 1))    
        self.connect((self.blocks_conjugate_cc_1, 0), (self.Test_MeanCorrelation_0, 0))    
        self.connect((self.blocks_conjugate_cc_2, 0), (self.probe_signal, 0))    
        self.connect((self.blocks_delay_0, 0), (self.Test_MeanCorrelation_0, 1))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.blocks_file_source_0_0_0, 0), (self.blocks_float_to_complex_0_0, 1))    
        self.connect((self.blocks_file_source_0_0_1, 0), (self.blocks_float_to_complex_0_0_0, 1))    
        self.connect((self.blocks_file_source_0_1, 0), (self.blocks_float_to_complex_0_0, 0))    
        self.connect((self.blocks_file_source_0_1_0, 0), (self.blocks_float_to_complex_0_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_const_vxx_0_1, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_3_0_0_1, 0))    
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.blocks_multiply_xx_3_0_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0_0_0, 0), (self.blocks_multiply_const_vxx_0_1_0, 0))    
        self.connect((self.blocks_float_to_complex_0_0_0, 0), (self.blocks_multiply_xx_3_0_0, 0))    
        self.connect((self.blocks_float_to_complex_1, 0), (self.blocks_multiply_xx_4, 0))    
        self.connect((self.blocks_float_to_complex_1_0, 0), (self.blocks_multiply_xx_4_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_multiply_xx_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_multiply_xx_1, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_multiply_xx_1_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_multiply_xx_1_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_conjugate_cc_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_1_0, 0), (self.blocks_conjugate_cc_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.Test_W_LMS_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_2_0, 0), (self.blocks_add_xx_0, 2))    
        self.connect((self.blocks_multiply_const_vxx_2_1, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_multiply_xx_2, 0))    
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.blocks_multiply_xx_2_0, 0))    
        self.connect((self.blocks_multiply_xx_2, 0), (self.blocks_delay_0, 0))    
        self.connect((self.blocks_multiply_xx_2, 0), (self.blocks_multiply_xx_4, 1))    
        self.connect((self.blocks_multiply_xx_2_0, 0), (self.blocks_multiply_xx_4_0, 1))    
        self.connect((self.blocks_multiply_xx_3, 0), (self.fir_filter_xxx_0, 0))    
        self.connect((self.blocks_multiply_xx_3_0, 0), (self.blocks_add_xx_0_0, 1))    
        self.connect((self.blocks_multiply_xx_3_0_0, 0), (self.blocks_multiply_const_vxx_2_0, 0))    
        self.connect((self.blocks_multiply_xx_3_0_0_0, 0), (self.blocks_multiply_const_vxx_2_1, 0))    
        self.connect((self.blocks_multiply_xx_3_0_0_1, 0), (self.blocks_multiply_const_vxx_2, 0))    
        self.connect((self.blocks_multiply_xx_3_0_1, 0), (self.blocks_add_xx_0_0, 2))    
        self.connect((self.blocks_multiply_xx_4, 0), (self.blocks_multiply_xx_3_0, 0))    
        self.connect((self.blocks_multiply_xx_4_0, 0), (self.blocks_multiply_xx_3_0_1, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_add_xx_0_0, 0))    
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_conjugate_cc_1, 0))    
        self.connect((self.fir_filter_xxx_1, 0), (self.blocks_multiply_const_vxx_1, 0))    

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

    def get_beta3_imag(self):
        return self.beta3_imag

    def set_beta3_imag(self, beta3_imag):
        self.beta3_imag = beta3_imag
        self.set_dpd13_imag(-self.beta3_imag)
        self.Test_ConfigurablePA_0. set_beta3(complex(self.beta3_real,self.beta3_imag))

    def get_variable_function_probe_0(self):
        return self.variable_function_probe_0

    def set_variable_function_probe_0(self, variable_function_probe_0):
        self.variable_function_probe_0 = variable_function_probe_0

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
        self.blocks_multiply_const_vxx_1.set_k((self.mu, ))

    def get_f3(self):
        return self.f3

    def set_f3(self, f3):
        self.f3 = f3
        self.Test_TotalFreqShift_0. set_shift_freq(self.f3*1000000) 
        self.Test_TotalFreqShift_0_0_0. set_shift_freq(int((self.f3-self.f1)*1000000)) 
        self.Test_TotalFreqShift_0_0_0_0_0. set_shift_freq(int(2*self.f1-self.f3)*1000000) 
        self.Test_TotalFreqShift_0_0_0_0. set_shift_freq(int(2*self.f3-self.f1)*1000000) 

    def get_f2(self):
        return self.f2

    def set_f2(self, f2):
        self.f2 = f2
        self.Test_TotalFreqShift_0_0. set_shift_freq(self.f2*1000000) 

    def get_f1(self):
        return self.f1

    def set_f1(self, f1):
        self.f1 = f1
        self.Test_TotalFreqShift_0_0_0. set_shift_freq(int((self.f3-self.f1)*1000000)) 
        self.Test_TotalFreqShift_0_1. set_shift_freq(self.f1*1000000) 
        self.Test_TotalFreqShift_0_0_0_0_0. set_shift_freq(int(2*self.f1-self.f3)*1000000) 
        self.Test_TotalFreqShift_0_0_0_0. set_shift_freq(int(2*self.f3-self.f1)*1000000) 

    def get_dpd13_real(self):
        return self.dpd13_real

    def set_dpd13_real(self, dpd13_real):
        self.dpd13_real = dpd13_real
        self.analog_const_source_x_0.set_offset(self.dpd13_real)
        self.analog_const_source_x_0_1.set_offset(self.dpd13_real)

    def get_dpd13_imag(self):
        return self.dpd13_imag

    def set_dpd13_imag(self, dpd13_imag):
        self.dpd13_imag = dpd13_imag
        self.analog_const_source_x_0_0.set_offset(self.dpd13_imag)
        self.analog_const_source_x_0_0_0.set_offset(self.dpd13_imag)

    def get_beta7_real(self):
        return self.beta7_real

    def set_beta7_real(self, beta7_real):
        self.beta7_real = beta7_real
        self.Test_ConfigurablePA_0. set_beta7(complex(self.beta7_real,self.beta7_imag))

    def get_beta7_imag(self):
        return self.beta7_imag

    def set_beta7_imag(self, beta7_imag):
        self.beta7_imag = beta7_imag
        self.Test_ConfigurablePA_0. set_beta7(complex(self.beta7_real,self.beta7_imag))

    def get_beta5_real(self):
        return self.beta5_real

    def set_beta5_real(self, beta5_real):
        self.beta5_real = beta5_real
        self.Test_ConfigurablePA_0. set_beta5(complex(self.beta5_real,self.beta5_imag))

    def get_beta5_imag(self):
        return self.beta5_imag

    def set_beta5_imag(self, beta5_imag):
        self.beta5_imag = beta5_imag
        self.Test_ConfigurablePA_0. set_beta5(complex(self.beta5_real,self.beta5_imag))

    def get_beta1_real(self):
        return self.beta1_real

    def set_beta1_real(self, beta1_real):
        self.beta1_real = beta1_real
        self.Test_ConfigurablePA_0. set_beta1(complex(self.beta1_real,self.beta1_imag))

    def get_beta1_imag(self):
        return self.beta1_imag

    def set_beta1_imag(self, beta1_imag):
        self.beta1_imag = beta1_imag
        self.Test_ConfigurablePA_0. set_beta1(complex(self.beta1_real,self.beta1_imag))

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
        self.blocks_multiply_const_vxx_2.set_k((self.a1, ))

    def get_ScalingForPA(self):
        return self.ScalingForPA

    def set_ScalingForPA(self, ScalingForPA):
        self.ScalingForPA = ScalingForPA
        self.blocks_multiply_const_vxx_0.set_k((self.ScalingForPA, ))
        self.blocks_multiply_const_vxx_0_0.set_k((self.ScalingForPA, ))
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.ScalingForPA, ))
        self.blocks_multiply_const_vxx_0_1.set_k((self.ScalingForPA, ))
        self.blocks_multiply_const_vxx_0_1_0.set_k((self.ScalingForPA, ))

    def get_LoopDelay(self):
        return self.LoopDelay

    def set_LoopDelay(self, LoopDelay):
        self.LoopDelay = LoopDelay
        self.blocks_delay_0.set_dly(self.LoopDelay)


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
