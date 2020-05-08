import sys
print(sys.version)
print(sys.executable)

def greetings(who):
	greeting = "Hello, {}".format(who)
	return greeting

greetings("Arun")
print("How are you doing today?")
