def read_from_database():
    file = open("test6-3.txt")

    for line in file:
        product = line.split(",")
        product = {"id" : product[0] , "name" :product[1],
                   "price" :product[2] , "count" :product[3]}
        
        products.append(product)
        print("product:" , product)

    
def add():
    id = input("enter id :")
    name = input("enter name :")
    price = input("enter price :")
    count = input("enter count :")
    product = {"id":id , "name":name ,"price": price , "count":count}
    products.append(product)
    print(products)

def edit():
    user_input = input("enter id kala :")
    for product in products:
        if user_input == product["id"]:
            print(product)
            print("1-name")
            print("2-price")
            print("3-count")
            user_select = int(input("select :"))
            user_edit = input("enter new item :")

            if user_select == 1:
                product["name"] = user_edit
                print(product)
                break

            if user_select == 2:
                product["price"] = user_edit
                print(product)
                break

            if user_select == 3:
                product["count"] = user_edit
                print("Information updated successfully")
                print(product)
                break
    else:
        print("not found")
        edit()




def buy():
    user_input = input("enter code kala :")
    for product in products:
        if user_input == product["id"]:
            print(product)
            number = int(input("enter tedad kala :"))
            mojoudi = int(product["count"])
            if number <= mojoudi:
                mojoudi -= number
                product["count"] = mojoudi
                print("kharid ba movafaghiyat anjam shod")

                break
            else:
                print("mojoudi kafi nist")
                buy()


    else:
        print("not found")
        buy()


    
    


def show_product():
    print("id \t name \t price \t count")
    for i in range(len(products)):
        print(products[i]["id"],"\t", products[i]["name"],"\t",products[i]["price"],"\t",products[i]["count"])


def delete():
    user_id = int(input("enter id kala for delete :"))
    for item in products:
        if user_id == int(item["id"]):
            products.remove(products[item])
            print("item has been delete successfuly")
            show_product()
            break

    else:
        print("not found")
        delete()

def write_to_database():
    file = open("test6-3.txt", "a")
    for product in products:
        file.write(product)
    file.close()

def search():
    user_input = input("enter keyword :")
    for product in products:
        if user_input == product["id"] or user_input == product["name"]:
            print(product)
            break
    else:
        print("not found")
        search()
        

def show_menu():

    print("1- add")
    print("2- edit")
    print("3- delete")
    print("4- buy")
    print("5- show product")
    print("6- search")
    print("7- exit")

products = []
read_from_database()


while True:
    show_menu()
    user_choice = int(input("select:"))

    if user_choice == 1:
        add()

    if user_choice == 2:
        edit()

    if user_choice == 3:
        delete()

    if user_choice == 4:
        buy()

    if user_choice == 5:
        show_product()

    if user_choice == 6:
        search()

    if user_choice == 7:
        write_to_database()
        exit()
