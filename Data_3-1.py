with open('ketingzhou.txt') as f:
    full_text = f.read()

print(full_text)



with open('hello.txt') as f:
	my_name = f.read()
	f.write('Hello, my name is my_name')