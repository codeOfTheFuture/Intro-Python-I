"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open('c:/Users/Jeff/Desktop/Lambda CS/Intro-Python-I/src/foo.txt', 'r') as f:
  read_data = f.read()
  print(read_data)

print(f.closed)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('c:/Users/Jeff/Desktop/Lambda CS/Intro-Python-I/src/bar.txt', 'w') as b:
  b.write('Did you know the first French fries weren\'t actually cooked in France? They were cooked in Greece.')

print(f.closed)

with open('c:/Users/Jeff/Desktop/Lambda CS/Intro-Python-I/src/bar.txt', 'r') as b:
  read_data = b.read()
  print(read_data)

print(f.closed)