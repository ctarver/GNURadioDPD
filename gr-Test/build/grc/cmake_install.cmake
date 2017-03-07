# Install script for directory: /home/chance/Documents/Git/GNURadioDPD/gr-Test/grc

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gnuradio/grc/blocks" TYPE FILE FILES
    "/home/chance/Documents/Git/GNURadioDPD/gr-Test/grc/Test_test.xml"
    "/home/chance/Documents/Git/GNURadioDPD/gr-Test/grc/Test_FreqShift.xml"
    "/home/chance/Documents/Git/GNURadioDPD/gr-Test/grc/Test_Freq2.xml"
    "/home/chance/Documents/Git/GNURadioDPD/gr-Test/grc/Test_SimpleFreqShift.xml"
    "/home/chance/Documents/Git/GNURadioDPD/gr-Test/grc/Test_BiSimpleShift.xml"
    "/home/chance/Documents/Git/GNURadioDPD/gr-Test/grc/Test_TotalFreqShift.xml"
    "/home/chance/Documents/Git/GNURadioDPD/gr-Test/grc/Test_MemorylessPA.xml"
    "/home/chance/Documents/Git/GNURadioDPD/gr-Test/grc/Test_MeanCorrelation.xml"
    "/home/chance/Documents/Git/GNURadioDPD/gr-Test/grc/Test_W_LMS.xml"
    "/home/chance/Documents/Git/GNURadioDPD/gr-Test/grc/Test_alpha.xml"
    "/home/chance/Documents/Git/GNURadioDPD/gr-Test/grc/Test_ConfigurablePA.xml"
    )
endif()

