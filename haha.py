import sys
print(sys.version)
print(sys.executable)

def greetings(who):
	greeting = "Hello, {}".format(who)
	return greeting


print(greetings("Arun"))
print(greetings("World"))
print(greetings("Thankam"))
