from numpy import *

errors=matrix([[0,0,0,0],[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
HT=matrix([[1,1],[0,1],[1,0],[0,1]])
syndromes=errors*HT

lookup={}
for i in range(5):
    strsyn=''
    for j in range(2):
        strsyn=strsyn+str(syndromes[i][0,j])
    if strsyn in lookup:
        print strsyn + ' is a duplicate syndrome - time to revise the code!'
    lookup[strsyn]=errors[i]

print lookup