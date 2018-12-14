import math
from numpy import array

def check_val(arr,e,i,j):
    row_check=1
    col_check=1
    for a in range(9):
        if e==arr[i][a]:
            row_check=0
            break

    if row_check:
        for b in range(9):
            if e==arr[b][j]:
                col_check=0
                break
        
        if col_check:
            I=int(math.floor(i/3))
            J=int(math.floor(j/3))
            for x in range(3*I,3*I+3):
                for y in range(3*J,3*J+3):
                    if arr[x][y]==e:
                        return 0
                        break
            return 1
    return 0

def next_box(arr,b=0,a=0):
    j=a
    for i in range(b,9):
        while j<9:
            if arr[i][j]==0:
                return i,j
            j+=1
        j=0
    return (-1,-1)

def solve(arr,i=0,j=0):
    if i==-1:
        return
    for e in range(1,10):
        if check_val(arr,e,i,j):
            arr[i][j]=e
            I,J=next_box(arr,i,j)
            solve(arr,I,J)
    if next_box(arr,i,j)[0]==-1:
        return
    if e==9:
        arr[i][j]=0
    return

arr=array([[0,6,0,0,0,5,7,0,2],
[0,0,4,0,9,6,0,1,0],
[8,7,1,3,0,2,0,0,0],
[5,0,0,0,7,1,3,0,0],
[0,3,0,0,5,0,0,7,0],
[0,0,7,8,2,0,0,0,5],
[0,0,0,5,0,9,6,8,7],
[0,8,0,2,6,0,1,0,0],
[7,0,6,4,0,0,0,2,0]])

solve(arr)
print(arr)