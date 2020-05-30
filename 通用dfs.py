from pythonds.graphs import Graph,Vertex
class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        #新加入时间属性
        self.time = 0

    #dfs的主要代码
    def dfsvisit(self,startVertex):
        #对起点上灰色 代表正在搜索
        startVertex.setColor('gray')
        #时间+1
        self.time += 1
        #发现时间
        startVertex.setDiscovery(self.time)
        #对起点的邻居进行遍历
        for nextVertex in startVertex.getConnections():
            #如果该邻居白色
            if nextVertex.getColor()=='white':
                nextVertex.setPred(startVertex)
                #对他递归  继续深搜
                self.dfsvisit(nextVertex)
        #当起点的所有邻居都被搜索完毕  起点搜索任务结束  设为黑色
        startVertex.setColor('black')
        #时间+1
        self.time += 1
        #起点的结束时间
        startVertex.setFinish(self.time)

    def dfs(self):
        #遍历图的每个点
        for aVertex in self:
            #将所有点设为白色  即待搜索
            aVertex.setColor('white')
            #暂时不知道作用 类似于找父节点？
            aVertex.setPred(-1)

        #遍历所有顶点
        for aVertex in self:
            #如果顶点白色  那就对他深度优先搜索
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

g = DFSGraph()
g.addVertex('milk')
g.addVertex('egg')
g.addVertex('oil')
g.addVertex('mix')
g.addVertex('heatsyrup')
g.addVertex('heatgriddle')
g.addVertex('pour 1/4 cup')
g.addVertex('turn')
g.addVertex('eat')

g.addEdge('milk','mix')
g.addEdge('egg','mix')
g.addEdge('oil','mix')
g.addEdge('mix','heatsyrup')
g.addEdge('heatsyrup','eat')
g.addEdge('mix','pour 1/4 cup')
g.addEdge('heatgriddle','pour 1/4 cup')
g.addEdge('pour 1/4 cup','turn')
g.addEdge('turn','eat')

g.dfs()
lst = []
for each in g:
    print(each.id + str(each.getFinish()))
    
