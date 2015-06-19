
SECTION .data
	xMsg: db "hola mundo",10
	xLen: equ $-xMsg
	c	dw	9
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
	mov 	ecx,"listo"
	int 	80H

	mov 	eax,4
	mov 	ebx,1
	mov 	ecx,"8"
	int 	80H

	mov 	eax,4
	mov 	ebx,1
	mov 	ecx,"Verdadero"
	int 	80H

	tmov 	eax,f
	mov 	c, eax
	xor 	eax, eax

	mov 	eax,4
	mov 	ebx,1
	mov 	ecx,cMsg
	mov 	edx,cLen
	int 	80H

	mov     eax,1
	mov     ebx,0
	int     80H
