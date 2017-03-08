# GNURadioDPD

To test, install gnuradio. 
Then, in the directory "gr-Test" create a directory called "build". In a terminal in that build directory do the following:
```
cmake ..
make
sudo make install
sudo ldconfig
```

This will install the OOT module Test into your local GNURadio installation. You should then be able to open the flowgraph and run it.  
