from numpy import *
import pdb
from mathCode import *

def generate_ldpc(rows,columns):
    #create a matrix of all zeros
    zeros_array = zeros((rows,columns))
    ldpc = matrix(zeros_array)

    #place 5 randoms 1s in each column
    for i in range(columns):
        for j in range(3):
            randrow=int(random.random()*rows)
            while ldpc[randrow,i]==1:
                randrow=int(random.random()*rows)
            ldpc[randrow,i]=1

    numones=0.0
    zeros_array = zeros((rows,1))
    rowones = matrix(zeros_array)
    for i in range(rows):
        for j in range(columns):
            if ldpc[i,j]==1:
                numones+=1
                rowones[i,0]+=1

    print ldpc
    print rowones
    avgones=numones/rows
    if not int(avgones)==avgones:
        print 'Avg number of ones: ' + str(avgones)
        print 'This is invalid.'
        pdb.set_trace()
    
    for a in range(10):
        templist=[]
        for i in range(rows):
            if rowones[i,0]>avgones:
                randcol=int(random.random()*columns)
                while ldpc[i,randcol]==0:
                    randcol=int(random.random()*columns)
                for j in range(rows):
                    if rowones[j,0]<avgones and (not ldpc[j,randcol]==1) and (not j==i):
                        templist.append(j)
                if not len(templist)==0:
                    randrow=int(random.random()*len(templist))
                    ldpc[i,randcol]=0
                    rowones[i,0]-=1
                    ldpc[templist[randrow],randcol]=1
                    rowones[templist[randrow],0]+=1
            templist=[]

    savetxt('pmatrix.txt',ldpc)
    print ldpc
    print rowones
    return ldpc

def stdForm(H):
    print shape(H)
    [n,q]=shape(H)
    #need n*n matrix to be identity

    #make sure that the diagonal has all ones
    #i iterates columns, j iterates rows
    rowops=[] #contains tuple of the form: (row operated on, row added to it)
    for i in range(n):
        if H[i,i]==0:
            for j in range(n):
                if H[j,i]==1 and j>i:
                    H[i,:]=binary(H[i,:]+H[j,:])
                    rowops.append((i,j))
                    #pdb.set_trace()
                    break
        for j in range(n):
            if H[j,i]==1 and (not j==i):
                H[j,:]=binary(H[i,:]+H[j,:])
                rowops.append((j,i))
    return [H,rowops]

def unStdForm(G,rowops):
    for op in rowops:
        G[op[0],:]=binary(G[op[0],:]+G[op[1],:])
    return G

count=0
H=matrix([0,1])
while not(equal(H[:,0:shape(H)[1]/2],eye(shape(H)[1]/2)).all()==True):
    H=generate_ldpc(25,50)
    [stdH,rowops]=stdForm(H)
    H=stdH
    count+=1
    print count
savetxt('testmatrix.txt',stdH)
pdb.set_trace()
P=stdH[:,25:50]
print P
ident=matrix(eye(25))
stdG=concatenate((transpose(P),ident),1)
print 'Std form G:'
print stdG
savetxt('gmatrix.txt',stdG)
G=unStdForm(stdG,rowops)
print 'Un-std form G:'
print G
print stdH
print binarymatrix(H*transpose(G))
savetxt('hmatrix.txt',H)