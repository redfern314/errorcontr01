from numpy import *
import pdb

def binary(code):
    for i in range(code.size):
        code[0,i]=code[0,i]%2
    return code

#a=mat(["1 2; 3 4"]) #could also do mat([1.,2.],[3.,4.])

#Define message and generator matrix
#Generate codeword
def getCodeword(c):
    #c=mat([1,0]) #one letter codeword
    #print "The original codeword is:"
    #print c
    #c=matrix(zeros((1,25)))
    ident=matrix(eye(25))
    ldpc=genfromtxt("pmatrix.txt")
    G=concatenate((ident,ldpc),1)
    #G=([1,0,1,1,1],[0,1,1,0,1])
    #add parity bit to end
    #print G
    c=binary(c*G)
    #c[0,3]+=1 #introduce error
    print c
    c=binary(c)
    return c

#takes a received message and outputs original codeword
#DO NOT USE
#NOT GOOD
def getMessage(r):
    ident=matrix(eye(25))
    ldpc=genfromtxt("pmatrix.txt")
    G=concatenate((ident,ldpc),1)
    pdb.set_trace()
    c=binary(r*G)


def getH_T():
    #H_T=matrix([[1,1,1],[1,0,1],[1,0,0],[0,1,0],[0,0,1]])
    ldpc=genfromtxt("pmatrix.txt")
    ident=matrix(eye(25))
    H_T=transpose(concatenate((transpose(ldpc),ident),1))
    return H_T

#Create a dictionary with syndromes as keys and error vectors as values
def getSyndromeTable():
    errors=concatenate((zeros((1,50)),eye(50)),0)
    syndromes=errors*getH_T()
    lookup={}
    for i in range(shape(errors)[1]):
        strsyn=''
        for j in range(shape(syndromes[i])[1]):
            strsyn=strsyn+str(syndromes[i][0,j])
        if strsyn in lookup:
            print strsyn + ' is a duplicate syndrome - time to revise the code!'
        lookup[strsyn]=errors[i]
    pdb.set_trace()
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
        errsyn=errsyn+str((c*getH_T())[0,j])
    pdb.set_trace()
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
m=mat([1,0]) 
print "The original message is:"
print m
c=getCodeword(m)
print "The encoded message before errors is:"
print c
c[0,5]+=1
c=binary(c)#introduce error
print "The code after an error is introduced is:"
print c
e=getError(c)
print "The error is:"
print e
print "The codeword after error correction is:"
print binary(e+c)
'''