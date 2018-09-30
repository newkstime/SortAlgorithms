from comparable import Comparable

class Date(Comparable):
    """
    This class is immutable and inherits from Comparable
    Please code this using private instance variables.
    Each instance variable should have a getter, but no setters
    Code the compare method, but do not call the base class compare
    Code a __str__ method
    """

    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day

    def get_month(self):
        return self.__month

    def get_day(self):
        return self.__day

    def get_year(self):
        return self.__year

    def compare(self, other_date):
        self.__this_date = Date(self.__year, self.__month, self.__day)
        if self.__this_date.__year > other_date.__year:
            return 1
        elif self.__this_date.__year == other_date.__year:
            if self.__this_date.__month > other_date.__month:
                return 1
            elif self.__this_date.__month == other_date.__month:
                if self.__this_date.__day > other_date.__day:
                    return 1
                elif self.__this_date.__day == other_date.__day:
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1

    def __str__(self):
        return str(self.__year + "-"+ self.__month + "-" + self.__day)
