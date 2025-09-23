# Here we are going to create a project of Email Validation using string function in python 

email = input("Enter Your Email Id :") #g@g.in
k,j,d = 0,0,0
if len(email)>=6:    # (1) length of the email minimum 6 hona chaiye 
    if email[0].isalpha():  # (2) first character is Alphabet
        if ( "@" in email) and (email.count("@")==1):   # (3) count @ in email
            if(email[-4]==".") ^ (email[-3]=="."):     # (4) use . in email
                for i in email:
                    if i == i.isspace():   #(5)
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():  #(5)
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "-"or i == "." or i== "@":
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email Id 5")
                else :
                    print("Write Email Id")
            else:
                print("Wrong Email Id 4")
                
        else :
            print("Wrong Email Id 3")    
    else:
        print("Wrong Email Id 2")
else:
    print("Wrong Emial Id 1")

