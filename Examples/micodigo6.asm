
SECTION .data
	xMsg: db "hola dos",10
	xLen: equ $-xMsg
	cMsg: db "hola mundo",10
	cLen: equ $-cMsg
	hola	dw	5
	f	dw	9

SECTION .text

global _start

_start:
	 nop
	 mov     ax,data
	 mov     ds,ax
	 xor     ax,ax

	mov 	eax,4
	mov 	ebx,1
	mov 	ecx,cMsg
	mov 	edx,cLen
	int 	80H

	mov 	eax,4
	mov 	ebx,1
	mov 	ecx,cMsg
	mov 	edx,cLen
	int 	80H

	mov     eax,1
	mov     ebx,0
	int     80H
