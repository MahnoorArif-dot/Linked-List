class Node:
    def __init__(self, val=None):
        self.data = val
        self.next = None
        
class StackbyLinkList:
    def __init__(self):
        self.top = None
    def push(self,val):
        temp=self.top
        new_node=Node(val)
        new_node.next=temp
        self.top=new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            return popped_node.data
    def is_empty(self):
        if self.top is None:
            return True
        return False
    def peek(self):
        if self.top is None:
            return 'Stack is empty'
        return self.top.data
    def reverse_stack(self):
        prev = None
        current = self.top
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.top = prev
        
    def display(self):
        temp=self.top
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
        print()

if __name__ == "__main__":
    list1 = StackbyLinkList()
    list1.push(3)
    list1.push(2)
    list1.push(1)
    list1.push(4)
    list1.push(6)
    list1.display()
    #list1.pop()
    #list1.is_empty()
    #list1.peek()
    list1.reverse_stack()
    print("\nReversed Stack:")
    while not list1.is_empty():
        print(list1.pop(), end=" ")
