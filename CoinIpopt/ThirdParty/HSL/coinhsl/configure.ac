# Copyright (C) 2011 Science and Technology Facilities Council.

# Author:  Jonathan Hogg               STFC   2011-09-20

####################################################################

# initialise automake
AC_INIT(coinhsl-archive, 2014.01.17, hsl@stfc.ac.uk)
AC_CONFIG_SRCDIR([ma27/ma27d.f])
AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE([subdir-objects])

# check for required programs
AC_PROG_FC
# Set f77 compiler to be same as f90 compiler unless explcitly told otherwise
if test "x$F77" = "x"; then
   F77="$FC"
fi
if test "x$FFLAGS" = "x"; then
   FFLAGS="$FCFLAGS"
fi
AC_PROG_F77
AC_PROG_CC
AC_PROG_LIBTOOL

# Define a macros to state availability, as per coin expectations
AC_DEFUN([HSL_CHECK_PKG],[
   pkg=$1
   AC_MSG_CHECKING([for $2])
   if test -r "$srcdir/$pkg/${pkg}d.f"; then
      AC_DEFINE(COINHSL_HAS_$2, [1], [Define to 1 if $2 is available.])
      coin_has_$1=yes
      AC_MSG_RESULT([yes])
   else
      coin_has_$1=no
      AC_MSG_RESULT([no])
   fi
   AM_CONDITIONAL(HAVE_$2, test x$coin_has_$1 = xyes)
   ])
AC_DEFUN([HSL_CHECK_PKG_F90],[
   pkg=$1
   AC_MSG_CHECKING([for $2])
   if test -r "$srcdir/$pkg/${pkg}d.f90"; then
      AC_DEFINE(COINHSL_HAS_$2, [1], [Define to 1 if $2 is available.])
      coin_has_$1=yes
      AC_MSG_RESULT([yes])
   else
      coin_has_$1=no
      AC_MSG_RESULT([no])
   fi
   AM_CONDITIONAL(HAVE_$2, test x$coin_has_$1 = xyes)
   ])

HSL_CHECK_PKG(mc19,MC19)
HSL_CHECK_PKG(ma27,MA27)
HSL_CHECK_PKG(ma28,MA28)

# Check if we're on Windows and have to do extra legwork for DLLs
AC_CHECK_HEADERS(windows.h)
AM_CONDITIONAL(TARGET_DLL, test x$ac_cv_header_windows_h = xyes)

# output data
AC_CONFIG_FILES([Makefile coinhsl.pc])
AC_CONFIG_HEADER(config.h CoinHslConfig.h)
AC_OUTPUT
