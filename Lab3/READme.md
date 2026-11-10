
# Algorithm Efficiency

**Name:** Amrita Patel  
**Roll Number:** IC-2k24-12
**Course:** MCA 3rd Year  
**College:** IIPS, DAVV, Indore

---
## Section A: Before You Start

### Q1. What makes code faster if it produces the same output?

Code can run faster when we use an efficient algorithm and avoid unnecessary calculations. Proper use of loops, functions, and data structures also improves performance.

### Q2. Name a Python function or technique that avoids repeating work.

Functions help us avoid repeating the same code. We can write a block of code once and call it whenever required. This makes the program shorter, cleaner, and easier to understand.

---

# Section B: Problem 1 – Sum of All Primes Below N

## Step 1: Naive Version

**File:** `prime_naive.py`

This program checks every number from 2 to N-1. It tests all possible divisors to determine whether a number is prime.

### Test Cases

| Input N | Expected Output |
|---|---:|
| 10 | 17 |
| 2 | 0 |
| 3 | 2 |
| 20 | 77 |
| 100 | 1060 |
| 50000 | 68143852 |
| 500000 | 6425722268 |
| 2000000 | 142913828922 |

### Q3. What did you observe?

The execution time increased significantly when N increased. The naive method checks many divisors for every number, so it requires a large number of calculations.

**Timing:**
- N = 50,000: __________ seconds
- N = 2,000,000: __________ seconds

## Step 2: Smaller Bound Approach

**File:** `prime_smaller_bound.py`

This approach checks divisors only up to the square root of a number. It reduces unnecessary calculations and improves execution speed.

**Expected Output for N = 2,000,000:**

142913828922

### Q4. How much faster was this compared to Step 1?

The smaller bound approach is much faster than the naive approach because it checks fewer divisors. However, it still checks each number separately, so it can be improved further.

**Timing for N = 2,000,000:** __________ seconds

## Step 3: Sieve of Eratosthenes

**File:** `prime_sieve.py`

### Core Idea

The Sieve of Eratosthenes is an efficient method for finding prime numbers. First, we assume that all numbers are prime. Then we mark multiples of each prime number as non-prime. The remaining unmarked numbers are prime.

**Expected Output for N = 2,000,000:**

142913828922

**Timing for N = 2,000,000:** __________ seconds

### Q5. Compare all three times

| Method | Time Taken |
|---|---|
| Naive | __________ seconds |
| Smaller Bound | __________ seconds |
| Sieve | __________ seconds |

### Q6. Which change gave the biggest jump in speed?

The Sieve of Eratosthenes gave the biggest improvement in speed. Instead of checking every number separately, it identifies prime numbers together by marking their multiples. This avoids repeated calculations and makes the program more efficient.

---

## How to Run the Programs

1. Open Python IDLE.
2. Open the required Python file.
3. Press F5 to run the program.
4. Enter the input when requested.
5. Check the output.

## Technologies Used

- Python
- Python IDLE
- GitHub
