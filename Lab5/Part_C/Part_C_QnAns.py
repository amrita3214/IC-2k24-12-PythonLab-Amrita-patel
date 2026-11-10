
Q1. Why does d2 = d not create a copy?
Ans:
d2 = d does not create a new dictionary. Both variables refer to the same dictionary in memory.
Difference:
d.copy() creates a shallow copy.
copy.deepcopy(d) creates a completely independent copy, including nested dictionaries and lists.
Example:
import copy

d = {"marks": {"Math": 90}}

d2 = d.copy()
d3 = copy.deepcopy(d)
For the student database, deepcopy() is better when we need a completely independent backup because the database contains nested dictionaries.


Q2. Why must dictionary keys be hashable?
Ans:
Dictionary keys must be hashable because Python uses their hash values to store and find data quickly.
Value
Can be a key?
[1, 2]
No
(1, 2)
Yes
{1, 2}
No
"12"
Yes
Lists and sets are mutable, so they cannot be dictionary keys.
Tuples and strings are hashable in these examples.


Q3. Difference between d[key], d.get(key) and d.get(key, default)?
Ans:
d[key]: Accesses a value directly. If the key does not exist, it gives KeyError.
d.get(key): Returns the value or None if the key does not exist.
d.get(key, default): Returns the value or a default value if the key does not exist.
Examples:
students[101]
students.get(105)
students.get(105, "Student not found")


Q4. Difference between .update() and assigning d[key] = value?
Ans:
update(): Adds multiple key-value pairs to a dictionary at once.
Assignment: Adds or changes one key-value pair.
Example:
d = {"a": 1}

d.update({"b": 2, "c": 3})

d["d"] = 4

print(d)
Output:
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
.update() is cleaner when adding multiple records together.


Q5. Why is creating a new dictionary with comprehension safer?
Ans:
Creating a new dictionary is safer because it does not change the original data.
Example:
new_salary = {
    k: v * 1.10
    for k, v in salary.items()
}
The original dictionary remains unchanged.
In-place modification is better when we intentionally want to update the original dictionary and do not need the old values.


Q6. Why does deleting keys while looping over a dictionary fail?
Ans:
Deleting keys changes the size of the dictionary during iteration. Python does not allow this because it can disturb iteration.
Two safe methods:
Method 1: Loop over a copied list of keys.
d = {"a": 1, "b": 2, "c": 3}

for k in list(d.keys()):
    if d[k] == 2:
        del d[k]

print(d)
Output:
{'a': 1, 'c': 3}
Method 2: Use dictionary comprehension.
d = {k: v for k, v in d.items() if v != 2}


Q7. How did you invert the book-to-member dictionary?
Ans:
In Q3, books store the member IDs who have borrowed them.
We create a new dictionary where member IDs become keys and book titles become values.
Example:
member_books = {}

for isbn, book in books.items():
    for member in book["issued_to"]:
        member_books.setdefault(member, []).append(book["title"])
Why use a list?
A member can borrow more than one book. Therefore, we use a list to store multiple book titles for one member.


Q8. What is the time complexity of dictionary lookup?
Ans:
Dictionary lookup usually takes O(1) time, which means constant time.
Searching through a list of records takes O(n) time because Python may need to check every record.
Example from Q5:
If we have 1000 contacts, searching for a phone number in a list may require checking many contacts.
Instead, we create a reverse dictionary:
reverse = {
    phone: name
    for name, c in contacts.items()
    for phone in c["phones"]
}
Now we can find the contact directly:
print(reverse.get("9988776655", "Not found"))
Output:
Manoj
This makes searching faster.
Important Python Dictionary Functions for Revision
Function
Use
get()
Access a value safely
keys()
Get all keys
values()
Get all values
items()
Get key-value pairs
update()
Add or update multiple values
pop()
Remove a specified key
popitem()
Remove last inserted item
setdefault()
Add key if it doesn't exist
copy()
Create shallow copy
clear()
Remove all items
sorted()
Sort dictionary data
max()
Find maximum value
len()
Count dictionary items
