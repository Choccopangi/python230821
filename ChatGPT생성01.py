# ChatGPT 질문: 파이썬의 list, tuple, set, dict의 장점과 단점을 비교하는 코드를 작성해줘

def compare_data_structures():
    # Lists
    list_pros = ["Ordered", "Mutable", "Allows duplicate elements"]
    list_cons = ["Slower for large datasets due to dynamic resizing"]

    # Tuples
    tuple_pros = ["Ordered", "Immutable", "Faster than lists for iteration and access"]
    tuple_cons = ["Cannot be modified once created"]

    # Sets
    set_pros = ["Unordered", "Mutable (addition/removal of elements)", "Fast membership testing"]
    set_cons = ["Cannot have duplicate elements", "No indexing"]

    # Dictionaries
    dict_pros = ["Key-value pairs", "Fast lookup using keys", "Flexible keys and values"]
    dict_cons = ["Unordered (in Python versions before 3.7)", "Keys must be unique", "Memory overhead for large dictionaries"]

    print("List:")
    print("Pros:", ", ".join(list_pros))
    print("Cons:", ", ".join(list_cons))
    print()

    print("Tuple:")
    print("Pros:", ", ".join(tuple_pros))
    print("Cons:", ", ".join(tuple_cons))
    print()

    print("Set:")
    print("Pros:", ", ".join(set_pros))
    print("Cons:", ", ".join(set_cons))
    print()

    print("Dictionary:")
    print("Pros:", ", ".join(dict_pros))
    print("Cons:", ", ".join(dict_cons))
    print()

compare_data_structures()
