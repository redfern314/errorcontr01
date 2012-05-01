from numpy import *

def binary(code):
    for i in range(len(code)):
        code[i]=code[i]%2
        #print c[i]
    return code

#a=mat(["1 2; 3 4"]) #could also do mat([1.,2.],[3.,4.])

c=mat([1,0]) #one letter codeword
print "The original codeword is:"
print c
G=([1,0,1,1,1],[0,1,1,0,1])
#add parity bit to end
#print G
c=binary(c*G)
#c[0,0]+=1 #introduce error
c=binary(c)

print "The encoding is:"
print c
h_T=([1,1,1],[1,0,1],[1,0,0],[0,1,0],[0,0,1])
valid = c*h_T
valid=binary(valid)
#print valid
if valid.all()==0:
    print "valid codeword"
else:
    print "an error has occured"

