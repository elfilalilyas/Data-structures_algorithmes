# ---------------------------------- 1/ Singly linked list

class Node:
    '''Represents a node in a singly linked list.

        Each node stores data and a reference to the next node in the list.

        Attributes:
            data: The data to be stored in the node.
            next: A reference to the next node in the list (or None if this is the last node).
    '''
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"<Node data: {self.data}>"

class SLinkedList:
    '''Represents a singly linked list.
        The singly linked list allows for dynamic addition, removal, and traversal of nodes.
        head: The first node in the linked list (or None if the list is empty).
    '''
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        """
        Time complexity of this method is O(1)
        Return: True if the linkedlist is empty
        """
        return self.head is None

    def length(self):
        """
        Time complexity of O(n): This method iterates through the entire linked list, counting of nodes
        until it reaches the end( when current(the next_node of the last node) becomes None)
        Returns the length of the linkedlist
        """
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.next
        return size

    # Adding data to the linkedlist
    def add_node(self, node_data):
        """
        Role:
            This method adds a new node at the head of the linkedlist, so each time the head is updated.
        Time complexity of O(1):
            -this method creates a new node which is a constant-time operation
            because it only involves assigning values to two variables (data and next) in the Node class.
            -this method also updates the head of the linked list to point to this newly created node.
            which is another constant-time operation because it only requires reassigning the head pointer.
        Returns:
            nothing. It just adds nodes the linkedlist
        """
        # node = Node(node_data)
        # node.next = self.head
        # self.head = node
        node = Node(node_data, self.head)
        self.head = node

    def insert_at_beginning(self, node_data):
        # The same functionality with add_node() method
        self.add_node(node_data)

    def insert_at_end(self, node_data):
        """
        Role:
            Adds a new node to the end of the linked list.
        Time complexity of O(n):
            - create new node     ---> O(1)
            - the method needs to traverse through the entire linkedlist to find
              the last node. This traversal involves visiting each node until
              the end of the list, which takes O(n) time
            - insertion operation ---> O(1)
        Returns:
            nothing.
        """
        node = Node(node_data)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def insert_at_index(self, data, index):
        """
        Role:
            Adds a new node to a given index of the linkedlist.
        Time complexity of O(n): in worst case.
            - Create new node     ---> O(1)
            - Checking for edge cases where the index is 0, -1, or equal to the
              length of the list is O(1).
            - If index is 0 it takes O(1)
            - In the worst case it needs to traverse through the entire linkedlist to find
              the last node. This traversal involves visiting each node iterates until it
              reaches the desired position, making it O(n) in the worst case.
            - Insertion operation ---> O(1)
        Returns:
            nothing.
        """
        if index == 0:
            self.insert_at_beginning(data)
            return
        if index == -1 or index == self.length() - 1:
            self.insert_at_end(data)
            return
        if index < 0 or index >= self.length():
            raise IndexError('Index out of range')
        position = 0
        current = self.head
        while position < index - 1:
            current = current.next
            position += 1
        prev_node = current
        next_node = current.next
        new_node = Node(data, next_node)
        prev_node.next = new_node

    def insert_after_data(self, after_data, new_data):
        """
        Role:
            Inserts a new node with the given `new_data` after the node with `after_data` data.
        Time complexity of O(n): in worst case.
            - Create new node     ---> O(1)
            - If after_data is the data of the head. it takes O(1)
            - In the worst case, this traversal involves examining each node
              until it finds the target data or reaches the end of the list,
              making it O(n).
            - Insertion operation ---> O(1)
            - Error Handling: as it involves completing the traversal to determine
              that after_data is not present. --> O(n)
        Returns:
            nothing.
        """
        current = self.head
        while current and current.data != after_data:
            current = current.next
        if current:
            new_node = Node(new_data, current.next)
            current.next = new_node
            return
        raise ValueError(f"{after_data} data not found!")

    def insert_values(self, data_list):
        # needs some tricks

        # #1 create a new linked_list
        # new_linkedlist = SLinkedList()
        # for data in data_list:
        #     new_linkedlist.insert_at_end(data)
        #
        # return new_linkedlist

        # #2 delete the old data of the linkedlist and fill it with new data
        # self.head = None                         # this line deletes the old data of the linkedlist
        # for data in data_list:
        #     self.insert_at_end(data)
        #     # self.insert_at_beginning(data_list[index])

        #3 add a list of data to the linkedlist
        for data in data_list:
            self.add_node(data)

    def search_node(self, index):
        """
        Role:
            Retrieves the node at the specified index in the linked list.
        Time complexity of O(n): in worst case.
            - Index Validation    ---> O(1)
            - Error Handling      ---> O(1)
            - If the index is valid, the method traverses the linked list to
              reach the node at the specified index. This involves iterating
              through the list from the head node up to the desired position.
              In the worst case, this requires visiting each node up to
              the index, making it O(n)
        Returns:
            the data of the node at the given index ---> O(1)
        """
        current = self.head
        if index == 0:
            return current
        # to be similar to arrays
        if -self.length() < index < 0:
            index = self.length() + index
        if index < -self.length() or index > self.length() - 1:
            raise IndexError('Index out of range!')
        position = 0
        while position < index:
            current = current.next
            position += 1
        return current

    def search_data(self, data, appearance=1):
        """
        Role:
             Searches for the 'appearance'th occurrence of 'data' in the linked list.
        Time complexity of O(n):
          Best Case O(1):
            -If the data appears at the very beginning of the
             linkedlist and it matches the required occurrence, the function will
             return early after only a few iterations.
          Worst case O(n).
            -In the worst case, the method needs to traverse the entire linkedlist
             to either find the required occurrence of the data or determine that
             it does not exist in the specified number of occurrences.
        Returns:
            -The index of the data if it found
            -Error if data not found at the linkedlist or if the number
             of occurrences of 'data' is less than 'appearance'.
        """
        current = self.head
        if not current:
            raise KeyError(f"No data yet to search!")
        appearances = 0
        index = 0
        while current:
            if current.data == data:
                appearances += 1
                if appearance == appearances:
                    return index
            current = current.next
            index += 1
        raise KeyError(f"data '{data}' appears only {appearances} time" if appearances > 0 else f"No data '{data}' found!")

        # index = -1
        # while appearances != appearance and current.next:
        #     if current.data == data:
        #         appearances += 1
        #     current = current.next
        #     index += 1
        # if not current.next:
        #     if current.data == data:
        #         return index + 1
        #     else:
        #         if appearances == 0:
        #             raise KeyError(f"No data {data} found!")
        #         else:
        #             raise KeyError(f"data {data} appears only {appearances} time")
        # else:
        #     return index

    def remove_at_index(self, index):
        """
        Role:
            Removes the node at the specified index from the linked list.
        Time complexity of O(n): in worst case.
          Best Case O(1): If index is 0, meaning we are removing the head
             of the list, the operation is performed in constant time.
          Worst Case (O(n)): If the node to be removed is at the end of the
             linkedlist, the method will need to traverse the entire list, resulting
             in linear time complexity relative to the length of the list.
        Returns:
            The data at the specific index(data removed)
        """
        if index == 0:
            self.head = self.head.next
            return
        if index < -self.length() or index > self.length() - 1:
            raise IndexError('Index out of range!')
        if -self.length() < index < 0:
            index = self.length() + index
        position = 0
        current = self.head
        while position < index - 1:
            current = current.next
            position += 1

        prev_node = current
        del_node = prev_node.next
        next_node = del_node.next
        prev_node.next = next_node
        return del_node, next_node

    def remove_data(self, data):
        """
        Role:
            Removes the first occurrence of a node with the specified data from the linked list.
        Time complexity of O(n): in worst case.
          Best Case O(1):
            -If the node to be removed is the head of the linkedlist
          Worst Case (O(n)):
            -If the node to be removed is not at the beginning and requires
             traversing the entire list to find the node
        Returns:
             -The data removed if it was found
             -Error if the data was not found
        """
        current = self.head
        if current.data == data:
            self.head = current.next
            return current

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current:
            prev.next = current.next
            return current
        else:
            raise ValueError(f'data {data} not found')

    def remove_at_start(self):
        """
        Role:
            Removes the first node (the head) in the linked list.
        Time complexity O(1):
            We remove the head and make the next node is the new head.
        Returns:
             Nothing.
        """
        self.head = self.head.next
    def remove_at_end(self):
        """
        Role:
            Removes the last data in the linked list.
        Time complexity of O(n):
            It requires traversing the entire list to find the last node and remove it.
        Returns:
            Nothing
        """
        current = self.head
        before_end = None
        while current.next:
            before_end = current
            current = current.next
        before_end.next = None

    def reverse_in_place(self):
        """
        Role:
            Reverse the original linkedlist.
        Time complexity of O(n):
            It requires traversing the entire linkedlist, for each node it makes
            the previous node the new next node
        Returns:
            The reversed linkedlist.
        """
        current = self.head
        prev = None
        while current:
            # we save the next node before we change it.
            head = current.next
            current.next = prev
            prev = current
            # we store the saved node in the current variable to keep
            # the flow of nodes clean and correct.
            current = head
        self.head = prev
        print(self)

    def new_reversed_list(self):
        """
        Role:
            Create another linkedlist to store the reverse of the linkedlist.
            The original linked list stays unchanged.
        Time complexity of O(n):
            It requires traversing the entire linkedlist, each time we add a node to
            the new linkedlist.
        Returns:
            The reversed linkedlist.
        """
        reverse_list = SLinkedList()
        current = self.head
        while current:
            reverse_list.add_node(current.data)
            current = current.next
        print(reverse_list)

    def __repr__(self):
        """
        Role:
            Provides a string representation of the linked list, including
            special indicators for the head and tail nodes.
        Time complexity of O(n):
            the method must traverse the entire list to construct the string
            representation, resulting in linear time complexity.
        Returns:
            a string representation of the linked list
        """
        if self.head is None:
            return 'None'

        linked_list = []
        current = self.head
        while current:
            if current == self.head:
                linked_list.append(f'[Head: {current.data}]')
            elif current.next is None:
                linked_list.append(f'[Tail: {current.data}]')
            else:
                linked_list.append(f'[{current.data}]')
            current = current.next

        return '-> '.join(linked_list) + '->'


