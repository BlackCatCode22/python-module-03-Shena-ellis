# CHAPTER 5 
## Loops & Iteration

### Repeated Steps

    n = 5
    while n > 0:
        print(n)
        n = n - 1
    print('BLASTOFF!')
    print(n)

5<br>
4<br>
3<br>
2<br>
1<br>
BLASTOFF<br>
0
------
### Infinite Loops 
#### Never Break the Cycle
    n = 5
    while n > 0:
        print('Lather')
        print'(Rinse')
    print('Dry Off!')


### Breaking Out of a Loop 
**This will repeat everything input by 
the user until the user types 'done'. 
   
     while True:
        line = input('<')
        if line == 'done':
            break
        print(line)
    print('Done!')


### Finishing an Iteration with Continue

- *This says: *print (repeat) user input. if line starts 
with a '#', don't repeat that line but continue. if line == 'done', 
break. print the line. print 'Done!'*
- This is a way to add comments in your terminal



    while True:
        line = input('>')
        if line[0] == '#':
            continue
        if line == 'done':
            break
        print(line)
    print('Done!')


## Indefinite Loops 

- Keep going until a logical condition becomes false.  

---
## Definite Loops

- Definite Loops **iterate** through the members of a set. 
- Execute an exact number of times

#### Simple Definite Loop
    
    for i in [5, 4, 3, 2, 1]:
        print(i)
    print('BLASTOFF!')

#### Definite Loop With Strings
    friends = ['Joseph', 'Jeff', 'Joe']
    for friend in friends:
        print('Happy New Years', friend)


## KEY TERMS

- The **iteration variable** "iterates" through the 
sequence *(ordered sets)*
- The **block (body)** of code is executed once for each 
value in he *sequence*
- The **iteration variable** Moves through all of the 
values in the sequence. 


---
## FINDING THE LARGEST VALUE

    largest_so_far = -1
    print('Before', largest_so_far)
    for the_num in [9, 41, 12, 3, 74, 15,]:
        if the_num > largest_so_far:
            largest_so_far = the_num
        print(largest_so_far, the_num)
   
    print('After', largest_so_far)

print('After', largest_so_far)

- We make a **variable** that contains 
the *largest value we have seen so far.* If the current
number we are looking at is larger, **it** is the new largest 
value we have seen so far.
- To get the smallest value, switch the **variable** name to **smallest_so_far** 
and switch the > to <

---
## COUNTING IN A LOOP

- To count how many times we execute a loop, we introduce a counter variable that 
starts at zero and we add one to it each time through the loop.


    zork = 0
    print('Before', zork)
    for thing in [9, 41, 12, 3, 74, 15]:
        zork = zork + 1
        print(zork, thing)
    print('After', zork)

>> ------------- 

    entries = 0
    print('Before', entries)
    for thing in [2, 4, 6, 8, 10]:
        entries = entries + 1
        print(entries, thing)
    print('After', entries)

---
## SUMMING IN A LOOP

    zork = 0
    print('Beforw', zork)
    for thing in [9, 41, 12, 3, 74, 15]:
        zork = zork + thing
        print(zork, thing)
    print('After', zork)

- **results read top to bottom, left to right**
  *(not right to left)*
---
## FINDING THE AVERAGE IN A LOOP 

- The **average** just combines the **counting** and **sum** 
patterns and divides when a loop is done. 
     

    count = 0
    sum = 0
    print('Before', count, sum)
    for value in [9, 41, 12, 3, 74, 15]:
        count = count + 1
        sum = sum + value
        print(count, sum, value)
    print('After', count, sum, sum / count)
---


## FILTERING IN A LOOP

- We use an **if** statement in the loop to catch/filter 
the *values* we are looking for. 

    
    print('Before')
    for value in [9, 41, 12, 3, 74, 15]:
        if value > 20:
            print('Large number', value)
    print('FILTERING')

----

## SEARCH USING A BOOLEAN VARIABLE

- If we just want to search and know if a value is found, we use
a variable that starts at false and is set to true as soon as we find 
what we are looking for. 


    found = False
    print('Before', found)
    for value in [9, 41, 12, 3, 74, 15]:
        if value == 3:
            found = True
        print(found, value)
    print('SEARCH USING BOOLEAN VARIABLE', found)
