# Bcrypt

We already talked a bit about hashing in the Flask section. We also mentioned that the hashing algorithm we used, md5, is not secure enough. We'll dive just a bit more into why that is before trying out a much more secure hashing algorithm, bcrypt.

## Hashing Revisited
Hashing is the process by which a value is converted into some new, harder to guess value. This process is complex and involves converting character values to numerical values and then repeating many mathematical operations many times. The more times this operation is repeated the more difficult, or even impossible, it becomes to reverse this process.

A hacker's best hope against hashing is a brute-force attack. Brute-force means that the only way to find a password from a hash is by attempting to guess every possible combination of values in order to arrive at the correct answer. With the vast increase in computing power this becomes more and more possible. The strength of a hashing algorithm lies in how long it takes to execute. If a hashing algorithm takes a long time to run, it will take far too long for even a computer to ever guess a password in any reasonable amount of time.

Although you can speed up this process by throwing more computing power at the problem, some problems are too complex to solve. This is where bcrypt comes in. Unlike md5, bcrypt has not been cracked. This is, in part, because bcrypt hashes more slowly than md5. Let's use bcrypt now in our Django app. Activate your Django virtual environment.

  `pip install bcrypt`

In some operating systems, bcrypt requires a few extra dependencies. If you're having trouble installing bcrypt don't try working it out on your own! Installation problems can be tricky and time consuming. Ask an instructor right away!

Bcrypt's documentation (https://pypi.python.org/pypi/bcrypt/2.0.0) explains how to generate an initial hashed password, as shown below, as well as how to compare passwords! In essence, bcrypt can retrieve a salt from a bcrypt encrypted string. Amazingly, the line before the exit in the snippet below prints out the same thing as hashed. Could we do some sort of comparison to see if a random password you pass in is equivalent?

After you have pip installed, in your terminal or command prompt, with your virtual environment active, try the following:

  `(djangoenv)>python
  >>> import bcrypt
  >>> password = "magical unicorns"
  >>> hashed = bcrypt.hashpw(password, bcrypt.gensalt())
  >>> print hashed
  >>> print len(hashed)
  >>> password2 = "bananas"
  >>> hashed2 = bcrypt.hashpw(password2, bcrypt.gensalt())
  >>> print hashed2
  >>> if hashed == hashed2:
  ...      print "the passwords match!"
  ...   else:
  ...      print "the passwords don't match!"
  ...
  >>> exit()`

This works great, but things will be different when you start working with user data and databases. You will find that, when passing data from your request object to bcrypt hashing functions, you will get an encoding error. The same thing will happen when you try to compare a password from the database to user input during login. For this, you'll need the your_string.encode() method. This method ensures that all of your data is encoded as 'utf-8'. Encoding is simply a technique for writing data for more efficient storage and transmission. Now you know how to use bcrypt to securely hash passwords. You'll be trying it out in coming assignments!

Check out the documentation for the encode method: your_string.encode():
https://docs.python.org/3/library/stdtypes.html#str.encode
