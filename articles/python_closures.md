# Python - Closures

Sometimes wrapping a block of code inside a function is not enough. Sometimes we need the function to retain some information across multiple calls. This might be a counter, that must remember the last count in order to add to it on each call, an appender, that must retain the list to which it must add yet another item or function that needs to retain a set of parameters which don’t need to be passed to it on every call. As a first instinct I opted to solving this issue using a class, but in Python there is a simpler solution, **closures**.
<br /><br /><br />
Closures are essentially **nested functions**. An *outer function* encloses an *inner function* that is ultimately returned as the outer functions output. We can then call the outer function, assign its output (the inner function) to a variable and then call that as many times as we want. The inner function retains all information from its non-local scope (the outer function).
<br /><br /><br />
To create a simple counter we need to declare the count variable in the outer function and add to it in the inner function

```python
def counter():
	cur_count = 0
	def count():
		cur_count += 1
		return cur_count
	return count
 
counter1 = counter()
counter1() # returns 1
counter1() # returns 2
counter1() # returns 3
```
<br />
Creating an appender is similar but instead of adding 1 to an integer we add strings/integers, or whatever else you want, to a list. 

```python
def make_appender():
	my_list = []
	def add_to_list(item):
		my_list.append(item)
		return my_list
	return add_to_list
 
minion_words = make_appender()
minion_words('bello')		# ['bello']
minion_words('bank yu')		# ['bello', 'bank yu']
minion_words('poopaye')		# ['bello', 'bank yu', 'poopaye']
```
<br />
We can also have parameters for the outer function that are then passed to the inner function. Changing the values of these parameters allows us to create variants of the inner function.

```python
def disco_disco_party_party(i_say, you_say):
	def sing_verse():
		print(f'I say {i_say}.\nYou say {you_say}.')
		print(f'{i_say.capitalize()}, {i_say}!\n{you_say.capitalize()}, {you_say}!')
	return sing_verse
 
verse1 = disco_disco_party_party('disco', 'party')
verse2 = disco_disco_party_party('party', 'disco')
verse3 = disco_disco_party_party('disco', 'disco')
verse1()
verse1()
verse2()
verse3()
```
<br />
Closures can also be used to create decorators, caching functions and callback functions amongst others, but these are subjects for later articles.
<br /><br /><br />
I hope you learned something new with this article and if you want to dig deeper into closures you can use the following links.

- **Learn Python** - [Closures](https://www.learnpython.org/en/Closures)
- **Analytics Vidhya** - [Understanding Python Closures: Deep Dive into Functional Programming](https://www.analyticsvidhya.com/blog/2024/02/python-closures/)
- **Real Python** - [Python Closures: Common Use Cases and Examples](https://realpython.com/python-closure/)
<br /><br /><br />
As a challenge, you can try to implement a simple caching function. It should should receive any function as a parameter and save its input and output. Every time you call it, it will query the previous inputs and if the current input has already been processed it will directly return the output without having to process it again. Enjoy the challenge!