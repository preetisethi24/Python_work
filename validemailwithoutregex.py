def validemail(email):
    try:
        username,url=email.split("@")
        domain,extn=url.split(".")
    except ValueError:
        return False
        
    if username.replace("_","").replace("-","").isalnum()==False:
        return False
    elif domain.isalnum()==False:
        return False
    elif len(extn)<1 or len(extn)>3:
        return False
    else:
        return True
    
    
print(validemail("preeti_sethi@gmail.com"))
    
