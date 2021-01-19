import re

test_string = '123abc456789abc123ABC'

# compile the pattern you want to find
pattern = re.compile(r"abc")
# r"" is for raw string

# find that pattern in "pattern" from test_string using finditer
matches = pattern.finditer(test_string)

# if you want to do it directly witout using "pattern" i.e re.compile
#matches = re.finditer(r"abc",test_string)

# matches is an obejct that can be looped over
# for match in matches:
#     print(match)
    #output
#<re.Match object; span=(3, 6), match='abc'>
#<re.Match object; span=(12, 15), match='abc'>

#METHODS TO SEARCH FOR PATTERN
# .match() looks for patterns only in the beginning of the string
# search() returns only the first instance of the pattern
# findall() output = ['abc', 'abc']
# finditer returns an object of matches patterns that can be iterated over

# matches = pattern.finditer(test_string)
# for match in matches:
#     print(match.group())

    # 4 methods can be used on match 
    # group () , start(), end, span

# META CHARACTERS

testStr = 'hello 123_ heyho hohey   '
tstr = 'heyho hohey   '

#pattern = re.compile('[a-zA-Z0-9]')
pattern = re.compile(r'\bhey')
matches = pattern.findall(tstr)
print(matches)
#for i in matches:   
#    print(i)
