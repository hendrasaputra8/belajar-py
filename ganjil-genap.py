#!/bin/python3


N = int(input())

if (N % 2) == 1 :
    print ('weird')
elif (N % 2 == 0 and N in range(2,5)) :
    print ('not weird')
elif (N % 2 == 0 and N in range(6,21)) :
    print ('weird')
elif (N % 2 == 0 and N > 20 ):
    print ('Not weird')


#  odd even / ganjil genap
#  N ganjil, maka hasil nya weird
#  N genap dalam range 2-5, maka hasilnya not weird
#  N genap dalam range 6-20, maka hasil nya weird
#  N genap jika lebih dari 20