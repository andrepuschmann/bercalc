bercalc
=======

For reviewing someones work on digital modulation
I needed something to quickly plot bit error rate (BER) curves
of various digital modulation schemes.
There is plenty of Matlab scripts [[[1]](http://www.gaussianwaves.com/2010/04/performance-comparison-of-digital-modulation-techniques-2/)]
but nothing that runs on a standard Linux without having to install a
bunch of other programs. 

So I created this Python script that plots the theoretical BER 
for various modulation schemes as a function of Eb/N0.

![Example](/berplot.png "Output of the script.")
