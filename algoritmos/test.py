'''
from brute_force.divisorsn import divisors

print("***Divisors de n***")
n = 381
result = divisors(381)
print("n: " + str(n) + "divisors: " + str(result))
'''

'''
from brute_force.pin_unlock import unlock
print("***pin unlock***")
print(unlock("3829"))
'''

'''
from brute_force.sum import suma
print("***sum***")
n = int(input("ingrese n: "))
'''
'''
from lists.largest_number import maximo
print("***largest number***")
maximo()
'''
'''
from lists.list_merge import comb
print ("***list merge***")
comb()
'''
'''
from recursion.coutdown import regresi
print ("***countdown***")
print(regresi(11))
'''
'''
from recursion.fsctorisl import fact
print("***Factorial of N***")
print("factorial de 8: ")
print(fact(8))
'''
'''
from recursion.fibonacci import fibonacci
print("***fibonacci***")
print(fibonacci(10))
'''
'''
from recursion.sum import sum
print("***Sum of first n numbers***")
print(sum(5))
'''
from unittest import result
from searching.binary_search import binary
print("***Binary search***")
print("input: " , [4, 88, 8, -2, 0])
print("output: " , binary([3, 44, 7, -1, 0] , 0))

if result == -1:
    print("No existe")
