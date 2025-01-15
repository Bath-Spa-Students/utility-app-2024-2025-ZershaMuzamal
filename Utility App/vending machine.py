from prettytable import PrettyTable
import random
USER_NAME =     input("""
█▀█ █░░ █▀▀ ▄▀█ █▀ █▀▀   █▀▀ █▄░█ ▀█▀ █▀▀ █▀█   █▄█ █▀█ █░█ █▀█   █▄░█ ▄▀█ █▀▄▀█ █▀▀ ▀
█▀▀ █▄▄ ██▄ █▀█ ▄█ ██▄   ██▄ █░▀█ ░█░ ██▄ █▀▄   ░█░ █▄█ █▄█ █▀▄   █░▀█ █▀█ █░▀░█ ██▄ ▄""")  #TAKING USER NAME AS INPUT
#DISPLAYING WELCOME MESSAGE
print("""
╭━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━╮
╰━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━╯""")
print("""                  🅸                                                                                                                         🅸
                  🅸    ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░  ███╗░░░███╗██╗░░░██╗           🅸
                  🅸    ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗  ████╗░████║╚██╗░██╔╝           🅸
                  🅸    ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║  ██╔████╔██║░╚████╔╝░           🅸
                  🅸    ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║  ██║╚██╔╝██║░░╚██╔╝░░           🅸
                  🅸    ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝  ██║░╚═╝░██║░░░██║░░░           🅸
                  🅸    ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░  ╚═╝░░░░░╚═╝░░░╚═╝░░░           🅸
                  🅸                                                                                                                         🅸
                  🅸    ██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗     🅸
                  🅸    ██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝     🅸
                  🅸    ╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░     🅸
                  🅸    ░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░     🅸
                  🅸    ░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗     🅸
                  🅸    ░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝     🅸      """)
print("""                  🅸                                                                                                                         🅸
╭━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━╮
╰━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━╯""") 
# ASCII ART FOR DIFFERENT ITEMS
text_art = {
    'Snacks': """
█▀ █▄░█ ▄▀█ █▀▀ █▄▀ █▀
▄█ █░▀█ █▀█ █▄▄ █░█ ▄█""",
    'Drinks': """
█▀▄ █▀█ █ █▄░█ █▄▀ █▀
█▄▀ █▀▄ █ █░▀█ █░█ ▄█""",
    'Chips': """
█▀▀ █░█ █ █▀█ █▀
█▄▄ █▀█ █ █▀▀ ▄█"""}
#MENU AS DICTIONARY
Items = {
    'Snacks': [{
        'PRODUCT CODE' : 'X1', 'PRODUCT NAME': 'FERRERO ROCHER CHOCOLATE'  , 'PRODUCT PRICE'  : '47.56 (AED)', 'PRODUCT STOCK': 20},
        {'PRODUCT CODE': 'X2', 'PRODUCT NAME': 'PISTACHIO KUNAFA CHOCOLATE', 'PRODUCT PRICE'  : '35.38 (AED)', 'PRODUCT STOCK': 20},
        {'PRODUCT CODE': 'X3', 'PRODUCT NAME': 'CLASSIC CARAMAL POPCORN   ', 'PRODUCT PRICE'  : '15.45 (AED)', 'PRODUCT STOCK': 20},
        {'PRODUCT CODE': 'X4', 'PRODUCT NAME': 'SALTED BUTTER POPCORN'     , 'PRODUCT PRICE'  : '16.24 (AED)', 'PRODUCT STOCK': 20},
        {'PRODUCT CODE': 'X5', 'PRODUCT NAME': 'CHOCOLATE CHIP COOKIE'     , 'PRODUCT PRICE'  : '10.50 (AED)', 'PRODUCT STOCK': 20}],
    'Drinks': [ {
        'PRODUCT CODE' : 'Y1', 'PRODUCT NAME': 'PEPSI'  , 'PRODUCT PRICE': '3.45', 'PRODUCT STOCK': 20},
        {'PRODUCT CODE': 'Y2', 'PRODUCT NAME': 'COLA'   , 'PRODUCT PRICE': '3.45', 'PRODUCT STOCK': 20},
        {'PRODUCT CODE': 'Y3', 'PRODUCT NAME': 'DEW'    , 'PRODUCT PRICE': '3.45', 'PRODUCT STOCK': 20},
        {'PRODUCT CODE': 'Y4', 'PRODUCT NAME': 'TEA'    , 'PRODUCT PRICE': '2.45', 'PRODUCT STOCK': 20},
        {'PRODUCT CODE': 'Y5', 'PRODUCT NAME': 'COFFEE' , 'PRODUCT PRICE': '3.45', 'PRODUCT STOCK': 20}],
    'Chips': [{
        'PRODUCT CODE': 'Z1' , 'PRODUCT NAME': 'LAYS'     , 'PRODUCT PRICE': '5.00', 'PRODUCT STOCK': 20},
        {'PRODUCT CODE': 'Z2', 'PRODUCT NAME': 'PRINGLES' , 'PRODUCT PRICE': '5.00', 'PRODUCT STOCK': 20},
        {'PRODUCT CODE': 'Z3', 'PRODUCT NAME': 'TAKIES'   , 'PRODUCT PRICE': '5.00', 'PRODUCT STOCK': 20},
        {'PRODUCT CODE': 'Z4', 'PRODUCT NAME': 'CHEETOS'  , 'PRODUCT PRICE': '5.00', 'PRODUCT STOCK': 20},
        {'PRODUCT CODE': 'Z5', 'PRODUCT NAME': 'RIPPLES'  , 'PRODUCT PRICE': '5.00', 'PRODUCT STOCK': 20}]}
