# Learning Python

## Python Variables

A variable is a user-defined name stored in the memory for holding values or a container for storing data values. For example: `x = 5`

- Variables do not need to be declared with any particular type and can even change type after they have been set.
- If you want to specify the data type of a variable, this can be done with **casting**.
  e.g., `x = str(3)` # x will be '3' not 3
- Variable names are case-sensitive. `a = 4` and `A = "Sally"` are two different variables.
- A variable name must start with a letter or the underscore character.
- A variable name cannot start with a number.
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and `_`).
- Variable names are case-sensitive (age, Age and AGE are three different variables).
- A variable name cannot be any of [Python reserved keywords](https://www.w3schools.com/python/python_ref_keywords.asp).
- Variables are sometimes declared using variable names in the format **camelCase**, **PascalCase**, or **snake_case**.
- Python allows you to assign values to multiple variables in one line.
  e.g.,
  ```python
  x, y, z = "Orange", "Banana", "Cherry"
  print(x)
  print(y)
  print(z)
  ```
- You can assign the same value to multiple variables in one line.
  e.g.,
  ```python
  x = y = z = "Orange"
  print(x)
  print(y)
  print(z)
  ```
- If you have a collection of values in a list, tuple, etc., Python allows you to extract the values into variables. This is called unpacking.
  ```python
  fruits = ["apple", "banana", "cherry"]
  x, y, z = fruits
  print(x)
  print(y)
  print(z)
  ```

### Getting the Type of a Variable

You can use `type()` to get the type of a variable.
e.g.,

```python
x = 5
print(type(x)) # This will print int
```

### Global Variables

- Variables created outside of a function are known as global variables, which means they can be accessed by everyone.
- You can make a variable inside a function globally by using the `global` keyword.
  e.g.,

  ```python
  def myfunc():
    global x
    x = "fantastic"

  myfunc()

  print("Python is " + x)
  ```

## Python Data Types

Data Types refer to the type of a value stored with the variable. There are different types of data, which include:

- `str` e.g., `x = "Hello World"`
- `int`, `float`, `complex` e.g., `x = 20`, `x = 1j`
- `list`, `tuple`, `range` e.g., `x = ["apple", "banana", "cherry"]`, `x = ("apple", "banana", "cherry")`, `x = range(6)`
- `dict` e.g., `x = {"name" : "John", "age" : 36}`
- `set`, `frozenset` e.g., `x = {"apple", "banana", "cherry"}`, `x = frozenset({"apple", "banana", "cherry"})`
- `bool` e.g., `x = True`
- `bytes`, `bytearray`, `memoryview` e.g., `x = b"Hello"`, `x = bytearray(5)`, `x = memoryview(bytes(5))`
- `NoneType` e.g., `x = None`

## isinstance

`isinstance()` is a built-in function in Python that checks whether an object is an instance of a particular class or data type, or any of a tuple of classes and types. It's a versatile tool used for type checking, ensuring that variables or objects adhere to expected types within code, which is crucial for maintaining code reliability and avoiding type-related errors in dynamically typed languages like Python.

```python
isinstance(object, classinfo)
```

- **object**: The variable or object to be checked.
- **classinfo**: A single class, data type, or a tuple of classes and types to check against the object.

**Returns**

- `True` if the object is an instance or subclass of `classinfo`, or if the object is one of the types in `classinfo` when it's a tuple.
- `False` otherwise.

## Python Strings

Strings in Python are surrounded by either single quotation marks or double quotation marks.

### Properties and Methods Related to Strings

- **Multiline Strings**: You can assign a multiline string to a variable by using three quotes.
- **Strings are Arrays**: This means you can use indexing on strings. e.g., `name = "John"` => `name[0]` would be **J**.
- `len()`: e.g.:
  ```python
  a = "Hello, World!"
  print(len(a))
  ```
- **Check String**: To check if a certain phrase or character is present in a string, we can use the keyword `in`. e.g.,
  ```python
  txt = "The best things in life are free!"
  print("free" in txt)
  ```
- **Check if NOT**: To check if a certain phrase or character is NOT present in a string, we can use the keyword `not in`.
- **Slicing Strings**: You can return a range of characters by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string.
  e.g.,
  ```python
  b = "Hello, World!"
  print(b[2:5]) # result: llo
  ```
  **Note**: You can also slice from the start by just doing `b[:5]` and slice up to the end by `b[2:]`. **Negative Indexing** allows you to use negative indexes to start the slice from the end of the string, like `b[-5:-2]`.
- `str.upper()`: Upper case
- `str.lower()`: Lower case
- `str.strip()`: Removes any whitespace from the beginning or the end
- `str.replace()`: The `replace()` method replaces a string with another string:
  e.g.,
  ```python
  a = "Hello, World!"
  print(a.replace("H", "J")) # result: Jello, World!
  ```
- `str.split()`: The `split()` method returns a list where the text between the specified separator becomes the list items. e.g.,
  ```python
  a = "Hello, World!"
  print(a.split(",")) # returns ['Hello', ' World!']
  ```
- **String Concatenation**: To concatenate, or combine, two strings, you can use the `+` operator. e.g.,
  ```python
  a = "Hello"
  b = "World"
  c = a + b
  print(c) # result: HelloWorld
  ```
- **String Formatting using F-Strings**:
  e.g.,
  ```python
  age = 36
  txt = f"My name is John, I am {age}"
  print(txt)
  ```
- **Placeholders and Modifiers**: A placeholder can contain variables, operations, functions, and modifiers to format the value.
  **Examples**:
  1. Add a placeholder for the price variable:
     ```python
     price = 59
     txt = f"The price is {price} dollars"
     print(txt)
     ```
  2. A placeholder can include a modifier to format the value. A modifier is included by adding a colon `:` followed by a legal formatting type, like `.2f`, which means a fixed-point number with 2 decimals:
     ```python
     price = 59
     txt = f"The price is {price:.2f} dollars"
     print(txt)
     ```
  3. A placeholder can contain Python code, like math operations:
     ```python
     txt = f"The price is {20 * 59} dollars"
     print(txt)
     ```
- **Escape Characters**: To insert characters that are illegal in a string, use an escape character. An escape character is a backslash `\` followed by the character you want to insert. An example of an illegal character is a double quote inside a string that is surrounded by double quotes.

**Summary of All Methods**

Here's the formatted content with markdown syntax for code:

**Summary of All Methods**

1. `capitalize()`: Converts the first character to upper case.
2. `casefold()`: Converts the string into lower case.
3. `center()`: Returns a centered string.
4. `count()`: Returns the number of times a specified value occurs in a string.
5. `encode()`: Returns an encoded version of the string.
6. `endswith()`: Returns true if the string ends with the specified value.
7. `expandtabs()`: Sets the tab size of the string.
8. `find()`: Searches the string for a specified value and returns the position of where it was found.
9. `format()`: Formats specified values in a string.
10. `format_map()`: Formats specified values in a string.
11. `index()`: Searches the string for a specified value and returns the position of where it was found.
12. `isalnum()`: Returns True if all characters in the string are alphanumeric.
13. `isalpha()`: Returns True if all characters in the string are in the alphabet.
14. `isascii()`: Returns True if all characters in the string are ASCII characters.
15. `isdecimal()`: Returns True if all characters in the string are decimals.
16. `isdigit()`: Returns True if all characters in the string are digits.
17. `isidentifier()`: Returns True if the string is an identifier.
18. `islower()`: Returns True if all characters in the string are lower case.
19. `isnumeric()`: Returns True if all characters in the string are numeric.
20. `isprintable()`: Returns True if all characters in the string are printable.
21. `isspace()`: Returns True if all characters in the string are whitespaces.
22. `istitle()`: Returns True if the string follows the rules of a title.
23. `isupper()`: Returns True if all characters in the string are upper case.
24. `join()`: Joins the elements of an iterable to the end of the string.
25. `ljust()`: Returns a left justified version of the string.
26. `lower()`: Converts a string into lower case.
27. `lstrip()`: Returns a left trim version of the string.
28. `maketrans()`: Returns a translation table to be used in translations.
29. `partition()`: Returns a tuple where the string is parted into three parts.
30. `replace()`: Returns a string where a specified value is replaced with a specified value.
31. `rfind()`: Searches the string for a specified value and returns the last position of where it was found.
32. `rindex()`: Searches the string for a specified value and returns the last position of where it was found.
33. `rjust()`: Returns a right justified version of the string.
34. `rpartition()`: Returns a tuple where the string is parted into three parts.
35. `rsplit()`: Splits the string at the specified separator, and returns a list.
36. `rstrip()`: Returns a right trim version of the string.
37. `split()`: Splits the string at the specified separator, and returns a list.
38. `splitlines()`: Splits the string at line breaks and returns a list.
39. `startswith()`: Returns true if the string starts with the specified value.
40. `strip()`: Returns a trimmed version of the string.
41. `swapcase()`: Swaps cases, lower case becomes upper case and vice versa.
42. `title()`: Converts the first character of each word to upper case.
43. `translate()`: Returns a translated string.
44. `upper()`: Converts a string into upper case.
45. `zfill()`: Fills the string with a specified number of 0 values at the beginning.

## Python Booleans

Booleans represent one of two values: `True` or `False`.
Almost any value is evaluated to `True` if it has some sort of content.

- Any `string` is `True`, except **empty** strings.
- Any `number` is `True`, except **0**.
- Any `list`, `tuple`, `set`, and `dictionary` are `True`, except **empty** ones.

**NOTES:**

- In fact, there are not many values that evaluate to `False`, except empty values, such as `(), [], {}, ""`, the number `0`, and the value `None`. And of course the value `False` evaluates to `False`.
- One more value, or object in this case, evaluates to `False`, and that is if you have an object that is made from a class with a `__len__` function that returns `0` or `False`

## List

`Lists` are used to store multiple items in a single variable.

`Lists` are one of **4 built-in data types** in Python used to store collections of data, the other 3 are `Tuple`, `Set`, and `Dictionary`, all with different qualities and usage.

### Properties & Methods of Lists

**len(list)**: Returns the number of elements in the list.

```python
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5
```

**list.append(element)**: Adds an element to the end of the list.

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```

**list.insert(index, element)**: Inserts an element at the specified index.

```python
my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # Output: [1, 4, 2, 3]
```

**list.remove(element)**: Removes the first occurrence of the specified element from the list.

```python
my_list = [1, 2, 3, 2, 4]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2, 4]
```

**list.pop(index)**: Removes and returns the element at the specified index. If no index is provided, it removes and returns the last element.

```python
my_list = [1, 2, 3, 4]
popped_element = my_list.pop(1)
print(my_list)  # Output: [1, 3, 4]
print(popped_element)  # Output: 2
```

**list.index(element, start, end)**: Returns the index of the first occurrence of the specified element within the optional `start` and `end` range.

```python
my_list = [1, 2, 3, 2, 4]
index = my_list.index(2, 2)
print(index)  # Output: 3
```

**list.count(element)**: Returns the number of occurrences of the specified element in the list.

```python
my_list = [1, 2, 3, 2, 4, 2]
count = my_list.count(2)
print(count)  # Output: 3
```

**list.reverse()**: Reverses the order of elements in the list.

```python
my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)  # Output: [4, 3, 2, 1]
```

**list.sort(key=None, reverse=False)**: Sorts the elements of the list in ascending order. The `key` and `reverse` parameters can be used for custom sorting.

```python
my_list = [4, 2, 1, 3]
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4]
```

**list.extend(iterable)**: Extends the list by appending elements from the iterable.

```python
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]
```

**list.clear()**: Removes all elements from the list.

```python
my_list = [1, 2, 3, 4]
my_list.clear()
print(my_list)  # Output: []
```

These are some of the most commonly used properties and methods of lists in Python 3.

### List Comprehension

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

This is how normally you would do it

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
```

**But with List Comprehension this is the syntax on how you would do it**

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
```

**The Syntax**

```python
newlist = [expression for item in iterable if condition == True]
```

### Sort Lists

- Sort list alphabetically and numerically: `list.sort()`. For `descending` you just add in the sort(reverse = True)
- Sort list using customized functions

```python
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
```

- By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters. So if you want a case-insensitive sort function, use str.lower as a key function

```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
```

- What if you want to reverse the order of a list, regardless of the alphabet? i.e `list.reverse()`

### Copy Lists

You cannot copy a list simply by typing `list2 = list1`, because: `list2` will only be a reference to `list1`, and changes made in `list1` will automatically also be made in `list2`.

There are ways to make a copy, one way is to use the **built-in** List method `copy()`. Another way to make a copy is to use the built-in method `list()`.

```python
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
```

```python
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
```

### Join Lists

There are several ways to join, or concatenate, two or more lists in Python.

1. using the + operator

```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
```

2. appending all the items from list2 into list1, one by one using for loop

```python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
```

3. use the extend() method, where the purpose is to add elements from one list to another list

```python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
```

## Python Dictionaries

- Dictionaries are used to store data values in key:value pairs.
- A dictionary is a collection which is ordered\*, changeable and do not allow duplicates.
- Dictionaries are written with curly brackets, and have keys and values:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
```

### Properties of Dictionaries

**Access Items:**

Accessing items in a dictionary is straightforward using keys. You can also use the `get()` method to retrieve a value with a default if the key is not found.

```python
my_dict = {"key1": "value1", "key2": "value2"}
print(my_dict["key1"])  # Output: value1
print(my_dict.get("key3", "default_value"))  # Output: default_value
```

To get the keys of a `dict` use `keys()`

```python
x = thisdict.keys()
```

To get the values of a `dict` use values() method will return a list of all the values in the dictionary.

```python
x = thisdict.values()
```

The `items()` method will return each item in a dictionary, as tuples in a list

```python
x = thisdict.items()
```

### Check if Key Exists

To determine if a specified key is present in a dictionary use the `in` keyword:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
```

**Change Items:**

To change the value of a specific item in a dictionary, simply assign a new value to the corresponding key.

```python
my_dict["key1"] = "new_value"
print(my_dict["key1"])  # Output: new_value
```

### Update Dictionary

The `update()` method will update the dictionary with the items from the given argument. The argument must be a dictionary, or an iterable object with key:value pairs.

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
```

**Add Items:**

To add a new item to a dictionary, simply assign a value to a new key.

```python
my_dict["new_key"] = "new_value"
print(my_dict["new_key"])  # Output: new_value
```

You can add an item as well using the `update()` method like this:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
```

**Remove Items:**

There are several methods to remove items from a dictionary:

1. The pop() method removes the item with the specified key name:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
```

2. The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
```

3. The del keyword removes the item with the specified key name:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
```

4. The clear() method empties the dictionary:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
```

**Length of Dict:**

To get the number of items in a dictionary, use the `len()` function.

```python
my_dict = {"key1": "value1", "key2": "value2"}
print(len(my_dict))  # Output: 2
```

**Loop:**

You can loop through a dictionary using its keys, values, or key-value pairs using `for` loops.

```python
for key in my_dict:
    print(key)  # Output: key1, key2

for value in my_dict.values():
    print(value)  # Output: value1, value2

for key, value in my_dict.items():
    print(key, value)  # Output: key1 value1, key2 value2
```

**Copy:**

To create a copy of a dictionary, use the `copy()` method.

```python
new_dict = my_dict.copy()
print(new_dict)  # Output: {"key1": "value1", "key2": "value2"}
```

You can as well use `dict()` function:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
```

**Dictionary Methods:**

Python dictionaries provide various methods for common operations such as getting keys, values, items, and more.

```python
print(my_dict.keys())  # Output: dict_keys(['key1', 'key2'])
print(my_dict.values())  # Output: dict_values(['value1', 'value2'])
print(my_dict.items())  # Output: dict_items([('key1', 'value1'), ('key2', 'value2')])
```

**NOTE:** As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

### Nested Dictionaries

Example

```python
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
```

Now how do we access items: _Print the name of child 2_:

```python
print(myfamily["child2"]["name"])
```

#### Loop Through Nested Dictionaries

You can loop through a dictionary by using the `items()` method like this:

```python
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
```

## Python Operators

Operators are used to perform operations on variables and values. These include

1. Arithmetic Operators

- Addition: `+` (e.g., `x + y`)
- Subtraction: `-` (e.g., `x - y`)
- Multiplication: `*` (e.g., `x * y`)
- Division: `/` (e.g., `x / y`)
- Modulus: `%` (e.g., `x % y`)
- Exponentiation: `**` (e.g., `x ** y`)
- Floor division: `//` (e.g., `x // y`)

2. Assignment Operators

- Assignment: `=` (e.g., `x = 5`)
- Addition assignment: `+=` (e.g., `x += 3` which is equivalent to `x = x + 3`)
- Subtraction assignment: `-=` (e.g., `x -= 3` which is equivalent to `x = x - 3`)
- Multiplication assignment: `*=` (e.g., `x *= 3` which is equivalent to `x = x * 3`)
- Division assignment: `/=` (e.g., `x /= 3` which is equivalent to `x = x / 3`)
- Modulus assignment: `%=` (e.g., `x %= 3` which is equivalent to `x = x % 3`)
- Floor division assignment: `//=` (e.g., `x //= 3` which is equivalent to `x = x // 3`)
- Exponentiation assignment: `**=` (e.g., `x **= 3` which is equivalent to `x = x ** 3`)
- Bitwise AND assignment: `&=` (e.g., `x &= 3` which is equivalent to `x = x & 3`)
- Bitwise OR assignment: `|=` (e.g., `x |= 3` which is equivalent to `x = x | 3`)
- Bitwise XOR assignment: `^=` (e.g., `x ^= 3` which is equivalent to `x = x ^ 3`)
- Right shift assignment: `>>=` (e.g., `x >>= 3` which is equivalent to `x = x >> 3`)
- Left shift assignment: `<<=` (e.g., `x <<= 3` which is equivalent to `x = x << 3`)
- Walrus operator: `:=` (e.g., `print(x := 3)` assigns 3 to x and prints it, then `print(x)` displays the value of x)

3. Comparison Operators

- Equal to: `==` (e.g., `x == y`)
- Not equal to: `!=` (e.g., `x != y`)
- Greater than: `>` (e.g., `x > y`)
- Less than: `<` (e.g., `x < y`)
- Greater than or equal to: `>=` (e.g., `x >= y`)
- Less than or equal to: `<=` (e.g., `x <= y`)

4. Logical Operators

- `and`: Returns True if both statements are true (e.g., `x < 5 and x < 10`)
- `or`: Returns True if one of the statements is true (e.g., `x < 5 or x < 4`)
- `not`: Reverses the result, returns False if the result is true (e.g., `not(x < 5 and x < 10)`)

5. Identity Operators

- `is`: Returns True if both variables are the same object (e.g., `x is y`)
- `is not`: Returns True if both variables are not the same object (e.g., `x is not y`)

6. Membership Operators

- `in`: Returns True if a sequence with the specified value is present in the object (e.g., `x in y`)
- `not in`: Returns True if a sequence with the specified value is not present in the object (e.g., `x not in y`)

7. Bitwise Operators

- `&`: AND - Sets each bit to 1 if both bits are 1 (e.g., `x & y`)
- `|`: OR - Sets each bit to 1 if one of two bits is 1 (e.g., `x | y`)
- `^`: XOR - Sets each bit to 1 if only one of two bits is 1 (e.g., `x ^ y`)
- `~`: NOT - Inverts all the bits (e.g., `~x`)
- `<<`: Zero fill left shift - Shift left by pushing zeros in from the right and let the leftmost bits fall off (e.g., `x << 2`)
- `>>`: Signed right shift - Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off (e.g., `x >> 2`)

**NOTE**:
Operator precedence describes the order in which operations are performed.

The following list describes the operator precedence in Python, starting from the highest to the lowest:

1. **`()`** - Parentheses
2. **`**`\*\* - Exponentiation
3. **`+x`, `-x`, `~x`** - Unary plus, unary minus, and bitwise NOT
4. **`*`, `/`, `//`, `%`** - Multiplication, division, floor division, and modulus
5. **`+`, `-`** - Addition and subtraction
6. **`<<`, `>>`** - Bitwise left and right shifts
7. **`&`** - Bitwise AND
8. **`^`** - Bitwise XOR
9. **`|`** - Bitwise OR
10. **`==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in`** - Comparisons, identity, and membership operators
11. **`not`** - Logical NOT
12. **`and`** - Logical AND
13. **`or`** - Logical OR

This order defines how expressions containing multiple operators are evaluated in Python. Operators listed earlier have higher precedence and are evaluated before operators lower in the list.

## Python `if statement`

Python Conditions and If statements

- Equals: a == b
- Not Equals: a != b
- Less than: a < b
- Less than or equal to: a <= b
- Greater than: a > b
- Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.

Example 1:

```python
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
```

Example 2:

```python
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
```

Example 3:

```python
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
```

### Short Hand If ... Else

```python
a = 2
b = 330
print("A") if a > b else print("B")
```

```python
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
```

### The pass Statement

`if` statements cannot be empty, but if you for some reason have an `if` statement with no content, put in the `pass` statement to avoid getting an error.

## Python Loops

### While Loops

With the `while` loop we can execute a set of statements as long as a condition is true.

```python
i = 1
while i < 6:
  print(i)
  i += 1
```

#### The break Statement

With the break statement we can stop the loop even if the while condition is true:

```python
i = 1
while i < 6:
  print(i)
  if i == 3: # Exit the loop when i is 3
    break
  i += 1
```

#### The continue Statement

With the continue statement we can stop the current iteration, and continue with the next:

```python
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
```

#### The else Statement

With the `else` statement we can run a block of code once when the condition no longer is true:

```python
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
```

### For Loops

A `for` loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the `for` keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the `for` loop we can execute a set of statements, once for each item in a list, tuple, set etc

Example

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```

**Note:** The for loop does not require an indexing variable to set beforehand.

#### Else in For Loop

The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

```python
for x in range(6):
  print(x)
else:
  print("Finally finished!")
```

**Note:** The else block will NOT be executed if the loop is stopped by a break statement. E.g

```python
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
```

#### Nested Loops

A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":

```python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
```

## Python Functions

- A function is a block of code which only runs when it is called.
- In Python a function is defined using the `def` keyword
  e.g

```python
def my_function():
  print("Hello from a function")

my_function()
```

### Arguments

Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

### Do we say Parameters or Arguments?

From a function's perspective:

A `parameter` is the variable listed inside the parentheses in the function definition.

An `argument` is the value that is sent to the function when it is called.

### Arbitrary Arguments, \*args

If you do not know how many arguments that will be passed into your function, add a \* before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:

```python
def my_function(*kids):
  print("The youngest child is " + kids[2]) #Output: The youngest child is Linus

my_function("Emil", "Tobias", "Linus")
```

**Note:** Arbitrary Arguments are often shortened to \*args in Python documentations.

### Keyword Arguments

You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.

```python
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
```

### Arbitrary Keyword Arguments, \*\*kwargs

If you do not know how many keyword arguments that will be passed into your function, add two asterisk: \*\* before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:

```python
def my_function(**kid):
  print("His last name is " + kid["lname"]) # Output: His last name is Refsnes

my_function(fname = "Tobias", lname = "Refsnes")
```

### Default Parameter Value

The following example shows how to use a default parameter value. If we call the function without argument, it uses the default value

```python
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden") # I am from Sweden
my_function("India") # I am from India
my_function() # I am from Norway
my_function("Brazil") # I am from Brazil
```

### Passing a List as an Argument

You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function. E.g. if you send a List as an argument, it will still be a List when it reaches the function:

```python
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
```

### `Return` Values and the `pass` Statement

- To let a function return a value, use the `return` statement
- `function` definitions cannot be empty, but if you for some reason have a `function` definition with no content, put in the `pass` statement to avoid getting an error.

### Positional-Only Arguments

You can specify that a function can have ONLY _positional arguments_, or ONLY _keyword arguments_. To specify that a function can have only positional arguments, add `, /` after the arguments:

```python
def my_function(x, /):
# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
  print(x)

my_function(3)
```

### Keyword-Only Arguments

To specify that a function can have only _keyword arguments_, add `*`, before the arguments:

```python
def my_function(*, x):
  print(x)

my_function(x = 3)
```

### Combine Positional-Only and Keyword-Only

You can combine the two argument types in the same function. Any argument before the` / ,` are _positional-only_, and any argument after the `*,` are _keyword-only_.

```python
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
```

### Recursion

Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, `tri_recursion()` is a function that we have defined to call itself ("recurse"). We use the `k` variable as the data, which decrements `(-1)` every time we recurse. The recursion ends when the condition is not greater than `0` (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

```python
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
```

### Python Lambda

A lambda function is a small anonymous function.

**Syntax:**

```python
lambda arguments : expression
```

The expression is executed and the result is returned:

Example:

```python
x = lambda a : a + 10
print(x(5))
```

### Why Use Lambda Functions?

The power of lambda is better shown when you use them as an anonymous function inside another function. Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

```python
def myfunc(n):
  return lambda a : a * n
```

```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
```

```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
```
