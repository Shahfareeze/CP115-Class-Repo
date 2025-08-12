value = 1

if(value == 1):
     print("Value is 1")
else:
  print("Value is not 1")



value = -1

if(value == 1):
        print("Value is 1")
        print("This is an additional print statement.")
else:
    print("Value is not 1")

#snake_case
student_name = "Ali"
total_price = 150.50
is_passed_exam = True
number_of_items = 5
#CamelCase
studentName = "Ali"
totalPrice = 150.50
isPassedExam = True
numberOfItems = 5

# Using single quotes
name1 = 'Ali'
print(name1)

# Using double quotes  
name2 = "Ali"
print(name2)

# Both produce the same result
print(name1 == name2)  # Output: True


# If your string contains single quotes, use double quotes
message1 = "I can't believe it's working!"
print(message1)

# If your string contains double quotes, use single quotes
message2 = 'He said "Hello there!"' \
'kalau yamg ni tak dapat banyak line cuma satu line ni' \
'kalau digunakan banyak baris ianya akan ditambah dengan tanda ni"\"'
print(message2)


# Using triple double quotes
long_text = """This is a long text
hai ini adalah teks yang panjang dapat tulis banyak baris
that spans multiple lines.

You can write as many lines as you want."""
print(long_text)

# Using triple single quotes
poem = '''Roses are red,
Violets are blue,
Python is awesome,
And so are you!'''
print(poem)

student_name = "Ali"
student_name.upper()
print(student_name)


student_name = "Ali"
uppercase_name = student_name.upper()
print(uppercase_name)  
print(student_name)    

# Or you can reassign to the same variable
student_name = student_name.upper()
print(student_name)

student_name = "Ali Rahman"
print(len(student_name)) 

# You can also use it directly on a string
print(len("Hello World"))



# Without \n - everything prints on one line
print("Hello World How are you?")

# With \n - creates line breaks
print("Hello\nWorld\nHow are you?")

# You can combine \n with regular text
message = "Name: Ali\nAge: 20\nGrade: A"
print(message)

# Without \t - no spacing
print("Name Age Grade")
print("Ali 20 A")

# With \t - creates neat columns
print("Name\tAge\tGrade")
print("Ali\t20\tA")
print("Sarah\t19\tB+")


# Creating a formatted table
student_data = "Student Information:\n\nName\tAge\tGrade\nAli\t20\tA\nSarah\t19\tB+"
print(student_data)


"""
This is a multi-line comment using triple quotes.
You can write multiple lines without using # on each line.
This is technically a string, but if it's not assigned to a variable,
Python ignores it, making it act like a comment.
"""

print("Code after triple quote comment")

'''
You can also use triple single quotes
for multi-line comments.
Both work the same way.
'''