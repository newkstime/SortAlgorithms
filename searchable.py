from abc import ABC, abstractmethod

class Searchable(ABC):
    """
    This class only has an abstract method: search
    The search method takes a function object and a search object
    It uses pass for its implementation
    """
    @abstractmethod
    def search(obj_list, search_obj):
        pass
