class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        nodes = [0] + [-1 for i in range(n)]
        # there used to be n nodes with n - 1 edges -> initialize each node to be root of itself

        # [-1,-1,-1]
        # merge node 0 and 1 -> [1,-1,-1]
        
        # [1,-1,-1]
        # merge node 1 and 2 -> 

        def find_parent(x):
            if nodes[x] == -1:
                return x

            return find_parent(nodes[x])
        
        # merges nodes x and y (y is attached under root of x) and the new root (x) is returned
        def merge(x, y):
            px, py = find_parent(x), find_parent(y)
            nodes[py] = px
        
        for a,b in edges:
            pa, pb = find_parent(a), find_parent(b)
            if pa == pb:
                return [a,b]
            merge(pa, pb)



        