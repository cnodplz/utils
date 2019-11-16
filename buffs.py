#!/usr/bin/python3
import collections

def main():

    registers_list32 = ['32-BIT REGISTERS (x86)', 'EIP', 'EBP', 'SFP']
    registers_list64 = ['64-BIT REGISTERS (x86)', 'RAX', 'RBX', 'RCX', 'RDX', 'RSI', 'RDI', 'RBP', 'RSP', 'RFLAGS', 'RIP', 'R8-R15']

    registers32 = {'32-BIT REGISTERS (x86)':'',
                   'EIP':'Extended Instruction Pointer',
                   'EBP':'Frame Pointer',
                   'SFP':'Saved Frame Pointer'}

    registers64 = {'64-BIT REGISTERS (x86)':'',
                   'RAX':'',
                   'RBX':'',
                   'RCX':'',
                   'RDX':'',
                   'RSI':'',
                   'RDI':'',
                   'RBP':'',
                   'RSP':'',
                   'RFLAGS':'',
                   'RIP':'',
                   'R8-R15':''}

    for x in registers_list32:
        print("{:<7}: {}".format(x, registers32[x]))
    print("")

    for x in registers_list64:
        print("{:<7}: {}".format(x, registers64[x]))
    print("")

if __name__ == '__main__':
    main()
