from comparable import Comparable
from personList import PersonList
from person import Person
from sort_search_funcs import *

def main():

    sort_list = [selection_sort, insertion_sort, quick_sort, merge_sort, heap_sort]
    #Sort the 32 element files
    for sort in sort_list:
        p_list = PersonList()
        p_list.populate("Person32.csv")
        p_list.sort(sort)
    
        print("Sorting 32 file " + p_list.name + " using " + p_list.func_name)
        print("The number of compares are", Comparable.get_num_compares())
        print()
        print("The sorted list is: ")
        print("==================================")
        print(p_list)
        Comparable.clear_compares()

    #Random list sorts
    print("Sorting the 4 different sized random Person files")
    print("==================================")
    print()
    random_lists = ["Person1Ka.csv", "Person2Ka.csv", "Person4Ka.csv", "Person8Ka.csv"]

    for sort in sort_list:
        size = 1
        for list in random_lists:
            p_list = PersonList()
            p_list.populate(list)
            p_list.sort(sort)
            print("Sorting " + str(size) + "K file " + p_list.name + " using " + p_list.func_name)
            print("The number of compares are", Comparable.get_num_compares())
            print()
            Comparable.clear_compares()
            size += size

    #Sorted list sorts
    print("Sorting the 4 different sized sorted Person files")
    print("==================================")
    print()
    random_lists = ["Person1Kb.csv", "Person2Kb.csv", "Person4Kb.csv", "Person8Kb.csv"]

    for sort in sort_list:
        size = 1
        for list in random_lists:
            p_list = PersonList()
            p_list.populate(list)
            p_list.sort(sort)
            print("Sorting " + str(size) + "K file " + p_list.name + " using " + p_list.func_name)
            print("The number of compares are", Comparable.get_num_compares())
            print()
            Comparable.clear_compares()
            size += size

#Reverse list sorts

    print("Sorting the 4 different sized reverse sorted Person files")
    print("==================================")
    print()
    random_lists = ["Person1Kc.csv", "Person2Kc.csv", "Person4Kc.csv", "Person8Kc.csv"]

    for sort in sort_list:
        size = 1
        for list in random_lists:
            p_list = PersonList()
            p_list.populate(list)
            p_list.sort(sort)
            print("Sorting " + str(size) + "K file " + p_list.name + " using " + p_list.func_name)
            print("The number of compares are", Comparable.get_num_compares())
            print()
            Comparable.clear_compares()
            size += size
main()    
