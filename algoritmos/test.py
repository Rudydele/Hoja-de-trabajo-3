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
'''
from unittest import result
from searching.binary_search import binary
print("***Binary search***")
print("input: " , [4, 88, 8, -2, 0])
print("output: " , binary([3, 44, 7, -1, 0] , 0))

if result == -1:
    print("No existe")
'''
'''
from searching.linear_search import linear
print("***linear search***")
print("input: " , [1, 55, 6, -1, 0])
print("output: " , linear([6, 44, 5, -2, 0] , 7))
'''
'''
from sorting.bubble_sort_opt import bubble_opt
print("***bubble sort optimized***")
print("input: " , [1, 88, 6, -1, 0])
print("output: " , bubble_opt([4, 91, 5, -9, 0]))
'''
from sorting.bubble_sort import bubble_sort
print ("***bubble sort***")
print("input: " , [1, 88, 6, -1, 0])
print("output: " , bubble_sort([4, 91, 5, -9, 0]))
