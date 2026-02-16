#match - match the exact sequence

import  re
#o/p match object: matched sequence and span()- start and end index
text="hello world"
result=re.match("hello",text)
print(result)



#using pattern
test_str="12345abcABCabc"
pattern = re.compile("abc")
#re.finditer() finds all non-overlapping matches of a pattern in a string
# and return an iterator of match objects(not a list)
matches= pattern.finditer(test_str)
for match in matches:

    print(match)


#search operation searches the entrie string
#return the first occurence

text="python is powerful maths powerful"
result= re.search("powerful",text)
print(result)


# search - it searches the entire string - find the occurances
# match- beginning value - validate the formats

# raw string for including special character
a=r"\tHello"
print(a)

#match() - determeine if the RE matches at the beginning of the string
#search() - scan through a string, looking for any location where this RE matches.
#finditer() - Find all the substrings where the RE matches, and returns them as an iterator.
#findall()- Find all the strings where the re matches and returns a list


#findall()
my_string = "abc123ABC123abc"
pattern = re.compile(r'123')
matches = pattern.findall(my_string)

for match in matches:
    print(match)

#Methods on match

#group()- Return the string matched by the RE
#start() - Return the starting position of the match
#end() - Return  the ending position of match
#span() - Return a tuple containig the (start,end) positions of the match

test_string = '123abc4567abc123ABC'
pattern = re.compile(r'abc')
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
    print(match.span(), match.start())
    print(match.group()) # return the substring that was matched by the RE

#special characters
#meta characters
# regular ecpressions

#Pattern Meaning

#abc Matches exact test
#[abc] a or b or c at
#[a-z] lowercase letters
#[0-9] digits

#abc
test="i like abc and abcd"
result= re.findall("[a-z]",text)
print(result)

#[abc] a or b or c - matches any one of the character
#matches single characters: a OR b OR c
test="apple banana cat"
result= re.findall("[abc]",test)
print(result)

#[a-z]lowercase letters
test = "I like abc and ABCGHJHJH"
result=re.findall("[a-z]",test)
print(result)

#[0-9]
text= " I like abc and 1234ABOBF495793"
result=re.findall("[0-9]",text)
print(result)

#a b
text= "cat bat rat mat"
result=re.findall("cat|bat",text)
print(result)
#matches either "cat OR "bat"

#any single character
text="cat bat rat bob"
result=re.findall("c.t",text)
print(result)

#special characters
'''
Special sequences begin with a \
Sequence Meaning example

Special sequences begin with a backslash \.
Sequence    Meaning    Example
\d  Digit (0–9)    \d\d
\D  Non-digit  \D
\w  Word char (a-z, A-Z, 0-9, _)   \w+
\W  Non-word char  \W
\s  Whitespace \s
\S  Non-whitespace \S
\b  Word boundary  \bcat\b
\B  Not a word boundary    \Bcat
'''


#\d Digit(0-9) \d\d
print(re.findall(r"\d","Order 123 costs 450"))
#\D  Non-digit  \D
print(re.findall(r"\D","Order 123 costs 450"))

#\w  Word char (a-z, A-Z, 0-9, _)   \w+

Text=("Python_3 version")
result=re.findall(r"\w",text)
print(result)
#\W  Non-word char  \W
#matches anything that is NOT a word character
text="Hello@123"
result=re.findall(r"\W",text)
print(result)

#\s  Whitespace \s spaces, tabs and newline
text="Hello World\nPython"
result= re.findall(r"\s",text)
print(result)


#\S  Non-whitespace \S
text="Hello@123"
result= re.findall(r"\S",text)
print(result)


#\b  Word boundary  \bcat\b
text="cat scatter catalog"
result= re.findall(r"\bcat\b",text)
print(result)

#matches only full  word "cat"
#\B  Not a word boundary    \Bcat
text="cat scatter catalog"
result= re.findall(r"cat\B",text)
print(result)

'''Meta - characters have 
Meta-characters have special meaning in regex.

Meta-character  Meaning
.   Any character
^   Start of string
$   End of string
*   0 or more
+   1 or more
?   0 or 1
{n} Exactly n times
{n,}    n or more
{n,m}   Between n and m
[]  Character set
()  Grouping
'''










#Start of string
text="Python is easy"
print(re.findall(r"^Python",text))

#$ End of the string
text= "Python is easy"
print(re.findall(r"easy$",text))

#* 0 or more
text="ab abb abbb a"
print(re.findall(r"ab+",text))

#? 0 or 1
text="color colour colr"
print(re.findall(r"colou?r",text))

#{n} Exactly n times
text= "111 22 3333 68777"
print(re.findall(r"\d{3}",text))

#{n,} Exactly n times
text= "111 22 3333 68777"
print(re.findall(r"\d{3,}",text))

#{n,m} Between n and m
text= "111 22 3333 68777"
print(re.findall(r"\d{2,3}",text))

#[] Character set
text="apple banana cat"
print(re.findall(r"[abc]",text))

#() Grouping
text= "2026-02-11"
result= re.findall(r"(\d{4})-(\d{2})-(\d{2})",text)
print(result)

#regular experssion
'''
Modifier    Short  Purpose
re.IGNORECASE   re.I   Case-insensitive matching
re.MULTILINE    re.M   ^ and $ match each line
re.DOTALL   re.S   . matches newline
re.VERBOSE  re.X   Write readable regex with comments
re.ASCII    re.A   ASCII-only matching
re.DEBUG    —  Debug pattern
'''

#re.IGNORECASE   re.I   Case-insensitive matching
text="Python"
print(re.search("python",text,re.I))

#re.MULTILINE    re.M   ^ and $ match each line
text="Hello\nPython"
print(re.search("^Python",text,re.M))

#re.DOTALL   re.S   . matches newline
text="Hello\World"
print(re.search("Hello.*World",text,re.S))

#re.VERBOSE  re.X   Write readable regex with comments
import re
pattern = re.compile(r"""
7879hbgjklkdgdskl..%^^&*89
""",re.X)
print(pattern)
#re.ASCII re.A   ASCII-only matching
print(re.findall(r"\w+",text,re.A))

#re.DEBUG    —  Debug pattern
pattern=re.compile(r"""
7879hbgjklkdgdskl..%^^&*89
""",re.DEBUG)
print(pattern)


#assertitions- validating the output or checking certain conditions

import re
text="Python is easy"
print(re.findall(r"^Python",text))
text="Python is easy"
print(re.findall(r"easy$",text))
text="cat scatter catalog"
print(re.findall(r"\bcat\b",text))
text="Python is easy"
print(re.findall(r"Python\B",text))
"""
^ → Start of string
$ → End of string
\b → Word boundary
\B → Not word boundary
(?=...) → Positive Lookahead
(?!...) → Negative Lookahead
(?<=...) → Positive Lookbehind
(?<!...) → Negative Lookbehind
"""

#(?=...) positive Lookahead= match only if
text="user1 admin 2 test"
print(re.findall(r'\w(?=\d)',text))
#neagtive lookahaed
text="user1 admin  test2"
print(re.findall(r'\w(?!\d)',text))
result = re.findall(r'\b(?!\w*\d)\w+\b', text)
print(result)

#(?<=...) positivr lookbehind match only if preeced by something
text="Price ₹500"
print(re.findall(r"(?<= ₹)\d+",text))

#(?<!...) negative lookbehind
text="500 ₹300"
print(re.findall(r"(?<!=₹ )\d+",text))

result=re.findall(r"^ab", "ab\nabc\nab", re.M)
print(result)
