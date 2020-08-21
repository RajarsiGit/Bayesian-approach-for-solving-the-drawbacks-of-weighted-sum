load cost_mat;

% taking edges
A=[0 0 0 0 0 1 1 2 2 2 2 3 3 3 4 4 4 5 5 5 6 6 6 6 7 7 7 7 8 8 8 9 9 9 10 10 10 10 11 11 11 11 12 12 12 12 13 13 14 14 15 15 16 16 17 18 19];
B=[0 1 2 3 4 5 6 5 6 7 8 5 7 8 6 7 8 9 10 11 9 10 11 12 9 10 11 12 10 11 12 13 14 15 13 14 15 16 13 14 15 16 13 14 15 16 17 18 17 18 17 18 17 18 19 19 19];

%taking node ids
ids={'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'};

% taking path obtained
path = [1, 3, 8, 13, 17, 19, 20]

for i=1:57
    A(i)=A(i)+1;
    B(i)=B(i)+1;
end

% putting the costs in the weight vector
k=1;
for i=1:20
    for j=i:20
        if cost(i,j)<10000
            W(k)=cost(i,j);
            k=k+1;
        end
    end
end

% creating sparse matrix
DG=sparse(A,B,W)

% creating and setting properties of graph
bg=biograph(DG,ids,'ID','Equal weight graph','EdgeType','curved','ShowArrows','off','NodeAutoSize','off','LayoutScale',3,'Label','Graph with equal weights','Description','Graph with equal weights');
G=view(bg)
set(G.Nodes,'Color',[0.5 1 0.5],'Shape','Ellipse','Size',[25 25],'LineColor',[0 0 0])
set(G.Nodes(path),'Color',[1 0.4 0.4])
edges=getedgesbynodeid(G,get(G.Nodes(path),'ID'));
set(edges,'LineColor',[1 0 0])
set(edges,'LineWidth',1.5)
