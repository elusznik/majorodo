#!/usr/bin/env python

import sys
import random

if __name__=="__main__":
    with open("rodo.txt") as rodo:
        teksty=[tekst.strip() for tekst in rodo]
    if len(sys.argv)==1:
        print(random.choice(teksty))
    elif len(sys.argv)==2:
        print(" ".join(random.sample(teksty, int(sys.argv[1]))))
        #print(sys.argv[1])
        """for i in range(int(sys.argv[1])):
            if i!=int(sys.argv[1])-1:
                print(choice(teksty), end=" ")
            else:
                print(choice(teksty))"""
