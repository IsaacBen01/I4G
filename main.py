# check if two words are anagrams
# Example:
# find_anagrams("hello", "check")
# find_anagrams("below", elbow")

first = input ("Enter first string: ")
second = input ("Enter second string: ")
if (sorted(first) == sorted(second)):
    print ("True")
else:
    print ("False")
