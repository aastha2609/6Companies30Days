'''
    Time complexity : O(N)
    Space complexity : O(H)

    where N is the number of nodes in the tree 
    and H is the height of the tree.

    H is equal to log(N) for a balanced tree
'''
from sys import stdin,setrecursionlimit
from queue import Queue

setrecursionlimit(10**7)

# Binary tree node class for reference 
class BinaryTreeNode :
	def __init__(self, data) :
		self.data = data
		self.left = None
		self.right = None



class Triplet :

    def __init__(self, max, above, below) :

        self.max = max
        self.above = above
        self.below = below
    

def fun( root,start) :

    if(root == None) :
        
        return Triplet(-1, -1, 0)
    
    
    left = fun(root.left, start)
    right = fun(root.right, start)
		
    ans = Triplet(-1, -1, 0)
		
    # Node is the starting node
    if(root.data == start) :

        below = max(left.below, right.below)
        ans.max = below
        ans.above = 0
        ans.below = below
	
    
    # Starting Node is in left subtree
    elif(left.above != -1) :

        ans.max = max(left.max, max(left.below, left.above + right.below + 1))
        ans.above = left.above + 1
        ans.below = left.below
    
    # Starting Node is in right subtree
    elif(right.above != -1) :

        ans.max = max(right.max, max(right.below, right.above + left.below + 1))
        ans.above = right.above + 1
        ans.below = right.below
    
    # Starting Node doesn't exist in the subtree
    else :
        ans.max = -1
        ans.above = -1
        ans.below = max(left.below, right.below) + 1
    
    return ans
	
def timeToBurnTree(root, start):

    ans = fun(root, start)
        
    return ans.max


# Fast input
def takeInput() :
	
    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1) :
        start = int(input().strip())
        return None, start

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0) :
        currentNode = q.get()  
        
        leftChild = arr[index]
        
        if(leftChild != -1) :
            leftNode =  BinaryTreeNode(leftChild)  
            currentNode.left = leftNode  
            q.put(leftNode)  
        
        index += 1
        rightChild = arr[index]
        
        if(rightChild != -1) :
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode  
            q.put(rightNode)  

        index += 1

    start = int(input().strip())

    return root, start

#main

root, start = takeInput()

print(timeToBurnTree(root, start))