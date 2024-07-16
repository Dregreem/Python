import re

email=input("What is your Email?:").strip()
""" with +
if re.search(".+@.+",email):
    # To check whether there is something before and after the @
    #however it accepts email@ therefore we have to use + (there must be at least one thing)
    print("Valid")
else:
    print("Invalid")
"""

if re.search(r"^\w+@(\w+\.)?(com|edu|net)$",email,re.IGNORECASE):
    #with this backslash it will accept only the codes that has ..@edu..
    #if not we could have done ..@jkj.edu

    #The r prefix tells Python to treat the backslash as a literal 
    # character, making the pattern easier to read and write.

    #however this code could take a sentence as an input it does not take the email 

    #now with these it will only take an email address not a sentence

    #[kasd] this would mean that side could only have those characters
    #[^@] this would mean all charctes except these but we have erased . because it would be double knot
    #(r"^[^@]+@[^@]+\.edu$",email)

    #a-zA-Z0-9_ all the characters are accepted (r"^[a-zA-Z0-9_]]+@[^a-zA-Z0-9_]+\.edu$",email)
    # Or to use automatically use \w-- only includes word characteristics no spaces and no "."things

    #we could group the allowed possibilities (com|edu|net)

    #to avoid the problems for uppercase we might use email.lower() or the flags in the re.search function
    #re.IGNORECASE

    #(\w+\.)? this addition makes it possible to use kerem@harvard.std.ktb.edu.tr possible
    # all the written things can be there once or none makes it optional: (r"^\w+@(\w+\.)?(com|edu|net)$",email,re.IGNORECASE)

    print("Valid")
else:
    print("Invalid")

# Generally a library would be used
