
'''

# 0 1 0 1 0
# 0 1 0 1 0
# 0 1 0 1 0
# 0 1 0 1 0
# 0 1 0 1 0

n = int(input())
for row in range(n):
    for col in range(n):
        print(col%2, end='')
    print()



# *
# * *
# * * *
# * * * *
# * * * * *

n = int(input())
for row in range(n):
    for col in range(row+1):
        print('*', end= ' ')
    print()



# * * * * *
# * * * *
# * * *
# * *
# *

n = int(input())
for i in range(n):
    for j in range(n-i):
        print('*', end=' ')
    print()




# * * * * *
#   * * * *
#     * * *
#       * *
#         *

n = int(input())
for i in range(n):
    for j in range(n):
        if i <= j:
            print('*', end= " ")
        else:
            print(' ', end= ' ')
    print()




#         *
#       * *
#     * * *
#   * * * *
# * * * * *

n = int(input("Enter the size: "))
for row in range(n):
    for sp in range(row):
        print(' ', end=' ')
    for col in range(n-row):
        print('*', end=' ')
    print()



    
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0

n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print((row+col)%2, end=' ')
    print()


# Another Method

n = int(input())
for i in range(n):
    for j in range(n):
        if i==j or j==n-i-1 or (j%2==0 and i%2==0):
            print("0", end = " ")
        else:
            print("1", end = " ")
    print()




# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

n = int(input("Enter the size: "))
c=1
for row in range(n):
    for col in range(row+1):
        print(str(c), end=' ')
        c+=1
    print()


#Another Metod
#Using the zfill to two digits
    
n = int(input("Enter the size: "))
c=1
for row in range(n):
    for col in range(row+1):
        print(str(c).zfill(2), end=' ')
        c+=1
    print()

'''
