def your_name(name):
    names = ['DeNICE', 'AAAARON', 'BALAKEY']
    if name in names:
        print("thank you come again")
    else:
        print("YOU DONE MESSED UP SON!!! GO TO THE PRINCIPAL'S OFFICE")
        
def get_your_name():
    return input("tell me your name:")


name = get_your_name()
print(your_name(name))


