# We can use regular expressions instead of if-else statements.
# Regex is used to match or find a certain format/patterns in Strings (for ex: user inputs!).
# 'The username can only be consists of lower-case letters.' Yeah, then, use regex!

import re

#after ^, there comes the thing we want them to be the first character.
pattern = re.compile("^[A-Z]+$")
#In here, we want to start with any upper-case letter between A to Z to be the first letter.
# $ sign is there to represent the end of the string.
# whatever between the ^ and $ means that the whole string should consists of uppercase characters.

print(pattern.search("Hello World"))
print(pattern.search("HELLO WORLD"))
print(pattern.search("HELLOWORLD"))

