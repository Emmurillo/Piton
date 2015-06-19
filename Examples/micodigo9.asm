
SECTION .data
	xMsg: db "este",10
	xLen: equ $-xMsg

SECTION .text

global _start

_start:
	 nop
	 mov     ax,data
	 mov     ds,ax
	 xor     ax,ax

	mov 	eax,4
	mov 	ebx,1
	mov 	ecx,xMsg
	mov 	edx,xLen
	int 	80H

	mov 	eax,4
	mov 	ebx,1
	mov 	ecx,"Hola: "
	int 	80H

	mov 	eax,4
	mov 	ebx,1
	mov 	ecx,xMsg
	mov 	edx,xLen
	int 	80H

	mov     eax,1
	mov     ebx,0
	int     80H
