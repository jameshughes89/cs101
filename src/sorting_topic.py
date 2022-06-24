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
