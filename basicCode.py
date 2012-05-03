from numpy import *
import pdb

def binary(code):
    for i in range(len(code)):
        code[i]=code[i]%2
        #print c[i]
    return code

#a=mat(["1 2; 3 4"]) #could also do mat([1.,2.],[3.,4.])

#Define message and generator matrix
#Generate codeword
c=mat([1,0]) #one letter codeword
print "The original codeword is:"
print c
G=([1,0,1,1,1],[0,1,1,0,1])
#add parity bit to end
#print G
c=binary(c*G)
c[0,0]+=1 #introduce error
c=binary(c)

#Create a dictionary with syndromes as keys and error vectors as values
errors=matrix([[0,0,0,0,0],[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]])
h_T=([1,1,1],[1,0,1],[1,0,0],[0,1,0],[0,0,1])
syndromes=errors*h_T
lookup={}
for i in range(shape(errors)[1]):
    strsyn=''
    for j in range(shape(syndromes[i])[1]):
        strsyn=strsyn+str(syndromes[i][0,j])
    if strsyn in lookup:
        print strsyn + ' is a duplicate syndrome - time to revise the code!'
    lookup[strsyn]=errors[i]

#Compute syndrome for received codeword
print "The encoding is:"
print c
valid = c*h_T
valid=binary(valid)
print valid
if valid.all()==0:
    print "valid codeword"
else:
    print "an error has occured"

#Looks up the error vector
errsyn=''
for j in range(shape(valid)[1]):
    errsyn=errsyn+str(valid[0,j])
print errsyn
if errsyn in lookup:
    errvec=lookup[errsyn]
    print 'Error vector: ',errvec
else:
    print 'not found'

#Corrects the error vector
print errvec+c