% global variables nv for input vector and n for sum of input vector
global nv
global n
 
nv = input('Please input the sample values like [n1 n2 n3]: ');
n = sum(nv);

% initial vector
v = [1, 1, 1];
 
% estimate values
options = optimset('Display', 'off', 'MaxFunEvals', 100000, 'MaxIter', 100000);
a = fminsearch(@three_var,v,options);
 
% obtaining distributed weights
weights = drchrnd(a, 50)
mean_weights = mean(weights());
 
fprintf('\n')
disp 'Displaying the weight matrix:'
disp (weights)
fprintf('\n')
disp 'Displaying mean weights:'
disp (mean_weights)

save('C:\Users\RAJARSI\Desktop\PROJECT\CODE\bays_weights.mat', 'mean_weights');

function r = drchrnd(a,n)
% function to create the dirichlet distribution
p = length(a);
r = gamrnd(repmat(a,n,1),1,n,p);
r = r ./ repmat(sum(r,2),1,p);
end


function func = three_var(v)
% function to create the marginal likelihood
global nv
global n

func = (gamma(sum(v))/(gamma(v(1))*gamma(v(2))*gamma(v(3))))*(factorial(n)/(factorial(nv(1))*factorial(nv(2))*factorial(nv(3))))*((gamma(v(1)+nv(1))*gamma(v(2)+nv(2))*gamma(v(3)+nv(3)))/gamma(v(1)+nv(1)+v(2)+nv(2)+v(3)+nv(3)));
func = -func;
% maximised value for a single iteration
end