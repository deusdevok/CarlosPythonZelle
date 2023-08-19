# Chapter 10 - Review Questions

## True/False

1. True. The constructor is the __init__ method.
2. False. Functions that live in objects are called _methods_.
3. False. It is generally called _self_, but it can be called anything in reallity. _this_ is used in _javascript_.
4. False. It can have more than one.
5. False. Is called an object.
6. True.
7. False. A docstring is a special type of comment, used for documenting methods or functions.
8. False. This happens in regular local function variables, the values disappear once the function terminates.
9. False. One or two underscores are used to make methods unaccesible.
10. True.

## Multiple Choice

1. b.
2. a.
3. d.
4. b.
5. c.
6. d.
7. c.
8. a.
9. c.
10. c.

## Discussion

1. (page 324). Instance variables live in objects. They can be used to remember the state of an object. They can be referred to again in other methods (using dot notation). Regular function variables values disappear once the function terminates, as opposed to instance variables in objects.

2. Explain in terms of actual code:

	a) **method**: a method is a function that lives in an object. It is a function inside a class. It can be executed using dot notation.

	b) **instance variable**: a variable that lives in an object. It can be accessed using dot notation.
		`self.value = 5`
		*value* is the instance variable.
	
	c) **constructor**: the *__init__* method. This is called to initialize a new instance of a class. Provides initial values for the instance variables of the object.
	
	d) **accessor**: a method that *returns* a value.
		```
		def getValue(self):
			return self.value
		```
	
	e) **mutator**: a method that *changes* the values of instance variables, without returning anything (returns `None`).
		```
		def editValue(self):
			self.value = randrange(1,9)
		```

3. After running main():
```
Clowning around now.
Creating a Bozo from: 3
Creating a Bozo from: 4
Clowning: 3
18
9
Clowning: 2
12
Clowning: 8
64
16
```