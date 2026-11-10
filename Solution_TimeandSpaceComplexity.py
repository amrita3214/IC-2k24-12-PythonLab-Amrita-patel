
Activity: Find the Time and Space Complexity
For each snippet, write the time complexity and space complexity using Big-O notation, and justify your answer in one line.

Snippet 1
def find_max(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

Time complexity: O(n) Space complexity: O(1) Justify: We have one single for loop that goes through all the elements in one go, which means that our time complexity will increase linearly with respect to the input size of array. The number of additional variables being used is one

Snippet 2
def has_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

Time complexity: O(n²) Space Complexity: O(1).  Justify: The inner loop runs the entire array once more for each iteration of the outer loop, which means there is a loop within a loop, giving us the typical O(n²) complexity. No new data structures are used, making space complexity constant



Snippet 3
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

Time complexity: O(log n) Space: O(log n) Justify:  Each recursive function reduces the value of n by one digit because the division process reduces the value of n to n/10, which results in reducing the number of recursions to log n. Since the function is recursive, its stack depth and space both become O(log n)

Snippet 4
def print_pairs(arr):
    n = len(arr)
    result = []
    for i in range(n):
        for j in range(n):
            result.append((arr[i], arr[j]))
    return result

Time complexity: O(n²), Space O(n²) Justify: Nested loops iterating over the whole array would ensure that all pairs are covered, i.e., n * n work is done here. Also, since we’re storing all pairs in result, space complexity would be O(n²).

Snippet 5
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

Time complexity:O(log n) Space: O(1) Justify: With each loop, we halve the range of search and therefore find our solution after only log n loops rather than looping through all of the elements. Our algorithm requires very little memory, using only a few parameters like (low, high, mid).


Snippet 6
def matrix_multiply(a, b):
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result

Time complexity: O(n³) Space: O(n²) Justify:The three for loops which run n number of times give rise to n×n×n operations, which is why it is cubed. The matrix in the output requires space of n², which is the maximum storage required.

Snippet 7
def to_sparse(matrix):
    triples = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] != 0:
                triples.append((r, c, matrix[r][c]))
    return triples

Time complexity (in terms of matrix dimensions m and n): O(m·n) Space: O(k). Justify: We have to check every single cell in the matrix once to see if it's non-zero, and the matrix has m rows and n columns, so that's m×n checks no matter what. But we only actually store something when we find a non-zero value, so the space used depends on k, the number of non-zero entries, not the full matrix size.












Snippet 8
def process(arr):
    n = len(arr)
    for i in range(n):
        print(arr[i])
    for j in range(n):
        for k in range(n):
            print(arr[j], arr[k])

Time complexity: O(n²) Justify:Even though the first one is O(n), the second one has two loops nested inside it, making it O(n²). When we combine O(n) and O(n²), the result becomes O(n²).

Snippet 9
def check_first_ten(arr):
    for i in range(len(arr)):
        for j in range(10):
            if arr[i] == j:
                return True
    return False

Time complexity: O(n) Explanation: The inner for-loop always iterates 10 times regardless of the size of the array – which makes it a constant time operation. The total time complexity therefore only comes from the outer for-loop which leads to O(n).
Snippet 10
def reverse_new(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

Time complexity:O(n) Space: O(n) Justify: We iterate through the array only once, adding each element to a new list, making the time complexity increase linearly with n. Since we are creating a new list from scratch and not using the old one, space complexity increases linearly as well.


Snippet 11
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

Time complexity:O(n) Space: O(1) Justify: The two pointers move toward each other and together they cover the whole array once, so it's linear time. We're swapping elements directly inside the original array instead of creating a new one, so no extra space is needed beyond a couple of temp variables.

Snippet 12
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

Time complexity:O(n) Space: O(n) Justify: This function calls itself once per value of n to 1. Hence, this will take n calls in total, which means that the algorithm will have linear runtime. Moreover, as all these recursive calls remain in the call stack until the previous recursive call finishes, then the space complexity of this algorithm will be O(n).

Snippet 13
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

Time complexity:O(2ⁿ) Space: O(n) Justify: The branching occurs in two additional calls except for the base case scenarios, and the doubling continues indefinitely, thus making the number of calls grow in an exponential fashion. Although the function splits frequently, in each instance there will be only one call along that line of branching which is active on the stack. Therefore, the memory usage is linearly dependent on n.

Snippet 14
def count_pairs_with_sum(arr, target):
    seen = set()
    count = 0
    for num in arr:
        if target - num in seen:
            count += 1
        seen.add(num)
    return count

Time complexity:O(n) Space: O(n) Justify: We only loop through the array once, and checking/adding to a set takes constant time on average, so overall it's linear. The seen set can end up holding up to n elements in the worst case, so space grows linearly too.

Snippet 15
def print_all_subsets(arr):
    n = len(arr)
    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        print(subset)

Time complexity: O(n·2ⁿ) Justify: There can be a total of 2ⁿ subsets of an array of size n, and for each subset, an inner loop runs in O(n) time to create that subset, resulting in n·2ⁿ.

Snippet 16
def merge_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

Time complexity:O(n + m) Space: O(n + m)  Justify: We iterate through array a and b one time each, comparing elements along the way, hence the amount of time it takes is dependent on the sum of both. We also create a resultant list consisting of all elements in both arrays, hence the space complexity will be the same.
Snippet 17
def is_palindrome(s):
    return s == s[::-1]

Time complexity: O(n) Space: O(n) Justify: Reversing a string with slicing has to look at every character once, so that's linear time. It also creates a brand-new reversed string in memory rather than modifying in place, so that's linear space too.
Snippet 18
def flatten(matrix):
    flat = []
    for row in matrix:
        for val in row:
            flat.append(val)
    return flat

Time complexity (in terms of m rows and n columns):O(m·n) Space: O(m·n) Justify: We iterate through each and every value in each and every row, which means there are a total of m×n values with m rows and n columns, so time will be based on both of them together. And we’re creating a list by copying all of these values, so space will also be m×n.








Snippet 19
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

Time complexity:O(n) Space: O(n) Justify: As the function continues to call itself, exp is continually reduced by 1 until exp = 0; therefore, n calls are made and it runs in linear time. As each call to the function is waiting in the stack for the previous call to complete, stack depth is O(n).
Snippet 20
def fast_power(base, exp):
    if exp == 0:
        return 1
    half = fast_power(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    return half * half * base

Time complexity:O(log n) Space: O(log n) Justify: In this case, instead of decreasing the exponent by one at each step, it decreases it by a factor of two, requiring significantly fewer iterations, in the order of log n. As it is a recursive algorithm, its space complexity equals the depth of the recursion stack, which is the number of iterations.
Snippet 21
def has_common_element(a, b):
    for x in a:
        for y in b:
            if x == y:
                return True
    return False

Time complexity (in terms of the sizes of a and b): O(n·m) Space: O(1) justify : For each item in a, there could be a full scan of all items in b, resulting in n*m comparisons in the worst-case scenario where no matching item is found. There are no other data structures that are created apart from the loop variables.

Snippet 22
def build_frequency_map(arr):
    freq = {}
    for val in arr:
        freq[val] = freq.get(val, 0) + 1
    return freq

Time complexity: O(n) Space: O(n)  Justify:  We scan the array just once, and each dictionary operation (get, set) has a constant time complexity on average. Hence, the algorithm has a linear time complexity in general. However, the space complexity may be linear in the worst-case scenario where all the elements in the array are unique.
