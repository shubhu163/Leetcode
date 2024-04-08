# Problem Statement: Problem Statement: Given the head of a singly linked list, write a program to reverse the linked list, and return the head pointer to the reversed list.
class Node:
    def __init__(self, data, next_node=None):
        self.data  = data
        self.next  = next_node
    
def reverse_linkedlist(head):
    temp = head
    prev = None

    while temp is not None:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev

def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=' ')
        temp = temp.next

if __name__ == '__main__':

    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(2)
    head.next.next.next = Node(4)

    # Print the original linked list
    print(" \n Original Linked List:")
    print_linked_list(head)

    # Reverse the linked list
    head = reverse_linkedlist(head)

    # Print the reversed linked list
    print("\n Reversed Linked List:")
    print_linked_list(head)



        

    






