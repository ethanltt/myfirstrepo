def secritcode (pasword):
    if pasword == "0000":
        return "correced"
    elif pasword == "1234" :
        return "incorect"
    else:
        return "you done mess up son!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" 
def get_user_pasword():
    return input("please enter pasword: ")
  
pasword = get_user_pasword()
print(secritcode(pasword))
print(f"My secritcode is {pasword}")