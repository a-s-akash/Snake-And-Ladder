;it don't kill the opponent
org 100h
jmp start
empty db 0ah,0ah,0ah,24h
over db 'GAME OVER!!!$'
overs db '            $'
is_check db 1
award   db '                                                                                                                    ',0dh,0ah,024h
cross   db '     +-------------------------------------------------------------------------------------------------------------+',0dh,0ah,024h
space   db '     |          |          |          |          |          |          |          |          |          |          |',0dh,0ah,024h
up      db '     |    21    |    22    |    23    |    24    |    25    |    26    |    27    |    28    |    29    |    30    |',0dh,0ah,024h
uspace  db '     |          |       \-\|    ¥     |     ¥    |          |          |    ¥     |          |    ¥     |  finish  |',0dh,0ah,024h   
ocross  db '     +-------------------\-\0-0-0------------0--------------0-0-0-0-0-0-0-0-0-----0-0-0-0-0-0-0-0-0----------------+',0dh,0ah,024h
muspace db '     |          |         \0\         |       0  |         0|          |         0|          |          |          |',0dh,0ah,024h      
center  db '     |    20    |   19  <0 \-\  18    |    17  0 |    16 <0 |    15    |    14 <0 |    13    |    12    |    11    |',0dh,0ah,024h
mdspace db '     |          |          |          |    ¥    0 /-/       |          |       \-\|          |          |/-/       |',0dh,0ah,024h
tcross  db '     +---------------------0-0-0-0-0-0-0-0-0-----/0/-0-0-0-0-0-0-0-0-0-0--------\-\---------------------/-/--------+',0dh,0ah,024h
dspace  db '     |   start  |         0|          |         /-/         |          |0        \-\         |         /-/         |',0dh,0ah,024h
down    db '     |     1    |    2  <0 |     3    |     4  /-/     5    |     6    | 0>  7    \-\   8    |     9  /-/    10    |',0dh,0ah,024h
abspace db '     |  A    B  |          |          |          |          |          |          |          |          |          |',0dh,0ah,024h
slintro db 0ah,0ah,09h,09h,09h,09h,09h,09h,'      Snake and Ladder$'
enter db 0ah,0ah,0ah,0ah,0ah,0ah,0dh,09h,09h,09h,09h,09h,09h,'    Enter Player Names$'
p1 db 0ah,0ah,0ah,0ah,0dh,09h,09h,09h,09h,09h,09h,'    Player A:$'
p2 db 0ah,0ah,0dh,09h,09h,09h,09h,09h,09h,'    Player B:$'
pp1 db 'Player A$'
pp2 db 'Player B$'
wins_match db ' won the match...$'
ac db 8,19,30,41,52,63,74,85,96,107,107,96,85,74,63,52,40,36,18,8,8,19,30,41,52,63,74,85,96,107
ar db 14,14,14,14,14,14,14,14,14,14,8,8,8,8,8,8,8,8,8,8,4,4,4,4,4,4,4,4,4,4
bc db 13,24,35,46,57,68,79,90,101,112,112,101,90,74,68,56,40,36,18,13,13,24,35,46,57,68,79,90,101,112
br db 14,14,14,14,14,14,14,14,14,14,8,8,8,10,8,8,10,10,10,8,4,4,4,4,4,4,4,4,4,4
p1_name db 25 dup(0)
p2_name db 25 dup(0)
a db 'A$'
clr db ' $'
where dw 0
b db 'B$'
ca dw 0
cb dw 0 
c db 0
r db 0
who db 1
what dw 0
is_odd db 0
start:                                 
    mov ah,0
    int 16h
   ;jmp game
    mov dx,offset slintro
    call print_str
    mov dx,offset enter
    call print_str
    mov dx,offset p1
    call print_str
    lea si,p1_name
    call string_input
    mov dx,offset p2
    call print_str
    lea si,p2_name
    call string_input
    mov ah,09
    mov ah,02
    mov bh,00
    mov dl,0
    mov dh,0
    int 10h
    jmp game
game:
    mov dx,offset empty
    call print_str
    mov dx,offset cross
    call print_str
    mov dx,offset space
    call print_str
    mov dx,offset up
    call print_str
    mov dx,offset uspace
    call print_str
    mov dx,offset ocross
    call print_str
    mov dx,offset muspace
    call print_str
    mov dx,offset center
    call print_str
    mov dx,offset mdspace
    call print_str
    mov dx,offset tcross
    call print_str
    mov dx,offset dspace
    call print_str      
    mov dx,offset down
    call print_str
    mov dx,offset abspace
    call print_str    
    mov dx,offset cross
    call print_str
