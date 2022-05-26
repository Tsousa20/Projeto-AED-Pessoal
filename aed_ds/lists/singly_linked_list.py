from .adt_list import List
from .nodes import SingleListNode
from aed_ds.exceptions import EmptyListException, InvalidPositionException, NoSuchElementException
from aed_ds.adt_iterator import Iterator
from aed_ds.lists.singly_linked_list_iterator import SinglyLinkedListIterator


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def is_empty(self) -> bool:
        if self.num_elements == 0:
            return True
        return False

    def size(self) -> int:
        return self.num_elements

    def get_first(self) -> object:
        if self.head == None:
            raise EmptyListException
        return self.head.get_element()

    def get_last(self) -> object:
        if self.head == None:
            raise EmptyListException
        return self.tail.get_element()

    def get(self, position: int) -> object:
        if self.head == None:
            raise EmptyListException()
        node = self.head
        idx = 0
        if position < 0 or position > self.size() - 1:
            raise InvalidPositionException
        while node:
            if idx == position:
                return node.get_element()
            node = node.get_next_node()
            idx += 1

    def find(self, element: object) -> bool:
        node = self.head
        idx = 0
        while node:
            if element == node.get_element():
                return idx
            node = node.get_next_node()
            idx += 1
        return -1

    def insert_first(self, element: object) -> None:
        node = SingleListNode(element, None)  # 2 4 3
        if self.head == None:
            self.tail = node
        else:
            node.set_next_node(self.head)
        self.head = node
        self.num_elements += 1

    def insert_last(self, element: object) -> None:
        node = SingleListNode(element, None)
        if self.tail is not None:
            self.tail.set_next_node(node)
        self.tail = node
        if self.head is None:
            self.head = self.tail
        self.num_elements += 1

    def insert(self, element: object, position: int) -> None:
        if position < 0 or position > self.size():
            raise InvalidPositionException()
        elif position == 0:
            return self.insert_first(element)
        elif position == self.size():
            return self.insert_last(element)
        prev_node = self.head
        cur_node = self.head
        idx = 0
        while prev_node:
            if position == idx:
                new_node = SingleListNode(element, cur_node)
                prev_node.set_next_node(new_node)
                self.num_elements += 1
                break
            prev_node = cur_node
            cur_node = cur_node.get_next_node()
            idx += 1

    def remove_first(self) -> object:
        if self.head is None:
            raise EmptyListException()
        elif self.head == self.tail:
            result = self.head.get_element()
            self.make_empty()
            return result
        else:
            old_head = self.head
            self.head = self.head.get_next_node()
            self.num_elements -= 1
            return old_head.get_element()

    def remove_last(self) -> object:
        if not self.head:
            raise EmptyListException()
        elif self.size() == 1:
            return self.remove_first()
        cur_node = self.head
        while cur_node.get_next_node().get_next_node() is not None:
            cur_node = cur_node.get_next_node()
        old_node = self.tail
        self.tail = cur_node
        cur_node.set_next_node(None)
        self.num_elements -= 1
        return old_node.get_element()

    def remove(self, position: int) -> object:
        if position < 0 or position > self.size() - 1:
            raise InvalidPositionException()
        elif position == 0:
            return self.remove_first()
        elif position == self.size() - 1:
            return self.remove_last()
        node = self.head
        idx = 0
        while node:
            if idx == position:
                prev_node.set_next_node(node.get_next_node())
                old_node = node
                node.set_next_node(None)
                self.num_elements -= 1
                return old_node.get_element()
            prev_node = node
            node = node.get_next_node()
            idx += 1

    def make_empty(self) -> None:
        self.head = None
        self.tail = None
        self.num_elements = 0

    def iterator(self) -> SinglyLinkedListIterator:
        return SinglyLinkedListIterator(self.head)

    # ###############################################################################
    # def sortList(self):
    #     current = self.head
    #     index = None
    #     if(self.head == None):
    #         return
    #     else:
    #         while(current != None):
    #             index = current.get_next_node()
    #             while(index != None):
    #                 if(current.get_element() > index.get_element()):
    #                     temp = current.get_element()
    #                     current.set_element(index.get_element())
    #                     index.set_element(temp.get_element())
    #                 index = index.get_next_node()
    #             current = current.get_next_node()
