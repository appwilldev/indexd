CC=clang
CFLAGS=-I/usr/local/include/scws -I/usr/include/python2.7 -fPIC -g -Wall
LDFLAGS=-lpython2.7 -lscws

.PHONY: all clean

all: scws.so

scws.so: scws.c
	$(CC) -shared $(CFLAGS) $(LDFLAGS) $+ -o $@

clean:
	-rm *.o
