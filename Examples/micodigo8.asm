
SECTION .data
	x	dw	6
	resp	dw	1
	cont	dw	2

SECTION .text

global _start

_start:
	 nop
	 mov     ax,data
	 mov     ds,ax
	 xor     ax,ax

	mov 	eax,4
	mov 	ebx,1
	mov 	ecx,"1"
	int 	80H

	mov 	eax,4
	mov 	ebx,1
	mov 	ecx,respMsg
	mov 	edx,respLen
	int 	80H

	mov     eax,1
	mov     ebx,0
	int     80H
