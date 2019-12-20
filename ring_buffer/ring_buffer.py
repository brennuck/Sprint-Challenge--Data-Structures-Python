from doubly_linked_list import DoublyLinkedList
# !! go over this when you can think !!

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # add elements till capacity is reached
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        elif self.storage.length == self.capacity:
            to_delete = self.storage.head
            self.storage.remove_from_head() # removes front of DLL
            self.storage.add_to_tail(item) # Add new item to back of DLL
            if to_delete == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        initial_node = self.current
        list_buffer_contents.append(initial_node.value)

        if initial_node.next is not None:
            next_node = initial_node.next
        else:
            next_node = self.storage.head

        while next_node != initial_node:
            list_buffer_contents.append(next_node.value)
            if next_node.next is not None:
                next_node = next_node.next
            else:
                next_node = self.storage.head
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
