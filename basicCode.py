from numpy import *
#a=mat(["1 2; 3 4"]) #could also do mat([1.,2.],[3.,4.])
c=mat([1,1,1,1,0]) #one letter codeword
G=([1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,1],[0,0,0,0,0,1]) #add parity bit to end
print G
c=c*G
for i in range(len(c)):
    c[i]=c[i]%2
    print c[i]
print c


