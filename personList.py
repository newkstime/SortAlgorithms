import csv
from person import Person
from sortable import Sortable
from searchable import Searchable

class PersonList(list, Sortable, Searchable):
    """
    This class has no instance variables.
    The list data is held in the parent list class object
    The constructor must call the list constructor: See Tower 
    Code a populate method, which reads the CSV file.
       It must use: try / except, csv.reader, with open
    Code the sort method: Must accept a function object
    Code the search method: Must accept function and search objects
    Code a __str__ method: Look at Tower for help
    You may want to code a person_at method for debug purposes.
    This takes an index and returns the Person at that location.
    """ 

    def __init__(self):
        super().__init__()
        self.__list = []
        self.name = ""
        self.func_name = ""

    def person_at(self, index):
        return self.__list[index]

    def populate(self, filename):
        try:
            with open(filename, 'r') as input_file:
                reader = csv.reader(input_file)
                person_list = list(reader)
                for item in person_list:
                    person = Person(item[0], item[3], item[1], item[2])
                    self.__list.append(person)

        except IOError:
            print("File Open Error.")
        self.name = filename

    def sort(self, func):
        func(self.__list)
        self.func_name = func.__name__

    def search(self, func, person):
        self.__person = person
        result = func(self.__list, self.__person)
        return result

    def __str__(self):
        printed_list = ""
        for p in self.__list:
            person = str(p)
            printed_list += person + "\n"
        return printed_list

