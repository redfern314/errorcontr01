%k = 2, length of message
%n = 5, length of codeword

for i=1:4
    
    switch i
        case 1
            m=[0 0 0 0];
        case 2
            m=[0 1 0 0];
        case 3
            m=[1 0 0 0];
        case 4
            m=[1 1 0 0];
    end
    p= [1 0 0 0 0 1 1 1 1 0 0 1 1;0 1 0 0 1 0 1 1 1 1 0 0 1;
        0 0 1 0 1 1 0 1 0 1 1 0 1; 0 0 0 1 1 1 1 0 0 0 1 1 1];
    %p = [1 1 1 0;1 0 1 1]; %k by (n-k) matrix
    G = [eye(4),p]; % k by k identity
    %H = [p;[1 0 0;0 1 0;0 0 1]]; %(n-k)by(n-k) identity matrix
    c = m*G
    %c*H
end