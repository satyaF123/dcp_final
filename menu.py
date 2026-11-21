import pandas as pd
df = pd.read_csv('dcp26_a00047588.csv')

flag = True
while flag == True:
    choice = int(input("enter your choice\n"
    "1:new row\n"
    "2:append row\n"
    "3:delete row\n"
    "4:quit\n"))
    if choice == 1:
        item_name = str(input("enter the item name: ")).strip()
        item_name = item_name[0].upper() + item_name[1:]
        category = str(input("enter the item category: ")).strip()
        date = str(input("enter purchase date: ")).strip()
        amount = float(input("enter amount spent: "))
        need = int(input("needed?:1 for yes , 0 for no"))
        if need == 1:
            need = "Yes"
        else:
            need = "No"
        quantity = float(input("enter the quantity: "))
        unit = str(input("enter the unit: ")).strip()
        unit_price = amount/quantity
        store = str(input("enter the store: ")).strip()
        discount = int(input("discount?:1 for yes , 0 for no ")).strip()
        if discount == 1:
            discount = "Yes"
        else:
            discount = "No"
        df.loc[len(df)] = [item_name,category,date,"€ "+str(amount),need,quantity,unit,"€ "+str(unit_price),store,discount]
        df.to_csv('dcp26_a00047588.csv', index=False)
        flag = False
    elif choice == 2:
        row = int(input("row number to append: "))
        print(df.iloc[row])
        flag1 = True
        while flag1 == True:
            column = int(input("which column to append?: " \
            "1:item name\n" \
            "2:category\n" \
            "3:date\n" \
            "4:purchased\n" \
            "5:amount\n" \
            "6:needed\n" \
            "7:quantity\n" \
            "8:unit\n" \
            "9:store\n" \
            "10:discount\n"))
            flag1 = False
        break



