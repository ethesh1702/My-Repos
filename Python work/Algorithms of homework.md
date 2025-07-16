&nbsp;**Problem**: Convert hours to seconds.

->Algorithm:

Input: hours



seconds = hours \* 3600



Return seconds

Problem: Square each element in a list.

->Algorithm:

Input: num\_list



For each n in num\_list, calculate n \*\* 2



Return the squared list



**Problem**: Create string s3 from two strings by alternating front of s1 and back of s2.

>-Algorithm:

Input: s1, s2



For i in range of minimum of lengths:



Append s1\[i] and s2\[-(i+1)]



Append leftovers of s1\[i+1:] and s2\[:-i-1]



**Problem**: Get key of minimum value in a dictionary.

->Algorithm:

Input: dictionary



Use min(dictionary, key=dictionary.get)





**Problem**: Sum the series: 1 + 11 + 111 + ... up to n terms.

-> Algorithm:

Input: n



For i from 1 to n:



Append '1' to string



Convert to int and add to sum



Return sum



**Problem**: Multiply two random float numbers.

->Algorithm:

Generate two floats between 0 and 1 or custom range.



Multiply them.



Return result.

