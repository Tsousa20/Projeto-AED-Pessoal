from aed_ds.dictionaries.adt_dictionary import Dictionary
from aed_ds.exceptions import DuplicatedKeyException, NoSuchElementException
from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.dictionaries.item import Item
import ctypes


class OpenHashTable(Dictionary):
    def __init__(self, size=101):
        self.list_size = size
        self.num_elements = 0
        self.table_creator = (size * ctypes.py_object)()
        for i in range(self.list_size):
            self.table_creator[i] = SinglyLinkedList()

    def size(self):
        return self.num_elements

    def is_full(self):
        return self.num_elements == self.list_size

    def get(self, k: object):
        idx = 0
        while idx < self.size()+1:
            iterador = self.table_creator[idx].iterator()
            while iterador.has_next() == True:
                item = iterador.get_next()
                if item.get_key() == k:
                    return item.get_value()
            idx += 1
        raise NoSuchElementException()

    def update(self, k: object, v: object):
        self.get(k)
        idx = 0
        while idx < self.size()+1:
            iterador = self.table_creator[idx].iterator()
            while iterador.has_next() == True:
                item = iterador.get_next()
                if item.get_key() == k:
                    item.set_value(v)
            idx += 1

    def insert(self, k: object, v: object):
        idx = 0
        while idx < self.size():
            iterador = self.table_creator[idx].iterator()

            while iterador.has_next() == True:
                item = iterador.get_next()
                if item.get_key() == k:
                    raise DuplicatedKeyException()
            idx += 1
        new_item = Item(k, v)
        self.table_creator[idx].insert_first(new_item)
        self.num_elements += 1

    def remove(self, k: object):
        idx = 0
        while idx < self.size()+1+1:
            iterador = self.table_creator[idx].iterator()
            cnt = -1
            while iterador.has_next() == True:
                item = iterador.get_next()
                cnt = cnt+1
                if item.get_key() == k:
                    old_iteam = item.get_value()
                    self.table_creator[idx].remove(cnt)
                    self.num_elements -= 1
                    cnt = cnt-1
                    return old_iteam
            idx += 1
        raise NoSuchElementException()

    def keys(self):
        idx = 0
        key_list = SinglyLinkedList()
        while idx < self.size()+1:
            iterador = self.table_creator[idx].iterator()
            while iterador.has_next() == True:
                item = iterador.get_next()
                key_list.insert_last(item.get_key())
            idx += 1
        return key_list

    def values(self):
        idx = 0
        values_list = SinglyLinkedList()
        while idx <= self.size()+1:
            iterador = self.table_creator[idx].iterator()
            while iterador.has_next() == True:
                item = iterador.get_next()
                values_list.insert_last(item.get_value())
            idx += 1
        return values_list

    def items(self):
        idx = 0
        items_list = SinglyLinkedList()
        while idx <= self.size()+1:
            iterador = self.table_creator[idx].iterator()
            while iterador.has_next() == True:
                item = iterador.get_next()
                items_list.insert_last(item)
            idx += 1
        return items_list
