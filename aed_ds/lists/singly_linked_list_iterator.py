from aed_ds.adt_iterator import Iterator
from ..exceptions import NoSuchElementException


class SinglyLinkedListIterator(Iterator):

    def __init__(self, head):
        self.head = head
        self.current_node = None

    def has_next(self) -> bool:
        if self.head is not None:
            if self.current_node == None:
                if self.head is not None:
                    return True
                else:
                    return False
            else:
                if self.current_node.get_next_node() is not None:
                    return True
                return False

    def get_next(self) -> object:
        if self.head is None:
            raise NoSuchElementException()
        else:
            if self.current_node is None:
                self.current_node = self.head
                return self.current_node.get_element()
            if self.current_node.get_next_node() is not None:
                self.current_node = self.current_node.get_next_node()
                return self.current_node.get_element()
            else:
                raise NoSuchElementException()

    def rewind(self) -> None:
        self.current_node = None
