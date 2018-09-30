from comparable import Comparable
from date import Date

class Person(Comparable):
    """
    This class is immutable and inherits from Comparable
    It uses composition by having a Date object for birthday
    Please code this using private instance variables.
    Each instance variable should have a getter, but no setters
    Code the compare method, and call the base class compare
    Code a __str__ method
    """

    def __init__(self, name, year, month, day):
        super().__init__()
        self.__name = name
        self.__birthday = Date(year, month, day)

    def get_name(self):
        return self.__name

    def get_birthday(self):
        return self.__birthday

    def compare(self, other_person):
        this_birthday = str(self.get_birthday())
        this_year, this_month, this_day = this_birthday.split('-')
        this_year, this_month, this_day = int(this_year), int(this_month), int(this_day)
        this_name = self.get_name()
        other_birthday = str(other_person.get_birthday())
        other_year, other_month, other_day = other_birthday.split('-')
        other_year, other_month, other_day = int(other_year), int(other_month), int(other_day)
        other_name = other_person.get_name()
        Comparable.compare(other_person)

        if this_year > other_year:
            return 1
        elif this_year == other_year:
            if this_month > other_month:
                return 1
            elif this_month == other_month:
                if this_day > other_day:
                    return 1
                elif this_day == other_day:
                    if this_name > other_name:
                        return 1
                    elif this_name < other_name:
                        return -1
                    else:
                        return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1


    def __str__(self):
        return self.__name + " " + str(self.__birthday)
