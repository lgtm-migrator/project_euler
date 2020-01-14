"""
Project Euler problem 8 solution

The four adjacent digits in the 1000-digit number that have the greatest
product are 9 x 9 x 8 x 9 = 5832.

73167176531330624919225119674426574742355349194934  
96983520312774506326239578318016984801869478851843  
85861560789112949495459501737958331952853208805511  
12540698747158523863050715693290963295227443043557  
66896648950445244523161731856403098711121722383113  
62229893423380308135336276614282806444486645238749  
30358907296290491560440772390713810515859307960866  
70172427121883998797908792274921901699720888093776  
65727333001053367881220235421809751254540594752243  
52584907711670556013604839586446706324415722155397  
53697817977846174064955149290862569321978468622482  
83972241375657056057490261407972968652414535100474  
82166370484403199890008895243450658541227588666881  
16427171479924442928230863465674813919123162824586  
17866458359124566529476545682848912883142607690042  
24219022671055626321111109370544217506941658960408  
07198403850962455444362981230987879927244284909188  
84580156166097919133875499200524063689912560717606  
05886116467109405077541002256983155200055935729725  
71636269561882670428252483600823257530420752963450  

Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?

"""
from typing import Tuple

problem_series = (
    '73167176531330624919225119674426574742355349194934'
    '96983520312774506326239578318016984801869478851843'
    '85861560789112949495459501737958331952853208805511'
    '12540698747158523863050715693290963295227443043557'
    '66896648950445244523161731856403098711121722383113'
    '62229893423380308135336276614282806444486645238749'
    '30358907296290491560440772390713810515859307960866'
    '70172427121883998797908792274921901699720888093776'
    '65727333001053367881220235421809751254540594752243'
    '52584907711670556013604839586446706324415722155397'
    '53697817977846174064955149290862569321978468622482'
    '83972241375657056057490261407972968652414535100474'
    '82166370484403199890008895243450658541227588666881'
    '16427171479924442928230863465674813919123162824586'
    '17866458359124566529476545682848912883142607690042'
    '24219022671055626321111109370544217506941658960408'
    '07198403850962455444362981230987879927244284909188'
    '84580156166097919133875499200524063689912560717606'
    '05886116467109405077541002256983155200055935729725'
    '71636269561882670428252483600823257530420752963450')


def largest_product_in_series(number_series: str, adjacent_digits: int = 13) -> Tuple[int, str]:
    """
    Find the largest product of the digits of a substring of given length in a
    supplied `number_series`.

    Return a tuple of the largest product, and the substring that multiplies to
    give it.

    :param number_series: str
    :param adjacent_digits: int
    :return: tuple
    """
    largest = 0
    largest_start_index = 0
    for index, number in enumerate(number_series[:-adjacent_digits]):

        product = 1
        for i in range(adjacent_digits):
            product *= int(number_series[index + i])
        if product > largest:
            largest = product
            largest_start_index = index
    return largest, number_series[largest_start_index:largest_start_index + adjacent_digits]


"""
# Solution to problem 8
largest_product_in_series(problem_series, 13)) == (23514624000, '5576689664895')
"""
