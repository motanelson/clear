import copy
print ("\033c\033[40;37m\n")

ss="""8086 X86
80186 X86
80286 X86
80386 X86
80486 X86
ARM7 ARM
ARM8 ARM"""

def ordarray(s):
    ss=[]
    for a in s:
       ss.append(copy.copy(ord(a)))           
    return ss
l=ordarray(ss)
print(l)