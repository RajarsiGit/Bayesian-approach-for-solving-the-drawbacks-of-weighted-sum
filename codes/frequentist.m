digits(6);
nv = input('Please input the sample values like [n1 n2 n3]: ');
n = sum(nv);

% calculating weights in a deterministic method
weights = [nv(1)/n nv(2)/n nv(3)/n];
fprintf('\n')
disp 'Displaying the weight matrix:'
disp (vpa(weights))
fprintf('\n')

save('C:\Users\RAJARSI\Desktop\PROJECT\CODE\freq_weights.mat', 'weights');