if __name__ == '__main__':
    l = SLinkedList()
    l.add_node(5)
    # print(l.head)                           # printing the node (requires --repr--)
    # print(l.head.data)                      # printing the data of the node
    # print(l.head.next)                      # printing the next node of the data
    # l.add_node(7)
    # print(l)
    # l.insert_at_beginning(5)
    # print(l)
    # l.insert_at_end(3)
    # print(l)
    # l.insert_values([55, 56, 58])
    # print(l)
    # print('the length is: ', l.length())
    # removed_node = l.remove_at_index(2)
    # print(removed_node)
    # print(l)
    # l.remove_at_index(3)
    # print(l)
    # l.insert_at_index(100, 3)
    # print(l)
    # print(l.search_node(3))
    # print(l.search_data(5, 2))
    # removed_data = l.remove_data(3)
    # print(removed_data)
    # print(l)
    # # print(l.search_node(4))
    # # print(l.search_node(4).next)   # next of the tail
    # l.insert_after_data(5, 19)
    l.add_node(1)
    l.add_node(3)
    l.add_node(10)
    l.add_node(15)
    l.remove_at_end()
    # print(l.head.next)
    # l.insert_after_data(6, 8)
    # l.insert_at_end(11)
    # l.insert_at_end(13)
    # l.insert_at_index(0, 2)
    print(l)
    # print(l.reverse_linkedlist())
    # l.reverse_in_place()
    # print(l)
    # print(l.head)
    # print(l.remove_at_index(-2))
    # l.remove_data(55)
    # print(l)
    # print(l.search_data(7, 4))
    # print(l.search_node(-2))
    # print(l.length())

    # print(l.search_data(5))
    # x = l.remove_data(5)
    # print(x)
    # print(l)
    # print(l.head)
    # print(bool(l.head))
    # print('-'*30)

