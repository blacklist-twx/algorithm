#从库中引入图类和顶点类
from pythonds.graphs import Graph,Vertex
#dfs的主函数  其中n代表树的深度  path代表这个节点前所有已经访问了的点的列表
#u 代表我们正在探索的点   limit代表搜索的总深度
def knightTour(n,path,u,limit):
    #将u点设为灰色  代表正在探索
    u.setColor('gray')
    # 探索过之后 路径中加入u点
    path.append(u)
    #如果树的深度未达到总深度 继续深入树
    if n < limit:
        #获取u的邻居 准备逐个继续深入探索
        nbrList = list(u.getConnections())
        #设置i来表示每位邻居
        i = 0
        done = False
        #当邻居未被遍历完，而且搜索也没有成功时
        while i < len(nbrList) and not done:
            # 如果这位邻居是白色 即可以搜索
            if nbrList[i].getColor() == 'white':
                # 对这位邻居展开搜索
                done = knightTour(n+1,path,nbrList[i],limit)
            i+=1#指针指向下一位邻居
        #如果该节点最终没有成功搜索完毕，那就返回上一层，并将这个节点设为可探索
        if not done:
            path.pop()
            u.setColor('white')
    #搜索成功
    else:
        done = True
        #将路径上的点都打印出来
        for each in path:
            print(each.id)
    return done
'''建图'''        
g = Graph()
for each in 'ABCDEF':
    g.addVertex(each)
g.addEdge('A','B',1)
g.addEdge('A','D',1)
g.addEdge('B','D',1)
g.addEdge('B','C',1)
g.addEdge('C','',1)
g.addEdge('D','E',1)
g.addEdge('E','B',1)
g.addEdge('E','F',1)
g.addEdge('F','C',1)


A = g.getVertex('A')

lst = []
print(knightTour(1,lst,A,6))

