INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_TEST Test)

FIND_PATH(
    TEST_INCLUDE_DIRS
    NAMES Test/api.h
    HINTS $ENV{TEST_DIR}/include
        ${PC_TEST_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    TEST_LIBRARIES
    NAMES gnuradio-Test
    HINTS $ENV{TEST_DIR}/lib
        ${PC_TEST_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(TEST DEFAULT_MSG TEST_LIBRARIES TEST_INCLUDE_DIRS)
MARK_AS_ADVANCED(TEST_LIBRARIES TEST_INCLUDE_DIRS)

