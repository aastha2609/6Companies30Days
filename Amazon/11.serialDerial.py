# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    

    def serialize(self, root):
        
        
        A=[]
        def dfs(root):
            if not root :
                A.append("null")
                return
              
            
            A.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)   
        return ",".join(A)
        
        

    def deserialize(self, data):
        
        val=data.split(",")
        self.i=0
        def CreateNode():
            if val[self.i]=="null":
                self.i+=1
                return None
            node =TreeNode(int(val[self.i]))
            self.i+=1
            node.left=CreateNode()
            node.right=CreateNode()
            
            return node
        
        return CreateNode()
        # CreateNode()
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))