% taking edges
A=[2 1 1 1 1 1 1 1 1 1 2 3 4 5 6 7 8 9 10 11 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 21 12 13 14 15 16 22 23 24 25 26 27 22 23 24 25 26 27 28 29 30 31 17 32 18 19 34 19 18 37 36 36 34 36 39 38 37 35 38 35];
B=[1 3 4 5 6 7 8 9 10 11 3 4 5 6 7 8 9 10 11 2 12 13 14 15 16 17 18 19 20 21 13 14 15 16 17 18 19 20 21 12 22 23 24 25 26 27 23 24 25 26 27 17 28 28 29 30 31 32 29 30 31 32 33 33 33 34 35 35 37 33 37 38 39 39 37 33 34 20 32 22];

% taking path obtained
path = input('Enter path like [x1, x2,..., xn]: ');
path = path + 1;

W=ones(1,80);

%taking node ids
ids={'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39'};

% creating sparse matrix
DG=sparse(A,B,W);

% creating and setting properties of graph
bg=biograph(DG,ids,'ShowWeights','off','LayoutType','radial','ID','Equal weight graph','EdgeType','curved','ShowArrows','off','NodeAutoSize','off','LayoutScale',2.5,'Label','Graph with equal weights','Description','Graph with equal weights');
G=view(bg)
set(G.Nodes,'Color',[0.65 0.7559 1],'Shape','Ellipse','Size',[40 45],'LineColor',[0 0 0],'FontSize',20)
set(G.Nodes(path),'Color',[1 0.4 0.4])
edges=getedgesbynodeid(G,get(G.Nodes(path),'ID'))
set(edges,'LineColor',[1 0 0])
set(edges,'LineWidth',1.5)