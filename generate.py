from numpy import *

def generate_ldpc(rows,columns):
    #create a matrix of all zeros
    zeros_array = zeros((rows,columns))
    ldpc = matrix(zeros_array)

    #place 5 randoms 1s in each column
    for i in range(columns):
        for j in range(5):
            randrow=int(random.random()*rows)
            while ldpc[randrow,i]==1:
                randrow=int(random.random()*rows)
            ldpc[randrow,i]=1

    for i in range(rows):
        numones=0
        for j in range(columns):
            if ldpc[i,j]==1:
                numones+=1
        while numones < 2:
            randcol=int(random.random()*columns)
            while ldpc[randcol,i]==1:
                randcol=int(random.random()*columns)
            ldpc[i,randcol]=1
    print ldpc
    return ldpc

generate_ldpc(10,5)