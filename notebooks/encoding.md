# Encoding

[Link to reference](https://www.techopedia.com/definition/948/encoding)

Encoding is the process of converting data into a format required for a number of information processing needs, including:

* Program compiling and execution
* Data transmission, storage and compression/decompression
* Application data processing, such as file conversion

encoding is the process of applying a specific code, such as letters, symbols and numbers, to data for conversion into an equivalent cipher.

### String Encoding

Since Python 3.0, strings are stored as Unicode, i.e. each character in the string is represented by a code point. So, each string is just a sequence of Unicode code points.

For efficient storage of these strings, the sequence of code points is converted into a set of bytes. The process is known as encoding.



## ASCII

American Standard Code for Information Interchange

The standard ASCII scheme has only zero to 127 character positions; 128 through 255 are undefined.


## Unicode

[Link to reference](https://flaviocopes.com/unicode/)

Unicode is a universal character encoding standard that assigns a code to every character and symbol in every language in the world. Since no other encoding standard supports all languages, Unicode is the only encoding standard that ensures that you can retrieve or combine data using any combination of languages.

### UTF-8

UTF-8 is a variable width character encoding, and it can encode every character covered by Unicode, using from 1 to 4 8-bit bytes.

 If the letter A in ASCII was represented with the number 65, using UTF-8 it’s encoded as U+0041.
