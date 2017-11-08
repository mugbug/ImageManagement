M = [1 2 3; 4 5 6; 7 8 9];
M = M';

s = size(M);
s = s(1) * s(2); // lenght(s)
DCT = [];

for k = 0:s-1 // k=0 pq vai usar na formula
    dctsum = 0;
    for n = 0:s-1 // n=0 msm coisa do k
        value = M(n+1) * cos((%pi/s)*(n+0.5)*k);
        dctsum = dctsum + value;
    end
    DCT(k+1) = dctsum; // k+1 pq a 1a posicao no scilab é 1
end

DCT = DCT';
disp(DCT);
