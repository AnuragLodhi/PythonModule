#:Python:
#Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

#It is used for:

#web development (server-side),
#software development,
#mathematics,
#system scripting.


1) print command:
    print("Hello World!")

2) #python install https://www.python.org/downloads/

3) exit() to quit the interface.

4) extension .py

5) #Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
   #Python uses indentation to indicate a block of code.
    
6) Comments: Single line #This is a comment
    """multi
        line
            comment."""

6) Variables:
    x = 5 #print(x)
    y = "Hello World!" 
    
    Casting:
        #var_name = var_type()
        x=str(3)
        y=int(3)
        z=float(3.14)
        
        type() #Function returns the data type of variable.
        
    #" " same as ' '
    #Variable names are case sensitive.
    
    Assigning values to variables:
    
        x ,y , z = 1, 2, 3 # x = 1, y = 2, z = 3
    
        x = y = z = 10 #Same value to multiple variables
    
        fruits = ["Apple", "Banana", "Orange"] #list
        x, y, z = fruits #unpacking list
    
    #print() function can be used to output variables.
    
    Global Variable:
        Variables that are created outside of a function are known as global variables.
        
        x = "awesome"

    def myfunc():
        x = "fantastic"
        print("Python is " + x) #Python in fantastic

    myfunc()
    print("Python is " + x) #Python is awesome
    
    #To create a Global Variable inside a function use "global" keywoard.
    #Also, use the global keyword if you want to change a global variable inside a function.

7) Data Types:
    Text Type:	    str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	    set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
    
    #type() function can be used to get the data type of variable.
    
    x = "Hello" #Data type not specified
    x = str("Hello") #Data type specified
    
    a)Numeric:
    
        int: Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
        float: Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
        complex: Complex numbers are written with a "j" as the imaginary part.
    
        Conversion:
         x = 1    # int
         y = 2.8  # float
         z = 1j   # complex

         #convert from int to float:
         a = float(x)

         #convert from float to int:
         b = int(y)
    
         #convert from int to complex:
         c = complex(x)
     
        #You cannot convert complex numbers into another number type.
     
    b)Strings: