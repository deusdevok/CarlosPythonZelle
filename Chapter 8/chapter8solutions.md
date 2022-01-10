# Chapter 8 - Review Questions

## True/False

1. False. `while` implements an indefinite loop.
2. True.
3. False. It uses a sentinel to break out of the loop.
4. True.
5. False. A `for` loop is handy to process a file.
6. False. A `while` loop is a __pre-test__ loop.
7. True.
8. True.
9. False. `not(a or b) == (not a) and (not b)` by De Morgan law.
10. True.

## Multiple Choice

1. a.
2. c.
3. d.
4. c.
5. c.
6. c.
7. d.
8. b.
9. c.
10. a.

## Discussion

1. Compare:
    
    a) A definite loop has a pre defined number executions (`for` loops for example). In an indefinite loop, the body executes repeatedly until the condition fails (`while` loops).

    b) A `for` loop is used in definite loops, and `while` loops are for indefinite loops.

    c) In an interactive loop, the user decides when the loop stops (for example via an input parameter). Sentinel loops keep executing until a special value (the __sentinel__) is reached.

    d) `end-of-file` loops uses `readline()`. When reaching the end of the file, it returns an empty string, which can be used as a sentinel value to end the corresponding loop.
	
2. Truth tables:

a)

P | Q | P and Q | not (P and Q)
:---:|:---:|:---:|:---:
T | T | T | F
T | F | F | T
F | T | F | T
F | F | F | T

b)

P | Q | not P | (not P) and Q
:---:|:---:|:---:|:---:
T | T | F | F
T | F | F | F
F | T | T | T
F | F | T | F

c)

P | Q | not P | not Q | (not P) or (not Q)
:---:|:---:|:---:|:---:|:---:
T | T | F | F | F
T | F | F | T | T
F | T | T | F | T
F | F | T | T | T

d)

P | Q | R | P and Q | (P and Q) or R
:---:|:---:|:---:|:---:|:---:
T | T | T | T | T
T | T | F | T | T
T | F | T | F | T
T | F | F | F | F
F | T | T | F | T
F | T | F | F | F
F | F | T | F | T
F | F | F | F | F

e)

P | Q | R | P or R | Q or R | (P or R) and (Q or R)
:---:|:---:|:---:|:---:|:---:|:---:
T | T | T | T | T | T
T | T | F | T | T | T
T | F | T | T | T | T
T | F | F | T | F | F
F | T | T | T | T | T
F | T | F | F | F | F
F | F | T | T | T | T
F | F | F | F | F | F

3. `while` loops:

a) 

```
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
```

b)

```
i = 1
sum = 0
while i <= 2*n-1:
    sum += i
    i += 2
```

c)

```
sum = 0
n = int(input('Enter a number: '))
while n != 999:
    sum += n
    n = int(input('Enter a number: '))
```

d)

```
times = 0
while n > 1:
    n = n/2
    times += 1
```