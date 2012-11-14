SCWS_PREFIX=/usr/local
SCWS_INC=$(SCWS_PREFIX)/include
SCWS_LIB=$(SCWS_PREFIX)/lib
PYTHON_CONFIG=python-config

CFLAGS=-I$(SCWS_INC)/scws $(shell $(PYTHON_CONFIG) --includes) -fPIC -g -Wall
LDFLAGS=$(shell $(PYTHON_CONFIG) --ldflags) -lscws -L$(SCWS_LIB)

.PHONY: all clean

all: scws.so

scws.so: scws.c
	$(CC) -shared $(CFLAGS) $(LDFLAGS) $+ -o $@

clean:
	-rm scws.so
