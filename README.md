# Regex for Uppercase Username Validation
## Overview
This Python script demonstrates the use of regular expressions (regex) to validate whether a given username adheres to a specific pattern. In this case, the requirement is that the username should consist solely of uppercase letters.

### How it Works
Regular expressions provide a powerful alternative to traditional if-else statements for pattern matching in strings. The script utilizes the re module in Python to define and apply a regex pattern.

### Regex Pattern
The regex pattern used in this script is as follows:

```
pattern = re.compile("^[A-Z]+$")
```

Here's a breakdown of the pattern:

+ "^" asserts the start of the string.
+ "[A-Z]" specifies that the first character should be any uppercase letter from A to Z.
+ "+" requires one or more occurrences of the specified character set.
+ "$" asserts the end of the string.
+ Together, "^[A-Z]+$" ensures that the entire string consists of uppercase letters.

### Example Usage
```
print(pattern.search("Hello World"))
print(pattern.search("HELLO WORLD"))
print(pattern.search("HELLOWORLD"))
```
<br/>
The first example (Hello World) does not match the pattern and returns None.<br/>
The second example (HELLO WORLD)does not match the pattern and returns None.<br/>
The third example (HELLOWORLD) matches the pattern and returns a match object.<br/>
