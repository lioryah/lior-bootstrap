title = 'Python Programming'

# The syntax of encode() method is:
print(title.encode(encoding='UTF-8',errors='strict'), '\n')

# unicode string
string = 'pythön!'

# print string
print('The string is:', string, '\n')

# default encoding to utf-8
string_utf = string.encode()

# print result
print('The encoded version is:', string_utf)

# ignore error
print('The encoded version (with ignore) is:', string.encode("ascii", "ignore"))

# replace error
print('The encoded version (with replace) is:', string.encode("ascii", "replace"), '\n')

# print decoded string from utf-8
print('The decoded version is:', string_utf.decode())

# default encoding to utf-8
string_utf16 = string.encode("utf-16")
print('The encoded version to utf-16 is:', string_utf16)