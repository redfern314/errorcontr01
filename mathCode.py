from numpy import *
import pdb

def binary(code):
    for i in range(code.size):
        code[0,i]=code[0,i]%2
    return code

def binarymatrix(A):
    [n,m] = shape(A)
    for i in range(n):
        A[i,:]=binary(A[i,:])
    return A

#a=mat(["1 2; 3 4"]) #could also do mat([1.,2.],[3.,4.])

#Define message and generator matrix
#Generate codeword
def getCodeword(c):
    #c=mat([1,0]) #one letter codeword
    #print "The original codeword is:"
    #print c
    #c=matrix(zeros((1,25)))
    ident=matrix(eye(25))
    ldpc=genfromtxt("gmatrix.txt")
    G=ldpc
    #G=concatenate((ident,transpose(ldpc)),1)
    #G=([1,0,1,1,1],[0,1,1,0,1])
    #add parity bit to end
    #print G
    pdb.set_trace()
    c=binary(c*G)
    #c[0,3]+=1 #introduce error
    print c
    c=binary(c)
    return c

#takes a received message and outputs original codeword
#DO NOT USE
#NOT GOOD
def getMessage(r):
    #ident=matrix(eye(5))
    ldpc=genfromtxt("gmatrix.txt")
    #G=concatenate((ldpc,ident),1)
    c=binary(r*linalg.inv(transpose(ldpc)))
    pdb.set_trace()


def getH_T():
    #H_T=matrix([[1,1,1],[1,0,1],[1,0,0],[0,1,0],[0,0,1]])
    ldpc=matrix(transpose(genfromtxt("hmatrix.txt")))
    return ldpc
    #ident=matrix(eye(5))
    #H_T=transpose(concatenate((ident,ldpc),1))
    #return H_T

#Create a dictionary with syndromes as keys and error vectors as values
def getSyndromeTable():
    errors=matrix(concatenate((zeros((1,50)),eye(50)),0))
    syndromes=errors*getH_T()
    lookup={}
    for i in range(shape(errors)[1]):
        strsyn=''
        for j in range(shape(syndromes[i])[1]):
            strsyn=strsyn+str(int(syndromes[i][0,j]))
        if strsyn in lookup:
            print strsyn + ' is a duplicate syndrome - time to revise the code!'
        lookup[strsyn]=errors[i]
    return lookup

#Compute syndrome for received codeword
def isValidCodeword(c):
    #print "The encoding is:"
    #print c
    valid = c*getH_T()
    valid=binary(valid)
    #print valid
    if valid.all()==0:
        return True
        #print "valid codeword"
    else:
        return False
        #print "an error has occured"

#Looks up the error vector
def getError(c):
    errsyn=''
    for j in range(shape(c*getH_T())[1]):
        errsyn=errsyn+str(int((c*getH_T())[0,j])%2)
    #pdb.set_trace()
    #print errsyn
    lookup=getSyndromeTable()
    if errsyn in lookup:
        errvec=lookup[errsyn]
        return errvec
        print 'Error vector: ',errvec
    else:
        print 'not found'
        return zeros(shape(c))
#Corrects the error vector
'''
m=matrix([1,0,0,1,0,1]) 
print "The original message is:"
print m
c=getCodeword(m)
print "The encoded message before errors is:"
print c
print binary(c*getH_T())
c[0,5]+=1
c=binary(c)#introduce error
print "The code after an error is introduced is:"
print c
#pdb.set_trace()
e=getError(c)
print "The error is:"
print e
print "The codeword after error correction is:"
print binary(e+c)'''
'''
m=matrix([0,1,1,0,1,1,1,0,0,1,1,0,1,0,1,1,1,1,0,0,1,0,1,0,0])
c=getCodeword(m)
print 'Codeword:'
print c
c[0,2]+=1
c=binary(c)
print 'Received:'
print c
e=getError(c)
print 'Error:'
print e
print "The codeword after error correction is:"
print binary(e+c)
print 'Received message: ',binary(e+c)[0,25:50]'''