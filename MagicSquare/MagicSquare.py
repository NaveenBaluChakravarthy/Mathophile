
"""
Game : #01
Title : Magic Square
Author : Naveen Chakravarthy Balasubramanian
"""
# Defining the functions

def oddx1(a):
    i, j = 0, a//2
    for x in range(a * a):
       z[i][j] = x + 1
       k , l = (i - 1) % a, (j + 1) % a 
       if z[k][l] == 0:
          i, j = k, l
       else:
          i += 1
    return z

def even2x(a, sqcnt):
    lim1 = 0
    i, j, lim2 = 0, a//4, lim1 + sqcnt
    for x in range(lim1, lim2):
       z[i][j] = x + 1
       k , l = (i - 1) % (a // 2) , (j + 1) % (a // 2) 
       if z[k][l] == 0:
          i, j = k, l
       else:
          i += 1  

    lim1 = lim2
    i, j, lim2 = a // 2 , (a - 1) - (a // 4), lim1 + sqcnt
    for x in range(lim1, lim2):
       z[i][j] = x + 1
       k , l = (a // 2) + (i - 1) % (a // 2) , (a // 2) + (j + 1) % (a // 2)
       if z[k][l] == 0:
          i, j = k, l
       else:
          i += 1 

    lim1 = lim2
    i, j, lim2 = 0 , (a - 1) - (a // 4), lim1 + sqcnt
    for x in range(lim1, lim2):
       z[i][j] = x + 1
       k , l = (i - 1) % (a // 2) , (a // 2) + (j + 1) % (a // 2)
       if z[k][l] == 0:
          i, j = k, l
       else:
          i += 1 

    lim1 = lim2
    i, j, lim2 = a // 2 , a // 4, lim1 + sqcnt
    for x in range(lim1, lim2):
       z[i][j] = x + 1
       k , l = (a // 2) + (i - 1) % (a // 2) , (j + 1) % (a // 2)
       if z[k][l] == 0:
          i, j = k, l
       else:
          i += 1 

    for i in range(a // 2):
        for j in range(a // 4):
            k = (a // 2) + i
            if i == (a // 4):
                j += 1
            z[i][j], z[k][j] = z[k][j] , z[i][j]

    if a > 6:            
        p = ((a - 2) // 4) - 1
        q = a - p
        for i in range(a // 2):
            for j in range(q, a):
                k = (a // 2) + i
                z[i][j], z[k][j] = z[k][j] , z[i][j]

    return z       
    
def even4x(a):
    x = 1
    q1 = a // 4
    q3 = 3 * q1
    y = (a * a) + 1
    
    for i in range(a):
        for j in range(a):
            z[i][j] = x
            x += 1
    
    for i in range(0, q1):
        for j in range(0, q1):
            z[i][j] = y - z[i][j]
            
    for i in range(0, q1):
        for j in range(q3, a):
            z[i][j] = y - z[i][j]

    for i in range(q3, a):
        for j in range(0, q1):
            z[i][j] = y - z[i][j]

    for i in range(q3, a):
        for j in range(q3, a):
            z[i][j] = y - z[i][j]

    for i in range(q1, q3):
        for j in range(q1, q3):
            z[i][j] = y - z[i][j]
    return z
    
# Importing the libraries
import numpy as np
import pandas as pd
from datetime import datetime
currts = datetime.now()
filesfx = currts.strftime("%Y%m%d%H%M%S")

# Printing the Magic Square
N = input("Order of the Square : ")
try:
    a = int(N)
    if a > 2:
        z = np.zeros((a, a), dtype = int)
        if a % 2 == 1:
            magicsquare = oddx1(a)
            pd.DataFrame(magicsquare).to_excel(f"MagicSquare_Ins{filesfx}_Order{a}.xlsx", index=False, header = False)
        elif a % 4 == 0:
            magicsquare = even4x(a)
            pd.DataFrame(magicsquare).to_excel(f"MagicSquare_Ins{filesfx}_Order{a}.xlsx", index=False, header = False)
        elif a % 4 == 2:
            sqcnt = (a * a) // 4
            magicsquare = even2x(a, sqcnt)
            pd.DataFrame(magicsquare).to_excel(f"MagicSquare_Ins{filesfx}_Order{a}.xlsx", index=False, header = False)
        else:
            print("Wakanda number is this?")
    else:
        print("Order {a} Magic Square cannot be constructed. Order has to be greater than 2")
except ValueError:
    print(f"The input value {N} is not a natural number")