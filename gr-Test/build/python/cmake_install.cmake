# Install script for directory: /home/chance/DPD/gr-Test/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/Test" TYPE FILE FILES
    "/home/chance/DPD/gr-Test/python/__init__.py"
    "/home/chance/DPD/gr-Test/python/test.py"
    "/home/chance/DPD/gr-Test/python/FreqShift.py"
    "/home/chance/DPD/gr-Test/python/Freq2.py"
    "/home/chance/DPD/gr-Test/python/SimpleFreqShift.py"
    "/home/chance/DPD/gr-Test/python/BiSimpleShift.py"
    "/home/chance/DPD/gr-Test/python/TotalFreqShift.py"
    "/home/chance/DPD/gr-Test/python/MemorylessPA.py"
    "/home/chance/DPD/gr-Test/python/MeanCorrelation.py"
    "/home/chance/DPD/gr-Test/python/W_LMS.py"
    "/home/chance/DPD/gr-Test/python/alpha.py"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/Test" TYPE FILE FILES
    "/home/chance/DPD/gr-Test/build/python/__init__.pyc"
    "/home/chance/DPD/gr-Test/build/python/test.pyc"
    "/home/chance/DPD/gr-Test/build/python/FreqShift.pyc"
    "/home/chance/DPD/gr-Test/build/python/Freq2.pyc"
    "/home/chance/DPD/gr-Test/build/python/SimpleFreqShift.pyc"
    "/home/chance/DPD/gr-Test/build/python/BiSimpleShift.pyc"
    "/home/chance/DPD/gr-Test/build/python/TotalFreqShift.pyc"
    "/home/chance/DPD/gr-Test/build/python/MemorylessPA.pyc"
    "/home/chance/DPD/gr-Test/build/python/MeanCorrelation.pyc"
    "/home/chance/DPD/gr-Test/build/python/W_LMS.pyc"
    "/home/chance/DPD/gr-Test/build/python/alpha.pyc"
    "/home/chance/DPD/gr-Test/build/python/__init__.pyo"
    "/home/chance/DPD/gr-Test/build/python/test.pyo"
    "/home/chance/DPD/gr-Test/build/python/FreqShift.pyo"
    "/home/chance/DPD/gr-Test/build/python/Freq2.pyo"
    "/home/chance/DPD/gr-Test/build/python/SimpleFreqShift.pyo"
    "/home/chance/DPD/gr-Test/build/python/BiSimpleShift.pyo"
    "/home/chance/DPD/gr-Test/build/python/TotalFreqShift.pyo"
    "/home/chance/DPD/gr-Test/build/python/MemorylessPA.pyo"
    "/home/chance/DPD/gr-Test/build/python/MeanCorrelation.pyo"
    "/home/chance/DPD/gr-Test/build/python/W_LMS.pyo"
    "/home/chance/DPD/gr-Test/build/python/alpha.pyo"
    )
endif()

