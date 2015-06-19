
SECTION .data
	x	dw	None

SECTION .text

global _start

_start:
	 nop
	 mov     ax,data
	 mov     ds,ax
	 xor     ax,ax

	mov     eax,1
	mov     ebx,0
	int     80H
