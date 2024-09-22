# your heading here

'''
DISCO:
<note any discoveries you made here... no matter how small!>

QCC:
0. Is Flask a class?
1. Where is the variable "name" coming from (for Flask)
2. Why is the link for the webpage temporary 
3. Why do you need to print(name) first?
4. Do the numbers within the link mean anything?
5. Why does print(name) print main?
 ...

INVESTIGATIVE APPROACH:
We can run through the process of creating the webpage again. By:
- Setting up a virtual enviornment
- Install flask through pip
- Running python3 app.py
- Copying the link into a browser
Then repeating the process again, but except some portions of the code,
like the print statements for example.
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?
                                            #This reminds of inheritance in java when calling super function.

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
                                            #"/" refers to the root URL of a web application (e.g., http://127.0.0.1:5000/)
                                            #/ also serves as the root directory
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
                                            #To the terminal; it prints (_main)
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?
                                            #On the webpage that is generated from the url when running app.py in the virtual enviornment

app.run()                                # Q5: Where have you seen similar constructs in other languages?
                                            #When calling a method of another class, this type of syntax is typically used.
                                            #Perhaps it is calling a static method since no objects seems to be created.
