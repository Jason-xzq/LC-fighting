# LC-fighting
My leetcode solutions


### Some concepts
In python, regard 0, "", None as false, other numbers or strings as true

### Definition and Usage
The None keyword is used to define a null value, or no value at all.

None is not the same as 0, False, or an empty string. None is a data type of its own (NoneType) and only None can be None.

### Python Dictionary Methods
| Method       | Description                                                  |
| ------------ | ------------------------------------------------------------ |
| clear()      | Removes all the elements from the dictionary                 |
| copy()       | Returns a copy of the dictionary                             |
| fromkeys()   | Returns a dictionary with the specified keys and value       |
| get()        | Returns the value of the specified key                       |
| items()      | Returns a list containing a tuple for each key value pair    |
| keys()       | Returns a list containing the dictionary's keys              |
| **pop()**    | Removes the element with the specified key                   |
| popitem()    | Removes the last inserted key-value pair                     |
| setdefault() | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value |
| update()     | Updates the dictionary with the specified key-value pairs    |
| values()     | Returns a list of all the values in the dictionary           |

### Python lambda

[good example](https://zhuanlan.zhihu.com/p/80960485)

### Python defaultdictionary 

[good example](https://www.jianshu.com/p/bbd258f99fd3)

### Python String

[string join operation](https://www.programiz.com/python-programming/methods/string/join)

### Python Set

[excellent data structure constant time in searching](https://www.runoob.com/python3/python3-set.html)

### Python Deque(great tools)
https://www.geeksforgeeks.org/deque-in-python/

## Solutions

### T166

- case: forget negative case
- int/int would get float; if you want return int, use //
- IMPORTANT: check remainder not quotient to determine whether it is recurring!

### T33&T13
take care of conditions!!!
too many details

###213 
very close to the solution: review later