----

## THE **is** AND **is not** OPERATORS

- Implies *"is the same as"*
- Similar to, but stronger than ==
- *"is not"* also is a logical operator 


    smallest = None
    print('Before')
    for value in [3, 41, 12, 9, 74, 15]:
        if smallest is None:
            smallest = value
        elif value < smallest:
            smallest = value
        print(smallest, value)
    
    print('IS OPERATOR - SMALLEST', smallest)
---
< ------------------------------------------------------->

---
# CHAPTER 6 
## STRINGS

- A *string* is a sequence of characters
- A **string literal** uses quotes 'Hello' or "Hello"
- For strings, + means **"concantonate"**


    str1 = 'Hello'
    str2 = 'there'



- When a **string** contains numbers, it is still a string
- We can convert *numbers in a string* into a *number* using **int()**



    x = int((str3) + 1
    print(x)
124

----
## READING AND CONVERTING

- We prefer to read data in using strings and then parse and convert the data as we need. 
- This gives us more control over error situations and/or bad user input.
- **INPUT NUMBERS MUST BE CONVERTED FROM STRINGS**


    name = input('Enter:')
Enter: **Chuck**


    print(name)
Chuck


    apple = input('Enter:')
Enter: **100**


    x = apple - 10
TRACEBACK(most recent ...)


    x = int(apple) - 10
    print(x)
90

---
## LOOKING INSIDE STRINGS

- We can get at *any single character* in a string using an index specified in **square brackets**


    fruit = 'banana'
    letter = fruit[1]
    print(letter)
a

- The *index number* must be an integer and starts at zero
- The *index value* can be an expression that is computed


    x = 3
    w = fruit[x - 1]
    print(w)
n


---
### len FUNCTION

- The built-in function **len** gives us the length of a string


    fruit = 'banana'
    x = len(fruit)
    print(x)
6
---
### LOOPING THROUGH STRINGS

- Using a **while** statement and **iteration variable** and the **len** function, we can 
construct a loop to look at each of the letters in a string individually. 



    fruit = 'banana'
    index = 0
    while index < len(fruit):
        letter = fruit[index]
        print(index, letter)
        index = index + 1
    0 b
    1 a
    2 n
    3 a
    4 n
    5 a

 

- A definate loop using a **for** statement is much more elegant
- The **iteration variable** is completely taken care of by the for loop. 

    
    fruit = 'banana'
    for letter in fruit:
        print(letter)
    
    b
    a
    n
    a
    n
    a
---
### SLICING STRINGS
#### Colon Operator


- You can look at any continuous selection of a string using a colon operator. 

    
    M  o  n  t  y   P  y  t  h  o  n
    0  1  2  3  4 5 6  7  8  9 10 11
    s = 'Monty Python'
    print(s[0:4])
Mont
   
- The second number is one beyond the end of the slice ("Up to but not including.")

    
    print(s[6:7])
P
- If the second number is beyond the end of the string, it stops at the end.


    print(s[6:20])
Python

- Leaving off the first number or the last number of the slice, it is assumed to be 
the beginning or end of the string respectively.

    
    s = 'Monty Python
    print(s[:2])
Mo 

    print(s[8:])
thon

    print(s[:])
Monty Python

---
## USING in AS A LOGICAL OPERATOR

- The **in** keyword can be used to check to see if one string is "in" another string. 

    
    fruit = 'banana'
    'n' in fruit
True

    'm' in fruit
False

    'nan' in fruit
True


- **in** returns **True** or **False** and can be used in an **if** statement.


    if 'a' in fruit:
    print('Found it!')
Found it!

---
## STRING COMPARISON


    if word == 'banana':
        print('All right, bananas.')
    if word < 'banana':
        print('Your word,' + word + ',comes before banana.')
    elif word > 'banana':
        print('Your word,' + word + ', comes after banana.')
    else:
        print('All right, bananas.')

---

## STRING LIBRARY

- Python has a number of string functions which are in the string library.
- You can invoke them by appending the function to the string variable. 
- These functions do not modify the original string. Instead, they return a new 
string that has been altered. 

    
    >>>greet = 'Hello Bob'
    >>>zap = greet.lower()
    >>>print(zap)
hello bob

    >>>print(greet)
Hello Bob

    >>>print('Hi There'.lower())
hi there

    >>>stuff = 'Hello World'
    type(stuff)
<class 'str'>
    
    >>>dir(stuff)
    [...'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', ''isdigit',
    'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join',
    'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust',
    'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title',
    'translate', 'upper', 'zfill']

---
## STRING LIBRARY

- str.capitalize()
- str.center(width[, fillchar])
- str.endswith(suffix[, start[, end]])
- str.find(sub[, start[, end]])
- str.lstrip([chars])
- str.replace(old, new[, count])
- str.lower()
- str.rstrip([chars])
- str.strip([chars])
- str.upper()
---
## SEARCHING A STRING

- We use the **find()** function to search for a sub-string within another string 
- **find()** finds the first occurrence of the sub-string 


    fruit = 'banana'
    pos = fruit.find('na')
    print(pos)
2

- If the substring is not found, **find()** returns **-1**

    
    aa = fruit.find('z')
    print(aa)
-1

----
## MAKING EVERYTHING UPPERCASE

- You can make a copy of a string in lower case or upper case.


    greet = 'Hello Bob'
---
< ------------------------------------------------------------------------- >

---
# Chapter 7 **READING FILES**  Chapter 7
----
## OPENING A FILE
----
### Using open()
      fhand = open('mbox.txt', 'r')  
- handle = open(filename, mode)
- filename is a string
- *mode is optional and should be* 'r' if we are planning to *read* the file and 'w' if we are planning to 8write8 the file
----
### The **newline** Character

- We use "newline" to indicate when a line ends

    
    >>>stuff = 'Hello\nWorld!'
    >>>print(stuff)
Hello<br>
World!

- **Newline** is still one character, not two


    >>>stuff = 'X\nY'
    >>>print(stuff)
X<br>
Y

    >>>len(stuff)
3
----

### COUNTING LINES IN A FILE

- Open a file as read-only

    
    fhand = open('mbox.txt')
    count = 0
- Use a **for** loop to read each line


    for line in fhand
        count = count + 1
- Count the lines and print out the number of lines


    print('Line Count:', count
$ python open.py<br>
Line Count: 132045

----
### SEARCHING THROUGH A FILE

- We can put an **if** statement in our **for** loop to only print out lines that meet a certain criteria.


    fhand = open('mbox-short.txt')
    for line in fhand:
        if line.startswith('From:'):
            print(line)
----
#### REMOVING "white space" 

- Use **.rstrip** To remove white space from the right hand side of the string. 


    fhand = open('mbox-short.txt')
    for line in fhand:
        line = line.rstrip()
        if line.startswith('From:') :
            print(line)
----
### SKIPPING WITH CONTINUE
- Skip a line by using the **continue** statement


    fhand = open('mbox-short.txt')
    for line in fhand:
        line = line.rstrip()
        if not line.startswith('From:') :
            continue
        print(line)
----
### USING **in** TO SELECT LINES
- We can look for a string anywhere **in** a line as our selection criteria. 


    fhand = open('mbox-short.txt')
    for line in fhand:
        line = line.rstrip()
        if not '@uct.ac.za' in line:
            continue
        print(line)
This will print out all of the lines that do contain that string, because if it doesn't contain that string, it's just going to continue, but if it does, it's going to print that line. 
----
### **try** and **except**
   
    fname = input('Enter the file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        quit()

    count = 0
    for line in fhand:
        if line.startswith('Subject:') :
            count = count + 1
    print('There were', count, 'subject lines in', fname)
---
< ----------------------------------------------------------------------- >

---

# CHAPTER 8 LISTS CHAPTER 8
### LIST CONSTANTS

- List constants are surrounded by square brackets and the elements in the list are separated by commas. 


    for i in [5, 4, 3, 2, 1]:
       print(i)
    print('Blastoff1')
5<br>
4<br>
3<br>
2<br>
1<br>
Blastoff!
---
### LISTS AND DEFINITE LOOPS

    >>>friends = ['Joseph', 'Glenn', 'Sally']
    >>>for friend in friends :
        >>>print('Happy New Year:', friend)
    >>>print('Done!')
or

    z = ['Joseph', 'Glenn', 'Sally']
    for x in z:
        print('Happy New Year:', x)
    print('Done!
Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
Done!
---

### LOOKING INSIDE LISTS
 
---
    >>>friends = ['Joseph', 'Glenn', 'Sally']
    >>>print(friends[1])
Glenn
---
### LISTS ARE MUTABLE

- Strings are *immutable*. We cannot change the contents of a string. We must make a new string to make any changes. 


    >>>fruit = 'Banana'
    >>>fruit[0] = 'b'
Traceback Error ...<br> 
SOOOOO... We do this:


    >>>x = fruit.lower()
    >>>print(x)
banana

- Lists are *mutable*. We can change an element of a list using the index operator. 

---
    >>>lotto = [2, 14, 26, 41, 63]
    >>>print(lotto)
[2, 14, 26, 41, 63]


    >>>lotto[2] = 28
    >>>print(lotto)
[2, 14, **28**, 41, 63]

---

### USING THE **range** FUNCTION

- The **range** function returns a list of numbers that range from zero to one less than the parameter. 

---
    >>>print(range(4))
[0, 1, 2, 3]


    >>>friends = ['Joseph', 'Glenn', 'Sally']
    print(len(friends))
3

    >>>print(list(range(len(friends))))
[0, 1, 2]
---

### CONCANTENATING LISTS USING **+**

- We can create new lists by adding two existing lists together.

---
    >>>a = [1, 2, 3]
    >>>b = [4, 5, 6]
    >>>c = a + b
    >>>print(c)
[1, 2, 3, 4, 5, 6]


    >>>print(a)
[1, 2, 3]
----

### SLICING LISTS USING **:**


    >>>t = [9, 41, 12, 3, 74, 15]
    >>>t[1:3]
[41, 12]


    >>>t[:4]
[9, 41, 12, 3]


    >>>t[3:]
[3, 74, 15]


    >>>t{:}
[9, 41, 12, 3, 74, 15]
----

### LIST METHODS


    >>>x = list()
    >>>type()
<type 'list'>


    >>>dir(x)
[...'append', 'count', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

---

### BUILDING A LIST FROM SCRATCH

- We can create an empty list and then add elements using the **append** method. 
- The **list** stays in order and new elements are added at the end of the list. 

---
    >>>stuff = list()
    >>>stuff.append('book')
    >>>stuff.append(99)
    >>>print(stuff)
['book', 99]
    
    >>>stuff.append('cookie')
    >>>print(stuff)
['book', 99, 'cookie']
---

### IS SOMETHING IN A LIST?

    
    >>>some = [1, 9, 21, 10, 16]
    9 in some
True


    >>>20 not in some
True
---

### SORTING LISTS


    >>>friends = 'Joseph', 'Glenn', 'Sally']
    >>>friend.sort()
    >>>print(friends)
['Glenn', 'Joseph', 'Sally']



    >>>print(friends[1])
Joseph

----

### BUILT IN FUNCTIONS AND LISTS


    >>>nums = [3, 41, 12, 9, 74, 15]
    >>>>print(len(nums))
6

    >>>print(max(nums))
74

    >>>print(min(nums))
3

    >>>print(sum(nums))
154

    >>>print(sum(nums)/len(nums))
25.6

---

    >>>total = 0
       count = 0
       while True:
           inp = input('Enter a number:')
           if inp == 'done': break
           value = float(inp)
           total = total + value
           count = count + 1
Enter a number: 3<br>
Enter a number: 9<br>
Enter a number: 5<br>
Enter a number: done


    >>>average = total / count
       print('Average:', average)
Average: 5.666666666667

### **OR**

    >>>numlist = list()
       while True:
           inp = input('Enter a number:')
           if inp == 'done': break
           value = float(inp)
           numlist.append(value)
Enter a number: 3<br>
Enter a number: 9<br>
Enter a number: 5<br>
Enter a number: done

       average = sum(numlist) / len(numlist)
       print('Average:', average)
Average: 5.666666666667

---

### STRINGS & LISTS

    >>>abc = 'With three words'
    >>>stuff = abc.split()
    >>>print(stuff)
['With', 'three', 'words']

    >>>print(len(stuff))
3

    >>>print(stuff[0])
With

    >>>for w in stuff:
       print(w)
With<br>
three<br>
words<br>

    >>>line = 'A lot       of spaces'
    >>>ect = line.split()
    >>>print(ect)
['A', 'lot', 'of', 'spaces']

    >>>line = first;second;third'
    >>>thing = line.split()
    >>>print(thing)
['first;second;third']
    
    >>>print(len(thing))
1

    >>>thing = line.split(';')
    >>>print(thing)
['first', 'second', 'third']

    >>>print(len(thing))
3

----

### DOUBLE SPLIT PATTERN

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

    >>>words = line.split()
    >>>email = words[1]
    >>>pieces = email.split('@')
    >>>print(email)
    >>>print(pieces)
stephen.marquard@uct.ac.za<br>
['stephen.marquard', 'uct.ac.za']

----

# CHAPTER 9 **DICTIONARIES** 

### COLLECTIONS
 
- Can store more than 1 value
- Can have more than 1 *place* in the variable
- (*so far, our variables have only 1 value- when we give it a new value, the original value is overwritten*)
- **LIST**- a linear collection of values. Lookup by **position 0 ... length-1**
- **DICTIONARY**- A linear collection of *key - value* pairs. Lookup by "**tag**" or "**key**"

---

### DICTIONARIES

- Keeps entries in the order they were inserted
- "**insertion order**" is NOT always "**sorted order**"

---

### LISTS (Review)

- We **.append** values to the end of a List and look them up by position


    cards = list()
    cards.append(12)
    cards.append(3)
    cards.append(75)
    print(cards)
[12, 3, 75]
    
    print(cards[1])
3

- We insert values into a Dictionary using a key and retrieve them using a key


    cards[1] = cards[1] + 2
    print(cards)
[12, 5, 75]

---

### COMPARING LISTS & DICTIONARIES


    lst = list()                ddd = dict()
    lst.append(21)              ddd['age'] = 21
    lst.append(183)             ddd['course'] = 183
    print(lst)                  print(ddd)
[21, 183]                {'age': 21, 'course': 183}


    lst[0] = 23                 ddd['age'] = 23
    print(lst)                  print(ddd)
[23, 183]                {'age': 23, 'course': 183'}

---

### DICTIONARY LITERALS *(Constants)*

- Dictionary literals use curly braces and have **key : value** pairs
- You can make an empty dictionary using empty curly braces


    jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
    print(jjj)
{'chuck': 1, 'fred': 42, 'jan': 100}


    ooo = {}
    print(ooo)
{}

---

### COUNTING


    ccc = dict()
    ccc['dog'] = 1
    ccc['cat'] = 1
    ccc['cat'] = ['cat'] + 1
    print(ccc)
{'dog': 1, 'cat': 2}

---

### ADDING TO THE DICTIONARY


    counts = dict()
    names = ['dog', 'cat', 'mouse']
    for name in names:
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] = counts[name] + 1

---

### THE **get** METHOD FOR DICTIONARIES


    if name in counts:
        x = counts[name]
    else:
        x = 0


    x = counts.get(name, 0)

---

### SIMPLIFIED COUNTING WITH **get()**


    counts = dict()
    names = ['dog', 'cat', 'dog', 'mouse',]
    for name in names:
        counts[name] = counts.get(name, 0) + 1
    print(counts)
{'dog': 2, 'cat': 1, 'mouse': 1}

---

### COUNTING PATTERN


    counts = dict()
    print('Enter a line of text:')
    line = input("")

    words = line.split()

    print('Words:', words)

    print('Counting...')
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    print('Counts', counts)
Enter a line of text:<br>
the clown ran after the car and the car ran into the tent and the tent fell
down on the clown and the car<br>
Words: ['the', 'clown', 'ran', 'after', 'the', 'car', 'and', 'the', 'car', 'ran', 'into',
'the', 'tent', 'and', 'the', 'tent', 'fell', 'down', 'on', 'the', 'clown', 'and', 'the',
'car']<br>
Counting…<br>
Counts {'the': 7, 'clown': 2, 'ran': 2, 'after': 1, 'car': 3, 'and': 3, 'into': 1,
'tent': 2, 'fell': 1, 'down': 1, 'on': 1}




