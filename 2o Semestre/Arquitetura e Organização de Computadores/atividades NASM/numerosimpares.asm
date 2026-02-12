%include '../util.asm'

section .data
    msgEntrada db "Digite um numero (0 para sair): ", 0
    msgSaida   db "Quantidade de numeros impares: ", 0

section .bss
    contador resd 1
    numero   resd 1

section .text
global _start

_start:
    mov dword [contador], 0       ; zera o contador

leitura:
    ; mostra a mensagem de entrada
    mov eax, msgEntrada
    call imprime_str

    ; lê um número inteiro
    call leia_int
    mov [numero], eax

    ; se o número for zero, sai do loop
    cmp eax, 0
    je fim

    ; testa se o número é ímpar (bit menos significativo = 1)
    test eax, 1
    jz proximo_numero        ; se for par, pula incremento

    ; incrementa o contador
    mov eax, [contador]
    add eax, 1
    mov [contador], eax

proximo_numero:
    jmp leitura

fim:
    ; imprime mensagem final
    mov eax, msgSaida
    call imprime_str

    ; imprime o valor do contador
    mov eax, [contador]
    call imprime_int

    ; pula linha
    call imprime_nl

    ; encerra o programa
    call sai
