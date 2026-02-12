; public symbols
extern	exit, exit0, strlen, itoa, atoi, endl, hello, printstr, printint, readstr, readint, numerosimpares, tde2

%ifidn __OUTPUT_FORMAT__, macho64
    default rel    
    %define     _start _main
%endif