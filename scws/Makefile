CC=clang
# CFLAGS=-O2 -Wall
CFLAGS=-I/usr/local/include/scws -I/usr/include/python2.7 -g -Wall
LDFLAGS=-lpython2.7 -lscws

.PHONY: all clean

all: scws.so

scws.so: scws.c
	$(CC) -shared $(CFLAGS) $(LDFLAGS) $+ -o $@

clean:
	-rm *.o
