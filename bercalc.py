#!/usr/bin/env python
#
# bercalc.py
#
# Copyright (C) 2014, Andre Puschmann <andre.puschmann@tu-ilmenau.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np
import pylab as pl
import math
import scipy.special as ss
import random

# BER functions ..
# Taken from here:
# http://www.gaussianwaves.com/2010/04/performance-comparison-of-digital-modulation-techniques-2/

# BPSK/QPSK/4-QAM,..
def ber_qpsk(EbN0):
    return 0.5 * math.erfc(math.sqrt(EbN0))

# M-PSK    
def ber_mpsk(EbN0, M):
    k = math.log(M, 2)
    return 1 / k * math.erfc(math.sqrt(EbN0 * k) * math.sin(math.pi / M))

# M-QAM, (m must be even)
def ber_mqam(EbN0, M):
    k = math.log(M, 2)
    return 2 / k * (1 - 1 / math.sqrt(M)) * math.erfc(math.sqrt(3 * EbN0 * k/(2 * (M - 1))))

# Plotting functions ..
def plot_ber_qpsk():
    ber = [ber_qpsk(x) for x in EbN0_lin]
    pl.plot(EbN0_dB, ber, label="BPSK/QPSK")

# M-PSK
def plot_ber_mpsk():
    m = [3, 4]
    M = [2**x for x in m]
    for x in M:
        ber = [ber_mpsk(eb, x) for eb in EbN0_lin]
        pl.plot(EbN0_dB, ber, label="%d-PSK" % x)

# M-QAM
def plot_ber_mqam():
    k = [4, 6, 8] 
    M = [2**x for x in k]
    for m in M:
        ber = [ber_mqam(eb, m) for eb in EbN0_lin]
        pl.plot(EbN0_dB, ber, label="%d-QAM" % m)

def main():
    start = 0
    end = 25
    step = 1
    
    global EbN0_dB
    EbN0_dB = range(start, end, step)
    # convert to linear
    global EbN0_lin
    EbN0_lin = [10**(float(x)/10) for x in EbN0_dB]
    #print EbN0_lin
        
    pl.figure(1)
    ax = pl.subplot(1, 1, 1)   
    plot_ber_qpsk()
    plot_ber_mpsk()
    plot_ber_mqam()
    
    ax.set_yscale('log')
    pl.ylim([10**-5, 0.5])
    pl.legend(loc='best')
    pl.title("Digital Modulation Bit Error Rate Comparison")
    pl.xlabel('Eb/N0 [dB]')
    pl.ylabel('Bit Error Rate')
    pl.show()
    
if __name__ == "__main__":
    main()
