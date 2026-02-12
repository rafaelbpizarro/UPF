# Makefile for util.asm assembly samples

UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
	FORMAT = elf64
	LINKER = ld
endif
ifeq ($(UNAME_S),Darwin)
	FORMAT = macho64
	LINKER = gcc
endif


all:	hello printint readstr readint numerosimpares tde2

hello:	hello.asm ../util.asm
	nasm -f $(FORMAT) hello.asm
	$(LINKER) -o hello hello.o

readstr:	readstr.asm ../util.asm
	nasm -f $(FORMAT) readstr.asm
	$(LINKER) -o readstr readstr.o
		
printint:	printint.asm ../util.asm
	nasm -f $(FORMAT) printint.asm
	$(LINKER) -o printint printint.o

readint:	readint.asm ../util.asm
	nasm -f $(FORMAT) readint.asm
	$(LINKER) -o readint readint.o

numerosimpares:	numerosimpares.asm ../util.asm
	nasm -f $(FORMAT) numerosimpares.asm
	$(LINKER) -o numerosimpares numerosimpares.o

tde2:	tde2.asm ../util.asm
	nasm -f $(FORMAT) tde2.asm
	$(LINKER) -o tde2 tde2.o

rebuild:
	make clean
	make all

clean:
	rm -f hello printint readstr readint numerosimpares tde2
	rm -f *~
	rm -f *.o
