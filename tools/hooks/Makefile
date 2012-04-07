all: libhooks_base.a buildscripts

include buildconf.makefile

CC=${HOOKS_CC}
CFLAGS=${HOOKS_CFLAGS} -fPIC

%.o: %.c *.h
	${CC} ${CFLAGS} -c -o $@ $<

lib%.a: %.o
	ar crs $@ $^

clean:
	rm -f *.o *.a

buildconf.makefile buildscripts:
	./makebuildscripts.py
