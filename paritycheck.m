%k = 2, length of message
%n = 5, length of codeword

m = [1 1]; 
p = [1 1 1;1 1 1]; %k by (n-k) matrix
G = [[1 0;0 1],p]; % k by k identity 
H = [p;[1 0 0;0 1 0;0 0 1]]; %(n-k)by(n-k) identity matrix
c = m*G
c*H
