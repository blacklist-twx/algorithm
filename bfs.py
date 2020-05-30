from pythonds.graphs import Graph,Vertex
from pythonds.basic import Queue
#g图和start起点
def bfs(g,start):
    start.setDistance(0) #起点的距离设为0
    start.setPred(None)#起点没有父节点
    vertQueue = Queue()#建立一个队列
    vertQueue.enqueue(start)#将起点加入队列中
    while(vertQueue.size()>0):#当队列存在对象时
        currentVert = vertQueue.dequeue()#弹出对象并设置为当前节点
        """该迭代阐明了bfs的特点就是把每个邻居都遍历，先完成一层，再往下完成，“广”"""
        for nbr in currentVert.getConnections():#搜索当前节点的所有邻居
            if(nbr.getColor()=='white'):#如果邻居x是白色的（即待搜索）
                nbr.setColor('gray')#设为灰色意为正在处理
                nbr.setDistance(currentVert.getDistance()+1)#该邻居距离为当前节点+1
                nbr.setPred(currentVert)#该邻居的父节点是当前节点
                vertQueue.enqueue(nbr)#队列加入该邻居