#FUNTION TO DISPLAY MENU IN TABLE
def DISPLAY_MENU(Items):
    for category, products in Items.items(): # USING FOR LOOP FOR CATEGORY AND PRODUCTS
        print(text_art.get(category)) #PRINT SPECIFIC TEXT ART OR CATEGORY
        Table = PrettyTable() #CREATING A NEW TABLE OBJECT FROM PRETTYTABLE 
        Table.field_names = ['PRODUCT CODE', 'PRODUCT NAME', 'PRODUCT PRICE', 'PRODUCT STOCK'] #DISPLAYING COLUMN NAMES
        for Product in products: #LOOP THROUGHT WHICH EACH PRODUCT ADD TO ROWS
            Table.add_row([Product['PRODUCT CODE'], Product['PRODUCT NAME'], Product['PRODUCT PRICE'], Product['PRODUCT STOCK']]) #ADDING THE PRODUCT DETAILS
        print(Table) #PRINTING THE TABLE
#FUNTION FOR UPDATING STOCKS AFTER PURCHASES
def STOCK_UPDATE(Items, PRODUCT_CODE): 
    for category, Products in Items.items():  #ILERTRATING THROUGH EACH CATEGORY
        for Product in Products:  #ILERTRATING THROUGH EACH PRODUCT IN PRODUCT LIST
            if Product['PRODUCT CODE'] == PRODUCT_CODE: #IF THE ENTERED PRODUCT CODEIS SAME AS THE REAL CODE
                if Product['PRODUCT STOCK'] > 0: #CHECKING IF THE PRODUCT IS IN STOCK
                    Product['PRODUCT STOCK'] -= 1 #DEDUCTING THE PRODUCT STOCK BY 1
                    print(f" STOCK UPDATE! {Product['PRODUCT NAME']} STOCK IS NOW {Product['PRODUCT STOCK']}.") #PRINTING THE PRODUCT INFORMATION
                else:
                    print(f"𝓢𝓞𝓡𝓡𝓨, {Product['PRODUCT NAME']} 𝓘𝓢 𝓞𝓤𝓣 𝓞𝓕 𝓢𝓣𝓞𝓒𝓚.") #IF THE PRODUCT IS OUT OF STOCK
                return

