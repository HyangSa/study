function ylpf = LPFy(y)
%
%
persistent prevY
persistent firstRun

if isempty(firstRun)
    prevY=y;
    firstRun = 1;
end

alpha2 = 0.9;
ylpf = alpha2*prevY + (1 - alpha2)*y;

prevY = ylpf;