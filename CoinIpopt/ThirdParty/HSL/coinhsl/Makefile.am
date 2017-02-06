AUTOMAKE_OPTIONS = foreign

ACLOCAL_AMFLAGS = -I m4

lib_LTLIBRARIES = libcoinhsl.la
include_HEADERS = CoinHslConfig.h

pkgconfigdir 	= $(libdir)/pkgconfig
pkgconfig_DATA = coinhsl.pc

libcoinhsl_la_LDFLAGS = -export-symbols $(srcdir)/libcoinhsl.sym
libcoinhsl_la_SOURCES = common/deps.f

EXTRA_DIST = LICENCE libcoinhsl.sym

if HAVE_MC19
libcoinhsl_la_SOURCES += mc19/mc19d.f
endif

if HAVE_MA27
libcoinhsl_la_SOURCES += ma27/ma27d.f
endif

if HAVE_MA28
libcoinhsl_la_SOURCES += ma28/ma28d.f
endif

if TARGET_DLL
libcoinhsl_la_LDFLAGS += -no-undefined
libcoinhsl_la_LIBADD = ${BLAS_LIBS}
endif
