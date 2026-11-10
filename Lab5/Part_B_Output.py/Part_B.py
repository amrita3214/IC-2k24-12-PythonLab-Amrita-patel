
# Part B: predict the output

# Q1. Directory Aliasing
d = {"a": 1, "b": 2}
d2 = d
d2["c"] = 3
print("Q1:",len(d))
#Output: 3
#Explaination: Both variables refer to the same dictionary.

# Q2. Shallow copy
d = {"x": [1]}
e = d.copy()
e["x"].append(2)
print("Q2:",d)
#Output: {'x': [1, 2]}
#Explaination: Shallow copy shares the nested list.

#Q3. Dictionary comprehension
print({"Q3;',k: v for k, v in zip("abc", range(3)) if v})
#Output: {'b': 1, 'c': 2}
#Explaination: Zero is considered False, so the first item is removed.

#Q4. setdefault()
d = {"a": 1}
print("Q4:",d.setdefault("a", 9), d.setdefault("b", 5), d)
#Output: 1 5 {'a': 1, 'b': 5}
#Explaination: setdefault() adds a key only if it does not already exist.

#Q5. Equivalent Dictionary Keys
d = {1: "a", 1.0: "b", True: "c"}
print("Q5:",d, len(d))
#Output: {1: 'c'} 1
#Explaination: In Python, 1, 1.0 and True are equal dictionary keys and have the same hash.

#Q6. Deleting During Itreation
d = {"a": 1, "b": 2, "c": 3}
for k in d:
    if d[k] == 2:
        del d[k]
#Output: RuntimeError: dictionary changed size during iteration
#Explaination: We cannot safely delete dictionary keys while directly iterating over the dictionary.
       
#Q7. pop() and popitem()
d = {"a": 1, "b": 2}
print("Q7:",.pop("z", None), d.popitem())
#Output: None ('b', 2)
#Explaination: pop("z", None) returns None because the key does not exist.
#popitem() removes the last inserted item.

#Q8. Dictionary Comprehension with Duplicate Values
print({"Q8:", v: k for k, v in {"a": 1, "b": 1}.items()})
#Output: {1: 'b'}
#Explaination: Both values are 1. The second key overwrites the first key in the new dictionary.       





     
