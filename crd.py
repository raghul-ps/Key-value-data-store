import json

keyval = dict()
def create():
    email = input("Enter email id: ")
    name = input("Enter your name: ")
    keyval[email]=name
    #for k,v in keyval.items():
    #    print(k,v)
    with open("values.json", "r+") as f:
        data = json.load(f)
        data.update(keyval)
        f.seek(0)
        json.dump(data, f)
    print("***CREATED***")


def search():
    mail = input("Enter mail id: ")
    with open("values.json", "r") as f:
        data = json.load(f)
    if mail in data:
        print("****FOUND***")
        print("Owner of the mail ",mail, " is",data[mail])
        print("\n")
    else:
        print("****NOT FOUND****")


def delete():
    mail = input("Enter mail id: ")
    with open('values.json', 'r') as f:
        values = json.load(f)

    if mail in values:
        del values[mail]
        values.update()
        print("****DELETED***")
    else:
        print("*There is no account**")

    with open('data.json', 'w') as f:
        values = json.dump(values, f)


while True:
    print("Enter what you want to do")
    print("1.Create")
    print("2.Search")
    print("3.Delete")
    x = int(input())
    if(x==1):
        create()
        #print("created")
    elif(x==2):
        search()
        #print("Searched")
    elif(x==3):
        delete()
        #print("deleted")
    else:
        print("enter valid input")
                
