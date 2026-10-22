# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # given sorted LL --> insert a new node into sorted LL

        # if multiple places --> insert somewhere --> first valid place, we can insert

        # Traverse LL
            # current node < new_node
            # after node > new_node
        
        new_node = Node(insertVal)
        curr = head
        visit = set()

        if not head:
            new_node.next = new_node
            return new_node
        
        while curr not in visit:
            if curr.val <= insertVal <= curr.next.val:
                temp = curr.next
                curr.next = new_node
                new_node.next = temp
                return head
            elif curr.val > curr.next.val and (insertVal >= curr.val or insertVal <= curr.next.val):
                temp = curr.next
                curr.next = new_node
                new_node.next = temp
                return head
            
            visit.add(curr)
            curr = curr.next
        
        temp = head.next
        head.next = new_node
        new_node.next = temp

        return head
        

        

            



