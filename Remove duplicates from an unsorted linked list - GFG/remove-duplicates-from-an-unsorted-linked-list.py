#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # # return head after editing list
        # val=[]
        # itr=head
        # #val.append(itr.data)
        # while itr and itr.next:
        #     if itr.data not in val:
        #         val.append(itr.data)
        #         prv=itr
        #         if itr.next:
        #             itr=itr.next
        #         #print("itr "+str(itr.data),"prv "+str(prv.data))
        #     else:
        #         if itr.next:
        #             itr=itr.next
        #             prv.next=itr
        #             #print("deb itr "+str(itr.data),"deb prv "+str(prv.data))
        #         else:
        #             itr=itr.next
        #             prv.next=itr
        #             #print("deb2 itr "+str(itr),"deb2 prv "+str(prv))
        #     #print(val)
        # return head
        l1=dict()
        itr=head
        while itr:
            if itr.data in l1.keys():
                prev.next=itr.next
                itr=itr.next
            else:
                prev=itr
                l1[itr.data]=0
                itr=itr.next
        return head

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # prints the elements of linked list starting with head
    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data,end=" ")
            curr_node=curr_node.next
        print(' ')
    
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        a.head = Solution().removeDuplicates(a.head)
        a.printList()
# } Driver Code Ends