def bubble_sort(obj_list):

    for num in range(len(obj_list) - 1, 0, -1):
        for i in range(num):
            if obj_list[i].compare(obj_list[i+1]) == 1:
                temp = obj_list[i]
                obj_list[i], obj_list[i+1] = obj_list[i+1], obj_list[i]


def selection_sort(obj_list):

    for num in range(len(obj_list)):
        min = num
        for i in range(num + 1, len(obj_list)):
            if obj_list[min].compare(obj_list[i]) == 1:
                min = i

        obj_list[num], obj_list[min] = obj_list[min], obj_list[num]

def insertion_sort(obj_list):
    for num in range(1, len(obj_list)):
        key = obj_list[num]
        i = num - 1
        while i >= 0 and key.compare(obj_list[i]) == -1 :
                obj_list[i+1] = obj_list[i]
                i -= 1
        obj_list[i+1] = key


def quick_sort(obj_list):
    q_sort(obj_list, 0, len(obj_list) - 1)

def q_sort(obj_list, left, right):
    if left >= right:
        return
    if right - left == 1:
        if obj_list[left].compare(obj_list[right]) == 1:
            obj_list[left], obj_list[right] = obj_list[right], obj_list[left]
            return
    pivot = partition(obj_list, left, right)
    q_sort(obj_list, left, pivot - 1)
    q_sort(obj_list, pivot + 1, right)

def partition(obj_list, left, right):
    pivot = left + (right - left) // 2
    obj_list[left], obj_list[pivot] = obj_list[pivot], obj_list[left]
    pivot = left
    left += 1

    while right >= left:
        while left <= right and obj_list[left].compare(obj_list[pivot]) != 1:
            left += 1
        while left <= right and obj_list[right].compare(obj_list[pivot]) == 1:
            right -= 1
        if left <= right:
            obj_list[left], obj_list[right] = obj_list[right], obj_list[left]
            left += 1
            right -= 1
        else:
            break
    obj_list[pivot], obj_list[right] = obj_list[right], obj_list[pivot]
    return right


def merge_sort(obj_list):
    if len(obj_list)>1:
        mid = len(obj_list)//2
        lefthalf = obj_list[ :mid]
        righthalf = obj_list[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i].compare(righthalf[j]) == -1:
                obj_list[k]=lefthalf[i]
                i=i+1
            else:
                obj_list[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            obj_list[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            obj_list[k]=righthalf[j]
            j=j+1
            k=k+1

def heapify(obj_heap, size, root):
    largest = root
    left = (2 * root) + 1
    right = (2 * root) + 2

    if left < size and obj_heap[left].compare(obj_heap[root]) > 0:
        largest = left
    if right < size and obj_heap[right].compare(obj_heap[largest]) > 0:
        largest = right
    if largest != root:
        obj_heap[root], obj_heap[largest] = obj_heap[largest], obj_heap[root]
        heapify(obj_heap, size, largest)

def heap_sort(obj_list):
    size = len(obj_list)

    for i in range(size, -1, -1):
        heapify(obj_list, size, i)

    for i in range(size - 1, 0, -1):
        obj_list[0], obj_list[i] = obj_list[i], obj_list[0]
        heapify(obj_list, i, 0)

