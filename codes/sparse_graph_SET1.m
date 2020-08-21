% taking edges
A=[0 0 0 0 0 1 1 2 2 2 2 3 3 3 4 4 4 5 5 5 6 6 6 6 7 7 7 7 8 8 8 9 9 9 10 10 10 10 11 11 11 11 12 12 12 12 13 13 14 14 15 15 16 16 17 18 19];
B=[0 1 2 3 4 5 6 5 6 7 8 5 7 8 6 7 8 9 10 11 9 10 11 12 9 10 11 12 10 11 12 13 14 15 13 14 15 16 13 14 15 16 13 14 15 16 17 18 17 18 17 18 17 18 19 19 19];
A = A + 1;
B = B + 1;

% taking path obtained
path = input('Enter path like [x1, x2,..., xn]: ');
path = path + 1;

W=[1000 52 61 8 16 78 41 84 63 2 99 71 223 73 55 44 88 11 22 33 21 32 43 54 74 85 96 14 64 75 35 66 55 44 91 97 73 19 45 65 25 85 73 37 87 16 86 84 74 76 2 6 7 9 52 25 1000];

%taking node ids
ids={'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'};

% creating sparse matrix
DG=sparse(A,B,W);

% creating and setting properties of graph
bg=biograph(DG,ids,'ShowWeights','off','LayoutType','equilibrium','ID','Equal weight graph','EdgeType','curved','ShowArrows','off','NodeAutoSize','off','LayoutScale',2.5,'Label','Graph with equal weights','Description','Graph with equal weights');
G=view(bg)
set(G.Nodes,'Color',[0.65 0.7559 1],'Shape','Ellipse','Size',[45 45],'LineColor',[0 0 0],'FontSize',20)
set(G.Nodes(path),'Color',[1 0.4 0.4])
edges=getedgesbynodeid(G,get(G.Nodes(path),'ID'));
set(edges,'LineColor',[1 0 0])
set(edges,'LineWidth',1.5)