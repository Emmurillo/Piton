
SECTION .data
	y	dw	10
	xMsg: db "hola mundo",10
	xLen: equ $-xMsg

SECTION .text

global _start

_start:
	 nop
	 mov     ax,data
	 mov     ds,ax
	 xor     ax,ax

	mov eax,4
	mov ebx,1
	mov ecx,yMsg
	mov edx,yLen
	int 80H

	mov eax,4
	mov ebx,1
	mov ecx,"listo"
	int 80H

	mov eax,4
	mov ebx,1
	mov ecx,"8"
	int 80H

	mov     eax,1
	mov     ebx,0
	int     80H
