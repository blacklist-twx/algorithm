from pythonds.graphs import PriorityQueue,Graph,Vertex
def dijkstra(aGraph,start):
    pq = PriorityQueue()#建立一个优先队列
    start.setDistance(0)#起点的距离为0
    #建堆（堆排序，按距离从小到大排序），用元组记录每个点的距离，将所有点放入列表
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    while not pq.isEmpty():#当队列有元素时
        currentVert = pq.delMin()#取出最小距离的点,设为当前节点
        for nextVert in currentVert.getConnections():#搜索当前节点的邻居
            #新距离=当前节点的距离+当前节点与该邻居的权重距离
            newDist = currentVert.getDistance()+currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():#如果新距离小于原来记录的距离
                nextVert.setDistance(newDist)#将近距离记录下来
                nextVert.setPred(currentVert)#将当前节点设为父节点
                pq.decreaseKey(nextVert,newDist)#因为距离修改了，所以调整堆顺序

aGraph = Graph()
aGraph.addEdge('u','v',2)
aGraph.addEdge('u','x',1)
aGraph.addEdge('u','w',5)
aGraph.addEdge('v','u',2)
aGraph.addEdge('v','x',2)
aGraph.addEdge('v','w',3)
aGraph.addEdge('w','v',3)
aGraph.addEdge('w','x',3)
aGraph.addEdge('w','u',5)
aGraph.addEdge('w','y',1)
aGraph.addEdge('x','u',1)
aGraph.addEdge('x','v',2)
aGraph.addEdge('x','w',3)
aGraph.addEdge('x','y',1)
aGraph.addEdge('y','x',1)
aGraph.addEdge('y','w',1)
aGraph.addEdge('y','z',1)
aGraph.addEdge('z','w',5)
aGraph.addEdge('z','y',1)

dijkstra(aGraph,aGraph.getVertex('u'))
vs = aGraph.vertices.values()
for each in vs:
    print(each.id +':'+ str(each.getDistance()))