#GENERATING ORDER ID FOR EACH COSTOMER
def ORDER_ID():
    return USER_NAME + str(random.randint(1, 1000)) # RESULT WILL BE INPUT NAME BY UESR AND RANDOM NUMBERS

#MAIN VENDING MACHINE 
def VENDING_MACHINE():
    Cart = []  #TO ADD AND STORE ITEMS
    TOTAL_AMOUNT = 0  #FOR THE FINAL PAYMENT IF MULTIPLE ITEMS ARE ADDED
    while True: #IFINITY LOOP TILL THE USER DECIDES TO STOP
        DISPLAY_MENU(Items) #DISPLAYING THE MENU OF UPDATED STOCK ITEMS
        SELECTED_ITEM_CODE = input(f"𝓟𝓛𝓔𝓐𝓢𝓔 𝓔𝓝𝓣𝓔𝓡 𝓣𝓗𝓔 𝓟𝓡𝓞𝓓𝓤𝓒𝓣 𝓒𝓞𝓓𝓔 𝓨𝓞𝓤 𝓦𝓘𝓢𝓗 𝓣𝓞 𝓑𝓤𝓨 {USER_NAME} ((𝓔𝓧𝓐𝓜𝓟𝓛𝓔= 𝓧1,𝓨2,𝓩3)): ").upper() #ASKING FOE CODE
        PROD_FOUND = False #CHECKING THE CODE
        for Category, Products in Items.items(): #ITERATE THROUGH EACH PRODUCT IN DICTIONARY
            for Product in Products: #ITERATE THROUGH EACH PRODUCT IN CATEGORY
                if Product['PRODUCT CODE'] == SELECTED_ITEM_CODE: #CHECHING IF THE PRODUCT CODE MATCHS EXACTLY
                    PROD_FOUND = True #IF THE PRODUCT IS FOUND
                    PRODUCT_SELECTED = Product #STORING THE PRODUCT
                    print(f"\nYOU HAVE SELECTED {PRODUCT_SELECTED['PRODUCT NAME']}.") #PRITING THE PRODUCT NAME
                    print(f"PRICE: {PRODUCT_SELECTED['PRODUCT PRICE']}") #PRINTING THE PRODUCT PRICE
                    print(f"STOCK AVAILABLE: {PRODUCT_SELECTED['PRODUCT STOCK']}") #PRINTNG THE AVAILABLE STOCK
                    if PRODUCT_SELECTED['PRODUCT STOCK'] > 0: #CHECKING IF THE PRODUCT IN STOCK
                        AMOUNT_DUE = float(PRODUCT_SELECTED['PRODUCT PRICE'].split()[0])  #EXTRACTING THE PRICE AS FLOAT
                        Order_ID = ORDER_ID()  #MAKING THE USER ID
                        print(f"𝓨𝓞𝓤𝓡 𝓞𝓡𝓓𝓔𝓡 𝓝𝓤𝓜𝓑𝓔𝓡 𝓘𝓢:{Order_ID}") #PRINTHING THE USER ID
                        while AMOUNT_DUE > 0: #WHILE LOOP FOR DUE AMOUNT
                            try:
                                PAYMENT_WAY = input("𝓦𝓞𝓤𝓛𝓓 𝓨𝓞𝓤 𝓛𝓘𝓚𝓔 𝓣𝓞 𝓟𝓐𝓨 𝓒𝓐𝓢𝓗 𝓞𝓡 𝓒𝓐𝓡𝓓❓").strip().lower() #ASKING PAYMENT METHOD
                                if PAYMENT_WAY == "CASH".lower(): # IF THE USER CHOOSE CASH
                                    PAYMENT = float(input(f"𝓟𝓛𝓔𝓐𝓢𝓔 𝓘𝓝𝓢𝓔𝓡𝓣 {AMOUNT_DUE:.2f} 𝓐𝓔𝓓: ")) #TAKING PAYMENT IN CASH
                                    if PAYMENT >= AMOUNT_DUE: #CHECKING IF THE AMOUNT IS MORE
                                        CHANGE = PAYMENT - AMOUNT_DUE #CREATING CHANGE CONCEPT
                                        print(f"𝓣𝓗𝓐𝓝𝓚 𝓨𝓞𝓤 𝓕𝓞𝓡 𝓨𝓞𝓤𝓡 𝓟𝓤𝓡𝓒𝓗𝓐𝓢𝓔❗ 𝓨𝓞𝓤𝓡 𝓒𝓗𝓐𝓝𝓖𝓔 𝓘𝓢 {CHANGE:.2f} 𝓐𝓔𝓓.") #PRINTING CHANGE STATEMENT
                                        STOCK_UPDATE(Items, SELECTED_ITEM_CODE)  #UPDATING STOCK AFTER PURCHASE
                                        Cart.append({'ORDER ID': Order_ID, 'PRODUCT NAME': PRODUCT_SELECTED['PRODUCT NAME'], 'PRICE': PRODUCT_SELECTED['PRODUCT PRICE'],
                                         'QUANTITY': 1,'AMOUNT PAID': PAYMENT, 'CHANGE': CHANGE}) #ADDING PURCHASED ITEM TO THE CART
                                        TOTAL_AMOUNT += AMOUNT_DUE  #ADDING PRICE TO THE TOTAL AMOUNT
                                        break
                                    else:
                                        NEW_AMOUNT = AMOUNT_DUE - PAYMENT # CHECKING IF THE PAYMENT IS MORE
                                        print(f"𝓘𝓝𝓢𝓤𝓕𝓘𝓒𝓘𝓔𝓝𝓣 𝓟𝓐𝓨𝓜𝓔𝓝𝓣. 𝓟𝓛𝓔𝓐𝓢𝓔 𝓐𝓓𝓓 {NEW_AMOUNT:.2f} 𝓐𝓔𝓓 𝓜𝓞𝓡𝓔.")# PRINT STATEMENT FOR MORE PAYMENT
                                        AMOUNT_DUE = NEW_AMOUNT  #NEW AMOUNT FOR MORE PAYMENT
                                elif PAYMENT_WAY == "CARD".lower(): #IF USER CHOOSE CARD
                                    input(f"𝓟𝓛𝓔𝓐𝓢𝓔 𝓘𝓝𝓢𝓔𝓡𝓣 𝓨𝓞𝓤𝓡 𝓒𝓐𝓡𝓓. 𝓨𝓞𝓤𝓡 𝓟𝓐𝓨𝓜𝓔𝓝𝓣 𝓐𝓜𝓞𝓤𝓝𝓣 𝓘𝓢 {AMOUNT_DUE:.2f} 𝓐𝓔𝓓 (𝓦𝓡𝓘𝓣𝓔 𝓨𝓔𝓢 𝓦𝓗𝓔𝓝 𝓨𝓞𝓤 𝓐𝓡𝓔 𝓓𝓞𝓝𝓔):") #PRINT STATEMENT FOR CARD PAYMENT
                                    STOCK_UPDATE(Items, SELECTED_ITEM_CODE)  #STOCK UPDATE
                                    Cart.append({'ORDER ID': Order_ID, 'PRODUCT NAME': PRODUCT_SELECTED['PRODUCT NAME'], 'PRICE': PRODUCT_SELECTED['PRODUCT PRICE'],
                                     'QUANTITY': 1}) #ADDING PURCHASD ITEM TO THE CART
                                    TOTAL_AMOUNT += AMOUNT_DUE  #ADDDING THE TOTAL PRICE
                                    break
                                else:
                                    print("𝓘𝓝𝓥𝓐𝓛𝓘𝓓 𝓟𝓐𝓨𝓜𝓔𝓝𝓣 𝓜𝓔𝓣𝓗𝓞𝓓. 𝓟𝓛𝓔𝓐𝓢𝓔 𝓣𝓡𝓨 𝓐𝓖𝓐𝓘𝓝.") #PRINT STATEMENT FOR INVALID PAYMENT METHOD
                            except ValueError:
                                print("𝓘𝓝𝓥𝓐𝓛𝓘𝓓 𝓘𝓝𝓟𝓤𝓣 𝓟𝓛𝓔𝓐𝓢𝓔 𝓔𝓝𝓣𝓔𝓡 𝓐 𝓥𝓐𝓛𝓘𝓓 𝓐𝓜𝓞𝓤𝓝𝓣.") #PRINT STATEMENT FOR INVLID AMOUNT
                        break
        if not PROD_FOUND: #IF THE PRODUCT IS NOT FOUND
            print("𝓘𝓝𝓥𝓐𝓛𝓘𝓓 𝓟𝓡𝓞𝓓𝓤𝓒𝓣 𝓒𝓞𝓓𝓔 ❗ 𝓟𝓛𝓔𝓐𝓢𝓔 𝓣𝓡𝓨 𝓐𝓖𝓐𝓘𝓝.") #PRINT STATEMENT FOR ASKING FOR NEW PRODUCT
        MORE_ITEMS = input("𝓓𝓞 𝓨𝓞𝓤 𝓦𝓐𝓝𝓣 𝓣𝓞 𝓑𝓨 𝓜𝓞𝓡𝓔 𝓘𝓣𝓔𝓜𝓢❓ (𝓨𝓔𝓢/𝓝𝓞):").strip().lower() #PRINT STATEMENT FOR ASKING FOR EXTRA ITEMS
        if MORE_ITEMS != "yes": #IF USER SAY NO
            print("""
▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█   █▀▀ █▀█ █▀█   █▀ █░█ █▀█ █▀█ █▀█ █ █▄░█ █▀▀   █░█░█ █ ▀█▀ █░█   █░█ █▀ █
░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█   █▀░ █▄█ █▀▄   ▄█ █▀█ █▄█ █▀▀ █▀▀ █ █░▀█ █▄█   ▀▄▀▄▀ █ ░█░ █▀█   █▄█ ▄█ ▄""")#THANKYOU PRINT STATEMENT
            print(f"𝓣𝓞𝓣𝓐𝓛 𝓐𝓜𝓞𝓤𝓝𝓣: {TOTAL_AMOUNT:.2f} 𝓐𝓔𝓓") #TOTAL AMOUNT PRINT STATEMENT
            print("𝓐𝓛𝓛 𝓣𝓗𝓔 𝓘𝓣𝓔𝓝𝓢 𝓗𝓐𝓢 𝓑𝓔𝓔𝓝 𝓓𝓔𝓢𝓟𝓔𝓝𝓢𝓔𝓓. 𝓟𝓛𝓔𝓐𝓢𝓔 𝓒𝓞𝓛𝓛𝓔𝓒𝓣 𝓘𝓣")
            print("""
█░█ █▀▀ █▀█ █▀▀   █ █▀   █▄█ █▀█ █░█ █▀█   █▀▀ ▄▀█ █▀█ ▀█▀   █▀ █░█ █▀▄▀█ █▀▄▀█ ▄▀█ █▀█ █▄█ ▀
█▀█ ██▄ █▀▄ ██▄   █ ▄█   ░█░ █▄█ █▄█ █▀▄   █▄▄ █▀█ █▀▄ ░█░   ▄█ █▄█ █░▀░█ █░▀░█ █▀█ █▀▄ ░█░ ▄""") #CART DETAILS PRINT STATEMENT
            Table = PrettyTable() #MAKING TABLE FOR CART
            Table.field_names = ['ORDER ID', 'PRODUCT NAME', 'PRICE', 'QUANTITY', 'CHANGE'] #CHOOSING FEILD NAMES OF TH FIELDS
            for item in Cart: #FOR LOOP FOR ALL THE ITEMS IN CART
                Table.add_row([item['ORDER ID'], item['PRODUCT NAME'], item['PRICE'], item['QUANTITY'],  item.get('CHANGE', '-')]) #PRINTING THE ROWS
            print(Table) #PRINTING THE TABLE
            break
VENDING_MACHINE()
