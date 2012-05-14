from numpy import *
import pdb
import pickle

def binary(code):
    for i in range(code.size):
        code[0,i]=code[0,i]%2
    return code

def binarymatrix(A):
    [n,m] = shape(A)
    for i in range(n):
        A[i,:]=binary(A[i,:])
    return A

#Define message and generator matrix

#Generate codeword
def getCodeword(c):
    ident=matrix(eye(25))
    ldpc=genfromtxt("gmatrix.txt")
    G=ldpc
    c=binary(c*G)
    return c

def getH_T():
    ldpc=matrix(transpose(genfromtxt("hmatrix.txt")))
    return ldpc

#Create a dictionary with syndromes as keys and error vectors as values
def generateSyndromeTable():
    errors=getErrorMatrix()
    syndromes=binarymatrix(errors*getH_T())
    lookup={}
    for i in range(shape(errors)[0]):
        strsyn=''
        for j in range(shape(syndromes[i])[1]):
            strsyn=strsyn+str(int(syndromes[i,j]))
        if strsyn in lookup:
            print strsyn + ' is a duplicate syndrome - time to revise the code!'
        lookup[strsyn]=errors[i,:]
        print strsyn, lookup[strsyn]
    f=open('syndromes.txt','w')
    pickle.dump(lookup, f)

def getSyndromeTable():
    f=open('syndromes.txt','r')
    syndromes=pickle.load(f)
    return syndromes

def generateErrorMatrix():
    errors=matrix(concatenate((zeros((1,50)),eye(50)),0))
    errors=matrix(zeros((1,50)))
    errorlist=[]
    allzeros=matrix(zeros((1,50)))
    print 'starting'
    #errorlist.append(errors)
    #loop through 1 error
    for i in range(50):
        currerr=matrix(zeros((1,50)))
        currerr[0,i]=1
        errors=matrix(concatenate((errors,currerr),0))
        #errorlist.append(errors)

    #loop through 2 errors
    for i in range(50):
        for j in range(50-i-1):
            j+=(i+1)
            currerr=matrix(zeros((1,50)))
            currerr[0,i]=1
            currerr[0,j]=1
            errors=matrix(concatenate((errors,currerr),0))
    
    #loop through 3 errors
    for i in range(50):
        print i
        for j in range(50-i-1):
            j+=(i+1)
            for k in range(50-j-1):
                k+=j+1
                currerr=matrix(zeros((1,50)))
                currerr[0,i]=1
                currerr[0,j]=1
                currerr[0,k]=1
                errors=matrix(concatenate((errors,currerr),0))
    '''
    #loop through 4 errors
    for i in range(50):
        print i
        for j in range(50-i-1):
            print j
            j+=(i+1)
            for k in range(50-j-1):
                k+=(j+1)
                for l in range(50-k-1):
                    l+=(k+1)
                    currerr=matrix(zeros((1,50)))
                    currerr[0,i]=1
                    currerr[0,j]=1
                    currerr[0,k]=1
                    currerr[0,l]=1
                    errors=matrix(concatenate((errors,currerr),0))'''

    #pdb.set_trace()
    print 'finished'
    savetxt('errormat.txt',errors)

def getErrorMatrix():
    errors=genfromtxt("errormat.txt")
    return matrix(errors)

#Compute syndrome for received codeword
def isValidCodeword(c):
    valid = c*getH_T()
    valid=binary(valid)
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
    lookup=getSyndromeTable()
    if errsyn in lookup:
        errvec=lookup[errsyn]
        return errvec
        print 'Error vector: ',errvec
    else:
        print 'not found'
        return zeros(shape(c))
'''
m=matrix([0,1,1,0,1,1,1,0,0,1,1,0,1,0,1,1,1,1,0,0,1,0,1,0,0])
c=getCodeword(m)
print 'Codeword:'
print c
c[0,48]+=1
c[0,49]+=1
c=binary(c)
print 'Received:'
print c
pdb.set_trace()
e=getError(c)
print 'Error:'
print e
print "The codeword after error correction is:"
print binary(e+c)
print 'Received message: ',binary(e+c)[0,25:50]
'''
#generateErrorMatrix()
#generateSyndromeTable()