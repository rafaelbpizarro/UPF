; Matrícula: 207749
; Nome: Rafael Brendler Pizarro

%include '../util.asm'

N equ 5

section .data
msg_pedido: db "Digite o numero: ", 0
msg_result: db "Diferenca (maior - menor): ", 0

section .text
global _start

process_values:
    push rbp
    mov rbp, rsp

    push rbx

    mov rcx, N

    lea rdi, [msg_pedido]
    call printstr
    call readint
    mov rbx, rax
    mov rdx, rax

.loop_values:
    dec rcx
    jz .end_loop

    lea rdi, [msg_pedido]
    call printstr
    call readint

    mov rsi, rax

    mov rdi, rbx
    cmp rsi, rdi
    cmovg rbx, rsi

    mov rdi, rdx
    cmp rsi, rdi
    cmovl rdx, rsi

    jmp .loop_values

.end_loop:
    mov rax, rbx
    sub rax, rdx

    pop rbx
    pop rbp
    ret

_start:

    call process_values

    lea rdi, [msg_result]
    call printstr

    mov rdi, rax
    call printint
    call endl

    call exit0
