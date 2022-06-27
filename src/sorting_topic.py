def selection_sort(collection):
    sorted_collection = []
    for _ in range(len(collection)):
        current_smallest = collection[0]
        for element in collection:
            if element < current_smallest:
                current_smallest = element
        collection.remove(current_smallest)
        sorted_collection.append(current_smallest)
    return sorted_collection


def insertion_sort(collection):
    sorted_collection = []
    for element in collection:
        i = 0
        # Scan sorted collection to find insertion spot
        while i < len(sorted_collection) and sorted_collection[i] < element:
            i += 1
        sorted_collection.insert(i, element)
    return sorted_collection


def bubble_sort(collection):
    collection = collection[:]
    for j in range(len(collection)):
        for i in range(len(collection) - 1 - j):
            if collection[i] > collection[i + 1]:
                collection[i], collection[i + 1] = collection[i + 1], collection[i]
    return collection


def bubble_sort_improved(collection):
    collection = collection[:]
    has_swapped = True
    complete_cells = 0
    while has_swapped:
        has_swapped = False
        for i in range(len(collection) - 1 - complete_cells):
            if collection[i] > collection[i + 1]:
                collection[i], collection[i + 1] = collection[i + 1], collection[i]
                has_swapped = True
        complete_cells += 1
    return collection
