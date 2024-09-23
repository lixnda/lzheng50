# your heading here

'''
DISCO:
-We noticed that the return  is what is printed on the content of the webpage itself, but the print function doesn't really do anything on the front end -- we're assuming it's going into the backend to create the webpage
-We think the print(__name__) points to the specific part of the app.
-print statements only show up after you close the webpage (on the console) -- weird b/c return is after the print (? strange)
-runs in a webpage
-internally generates html code as well
-runs locally
-you can run the virtual environment from even outside the directory/virtual env
-py works instead of python too
-you need to reference a global variable in a method if you definied it outside of that method
-you can format html in a simpler way by putting it in the return statement
-the app route shows where relative to the website this runs, so / is the root and /hi is the url/hi

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
"""
    global i
    i += 1
    print(i)
    return(f"<h1>abc: {i}<h1>hello <a href=hi target=_blank>This is a link</a>")
"""
app.run()                                # Q5: Where have you seen similar constructs in other languages?
                                            #When calling a method of another class, this type of syntax is typically used.
                                            #Perhaps it is calling a static method since no objects seems to be created.
