#med2
email=input("Enter email: ")
new_domain=input("Enter new domain: ")
old_domain=input("Enter old domain: ")
def replace_domain(email,new_domain,old_domain):
    if new_domain in email:
        c=email
        print("Unchanged: ",c)
    else:
        c=""
        for i in range(0,len(email),1):
            if email[i]=="@":
                c+=email[i]
                break
            else:
                c+=email[i]
        c=c+new_domain
        print("Changed: ",c)
replace_domain(email,new_domain,old_domain)        