play:    
    mov is_check,0
    call last_line
    shr who,1
    jc odd
    jmp even
odd:
    rcl who,1
    mov dx,offset pp1
    call print_str 
    mov is_odd,1
    jmp move
even:
    rcl who,1
    mov dx,offset pp2
    call print_str
    mov is_odd,0
move:
    inc who
    mov ah,0
    int 16h
    sub al,30h
    cmp al,6
    jg move
    cmp al,1
    jb move
    cmp is_odd,1
    je yes_odd
    jmp yes_even
next:    
    jmp play
yes_odd:    
    mov ah,0 
    add ax,ca
    mov what,ax
    cmp what,30
    jl ok1
    mov cx,ca
    mov what,cx
ok1:    
    call clr_set_a
    mov ax,ca
    mov where,ax
    jmp check
yes_even: 
    mov ah,0
    add ax,cb
    mov what,ax
    cmp what,30
    jl ok2     
    mov cx,cb
    mov what,cx
ok2:    
    call clr_set_b
    mov ax,cb
    mov where,ax
    jmp check    
print_str:
    mov ah,09h
    int 21h
    ret
string_input:
    mov ah,1
    int 21h
    cmp al,0dh
    je finish_input
    mov [si],al
    inc si
    jmp string_input      
finish_input:
    mov [si],'$'
    ret
print_a:                
    mov dx,offset a
    mov ah,09h
    int 21h
    ret
print_b:
    mov dx,offset b    
    mov ah,09h
    int 21h
    ret
position:
    mov ah,02
    mov bh,00
    mov dl,c
    mov dh,r
    int 10h
    ret    
load_a:    
    lea si,ac    
    lea di,ar
    ret
load_b:    
    lea si,bc    
    lea di,br
    ret
xcg:    
    mov cl,[si]
    mov c,cl
    mov cl,[di]
    mov r,cl     
    ret
check:
    mov is_check,1
    cmp where,3
    je fto16   
    cmp where,7
    je eto14
    cmp where,8
    je nto11
    cmp where,17
    je e8to22
    cmp where,16
    je s7to2
    cmp where,23
    je t4to7
    cmp where,28
    je t9to14
    cmp where,26
    je t7to16
    cmp where,22
    je t3to19
    cmp where,29
    je finished
re_check:
    jmp next
fto16:
    mov what,15
    call further
eto14:
    mov what,13 
    call further
nto11:
    mov what,10 
    call further
e8to22:        
    mov what,21 
    call further
s7to2:        
    mov what,1  
    call further
t4to7:        
    mov what,6  
    call further
t3to19:       
    mov what,18 
    call further
t7to16:        
    mov what,15 
    call further
t9to14:        
    mov what,13 
    call further
clr_set_a:    
    call load_a
    add si,ca
    add di,ca
    mov cx,what
    mov ca,cx
    call xcg
    call position
    mov dx,offset clr
    call print_str
    call load_a
    add si,what
    add di,what
    call xcg
    call position
    call print_a
    cmp is_check,1
    je re_check
    ret
clr_set_b:    
    call load_b
    add si,cb
    add di,cb
    mov cx,what
    mov cb,cx
    call xcg
    call position
    mov dx,offset clr
    call print_str
    call load_b
    add si,what
    add di,what
    call xcg
    call position
    call print_b    
    cmp is_check,1
    je re_check
    ret    
further:    
    cmp is_odd,1
    je clr_set_a
    jmp clr_set_b        
    ret
finished:
    mov cx,5
ree:    
    call last_line
    mov dx,offset overs
    call print_str
    call last_line
    mov dx,offset over
    call print_str
    dec cx
    jnz ree
    mov ah,09
    mov ah,02
    mov bh,00
    mov dl,0
    mov dh,0
    int 10h
    mov dx,offset empty
    call print_str
    mov cx,14
re:    
    mov dx,offset award
    call print_str
    dec cx
    jnz re
    mov ah,02
    mov bh,00
    mov dl,52 
    mov dh,8
    int 10h
    cmp is_odd,1
    je pAwin
    jmp pBwin
pAwin:
    lea si,p1_name
    jmp announce
pBwin:
    lea si,p2_name              
announce:
    cmp [si],'$'
    je trophy
    mov dl,[si]
    mov ah,02h
    int 21h
    inc si
    jmp announce        
last_line:    
    mov dl,55
    mov dh,16
    mov ah,02
    mov bh,00
    int 10h
    ret    
trophy:
    mov dx,offset wins_match
    call print_str
    mov ah,0
    int 16h
    end    
