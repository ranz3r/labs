def all_elements_true(tup):
    return all(tup)

tuple1 = (True, 1, "Hello", 5)  # All elements are truthy
tuple2 = (True, 0, "Hello")     # 0 is falsy, so it should return False

print(all_elements_true(tuple1))  # Output: True
print(all_elements_true(tuple2))  # Output: False
