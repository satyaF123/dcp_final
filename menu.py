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
        item_name = str(input("enter the item name: ")).strip().upper()
        category = str(input("enter the item category: ")).strip()
        category = category[0].upper() + category[1:]
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
        discount = int(input("discount?:1 for yes , 0 for no "))
        if discount == 1:
            discount = "Yes"
        else:
            discount = "No"
        df.loc[len(df)] = [item_name,category,date,"€ "+str(amount),need,quantity,unit,"€ "+str(round(unit_price,2)),store,discount]
        df.to_csv('dcp26_a00047588.csv', index=False)
    elif choice == 2:
        row = int(input("row number to append: "))
        print(df.iloc[row])
        flag1 = True
        while flag1 == True:
            column = int(input("which column to append?: \n" \
            "1:item name\n" \
            "2:category\n" \
            "3:date\n" \
            "4:amount\n" \
            "5:needed\n" \
            "6:quantity\n" \
            "7:unit\n" \
            "8:store\n" \
            "9:discount\n"
            "10:done\n"))
            if column == 1:
                item_name = str(input("enter the new value")).strip().upper()
                df.loc[row, "Item name"] = item_name
                df.to_csv('dcp26_a00047588.csv', index=False)
            elif column == 2:
                cat = str(input("enter the new value")).strip()
                cat = cat[0].upper() + cat[1:]
                df.loc[row, "Category"] = cat
                df.to_csv('dcp26_a00047588.csv', index=False)
            elif column == 3:
                dat = str(input("enter the new value"))
                df.loc[row, "Date purchased"] = dat
                df.to_csv('dcp26_a00047588.csv', index=False)
            elif column == 4:
                amount = float(input("enter the new value"))
                df.loc[row, "amount"] = "€ " + str(amount)
                qty = df.loc[row, "Quantity"]
                df.loc[row, "Unit price"] = "€ " + str(round(amount / qty, 2))
                df.to_csv('dcp26_a00047588.csv', index=False)
            elif column == 5:
                need = int(input("needed?:1 for yes , 0 for no"))
                if need == 1:
                    df.loc[row, "needed"] = "Yes"
                else:
                    df.loc[row, "needed"] = "No"
                df.to_csv('dcp26_a00047588.csv', index=False)
            elif column == 6:
                quantity = float(input("enter the new value"))
                df.loc[row, "Quantity"] = quantity
                amt = float(df.loc[row, "amount"].replace("€", "").strip())
                df.loc[row, "Unit price"] = "€ " + str(round(amt / quantity, 2))
                df.to_csv('dcp26_a00047588.csv', index=False)
            elif column == 7:
                unit = str(input("enter the new value")).strip()
                df.loc[row, "Unit"] = unit
                df.to_csv('dcp26_a00047588.csv', index=False)
            elif column == 8:
                store = str(input("enter the new value")).strip()
                df.loc[row, "store"] = store
                df.to_csv('dcp26_a00047588.csv', index=False)
            elif column == 9:
                discount = int(input("discount?:1 for yes , 0 for no "))
                if discount == 1:
                    df.loc[row, "Discount"] = "Yes"
                else:
                    df.loc[row, "Discount"] = "No"
                df.to_csv('dcp26_a00047588.csv', index=False)
            elif column == 10:
                flag1 = False
    elif choice == 3:
        row = int(input("row number to delete: "))
        print(df.iloc[row])
        df = df.drop(row).reset_index(drop=True)
        df.to_csv('dcp26_a00047588.csv', index=False)
    elif choice == 4:
        flag = False


            
        



