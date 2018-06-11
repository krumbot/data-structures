# Linked List implementation


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_first(self, val):
        first_node = Node(val)
        first_node.next = self.head
        self.head = first_node

        return first_node

    def insert_after(self, prev_node, val):
        if prev_node is None:
            print("Cannot insert after a node of None type")
            return

        new_node = Node(val, prev_node.next)
        prev_node.next = new_node

        return new_node

    def insert_last(self, val):
        last_node = Node(val)

        loop_node = self.head
        if loop_node is None:
            self.head = last_node
        else:
            while loop_node.next is not None:
                loop_node = loop_node.next

            loop_node.next = last_node
        return last_node

    # Returns the nth node in the linked list with the given val
    def search(self, val, n=1):
        loop_node = self.head

        num_found = 0

        def validate_node(node, found):
            if node.val == val:
                found += 1
                if found == n:
                    return True, found
            return False, found

        while loop_node.next is not None:
            found_node, num_found = validate_node(loop_node, num_found)
            if found_node:
                return loop_node

            loop_node = loop_node.next

        found_node, num_found = validate_node(loop_node, num_found)
        if found_node:
            return loop_node

        return None

    def remove(self, node):
        if node is None:
            print("Please specify a node to remove from the Linked List.")
            return

        def remove_node(prev):
            if self.head == node:
                self.head = node.next
                return

            prev.next = node.next

        loop_node = self.head
        prev_node = None
        while loop_node.next is not None:
            if node == loop_node:
                remove_node(prev_node)
                return

            prev_node = loop_node
            loop_node = loop_node.next

        if node == loop_node:
            remove_node(prev_node)
