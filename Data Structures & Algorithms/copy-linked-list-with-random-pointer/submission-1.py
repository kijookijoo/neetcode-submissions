"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        clone = {}

        def deep_copy(node):
            if node in clone:
                return clone[node]
            if node is None:
                return None
            
            new_node = Node(node.val)
            clone[node] = new_node
            new_node.next = clone[node.next] if node.next in clone else deep_copy(node.next)
            new_node.random = clone[node.random] if node.random in clone else deep_copy(node.random)
            
            return clone[node]
        
        return deep_copy(head)


