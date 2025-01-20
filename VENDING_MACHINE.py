from prettytable import PrettyTable
import random
import colorama 
from colorama import Fore 
colorama.init(autoreset=True)
USER_NAME =     input(Fore.RED + """
█▀█ █░░ █▀▀ ▄▀█ █▀ █▀▀   █▀▀ █▄░█ ▀█▀ █▀▀ █▀█   █▄█ █▀█ █░█ █▀█   █▄░█ ▄▀█ █▀▄▀█ █▀▀ ▀
█▀▀ █▄▄ ██▄ █▀█ ▄█ ██▄   ██▄ █░▀█ ░█░ ██▄ █▀▄   ░█░ █▄█ █▄█ █▀▄   █░▀█ █▀█ █░▀░█ ██▄ ▄""") #TAKING USER NAME AS INPUT
#DISPLAYING WELCOME MESSAGE
print(Fore.CYAN + """
╭━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━╮
╰━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━╯""")
print(Fore.RED +"""                 🎀                                                                                                                        🎀
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
print(Fore.CYAN +"""                  🎀                                                                                                                        🎀
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
        print(Fore.RED +text_art.get(category)) #PRINT SPECIFIC TEXT ART OR CATEGORY
        Table = PrettyTable() #CREATING A NEW TABLE OBJECT FROM PRETTYTABLE 
        Table.field_names = [Fore.GREEN + 'PRODUCT CODE',Fore.GREEN +  'PRODUCT NAME',Fore.GREEN +  'PRODUCT PRICE',Fore.GREEN +  'PRODUCT STOCK'] #DISPLAYING COLUMN NAMES
        for Product in products: #LOOP THROUGHT WHICH EACH PRODUCT ADD TO ROWS
            Table.add_row([Fore.CYAN + Product['PRODUCT CODE'], Product['PRODUCT NAME'], Product['PRODUCT PRICE'], Product['PRODUCT STOCK']]) #ADDING THE PRODUCT DETAILS
        print(Table) #PRINTING THE TABLE
#FUNTION FOR UPDATING STOCKS AFTER PURCHASES
def STOCK_UPDATE(Items, PRODUCT_CODE): 
    for category, Products in Items.items():  #ILERTRATING THROUGH EACH CATEGORY
        for Product in Products:  #ILERTRATING THROUGH EACH PRODUCT IN PRODUCT LIST
            if Product['PRODUCT CODE'] == PRODUCT_CODE: #IF THE ENTERED PRODUCT CODEIS SAME AS THE REAL CODE
                if Product['PRODUCT STOCK'] > 0: #CHECKING IF THE PRODUCT IS IN STOCK
                    Product['PRODUCT STOCK'] -= 1 #DEDUCTING THE PRODUCT STOCK BY 1
                    print(Fore.CYAN +f" STOCK UPDATE! {Product['PRODUCT NAME']} STOCK IS NOW {Product['PRODUCT STOCK']}.") #PRINTING THE PRODUCT INFORMATION
                else:
                    print(Fore.RED +f"𝓢𝓞𝓡𝓡𝓨, {Product['PRODUCT NAME']} 𝓘𝓢 𝓞𝓤𝓣 𝓞𝓕 𝓢𝓣𝓞𝓒𝓚.") #IF THE PRODUCT IS OUT OF STOCK
                return
#GENERATING ORDER ID FOR EACH COSTOMER
def ORDER_ID():
    return USER_NAME + str(random.randint(1, 1000)) # RESULT WILL BE INPUT NAME BY UESR AND RANDOM NUMBERS
def suggesteditem(): #FUNTION FOR SUGGESTED ITEMS
    SUGGESTED_CATGORIES = random.choice(list(Items.keys())) #CHOOSING THE CATEGORY
    SUGGESTED_PRODUCTS = random.choice(Items[SUGGESTED_CATGORIES]) #CHOOSING THE PRODUCT
    return f"{SUGGESTED_PRODUCTS['PRODUCT NAME']} (Code: {SUGGESTED_PRODUCTS['PRODUCT CODE']}, Price: {SUGGESTED_PRODUCTS['PRODUCT PRICE']})"

#MAIN VENDING MACHINE 
def VENDING_MACHINE():
    Cart = []  #TO ADD AND STORE ITEMS
    TOTAL_AMOUNT = 0  #FOR THE FINAL PAYMENT IF MULTIPLE ITEMS ARE ADDED
    while True: #IFINITY LOOP TILL THE USER DECIDES TO STOP
        DISPLAY_MENU(Items) #DISPLAYING THE MENU OF UPDATED STOCK ITEMS
        SELECTED_ITEM_CODE = input(Fore.CYAN +f"𝙋𝙇𝙀𝘼𝙎𝙀 𝙀𝙉𝙏𝙀𝙍 𝙏𝙃𝙀 𝙋𝙍𝙊𝘿𝙐𝘾𝙏 𝘾𝙊𝘿𝙀 𝙔𝙊𝙐 𝙒 𝙊𝙐𝙇𝘿 𝙇𝙄𝙆𝙀 𝙏𝙊 𝙋𝙐𝙍𝘾𝙃𝘼𝙎𝙀 {USER_NAME} (🎀 𝐸𝒳𝒜𝑀𝒫𝐿𝐸 : 𝒳𝟣, 𝒴𝟤,𝒵𝟥 🎀): ").upper() #ASKING FOE CODE
        PROD_FOUND = False #CHECKING THE CODE
        for Category, Products in Items.items(): #ITERATE THROUGH EACH PRODUCT IN DICTIONARY
            for Product in Products: #ITERATE THROUGH EACH PRODUCT IN CATEGORY
                if Product['PRODUCT CODE'] == SELECTED_ITEM_CODE: #CHECHING IF THE PRODUCT CODE MATCHS EXACTLY
                    PROD_FOUND = True #IF THE PRODUCT IS FOUND
                    PRODUCT_SELECTED = Product #STORING THE PRODUCT
                    print(Fore.RED +f"\nYOU HAVE SELECTED {PRODUCT_SELECTED['PRODUCT NAME']}.") #PRITING THE PRODUCT NAME
                    print(Fore.CYAN +f"PRICE: {PRODUCT_SELECTED['PRODUCT PRICE']}") #PRINTING THE PRODUCT PRICE
                    print(Fore.RED +f"STOCK AVAILABLE: {PRODUCT_SELECTED['PRODUCT STOCK']}") #PRINTNG THE AVAILABLE STOCK
                    if PRODUCT_SELECTED['PRODUCT STOCK'] > 0: #CHECKING IF THE PRODUCT IN STOCK
                        AMOUNT_DUE = float(PRODUCT_SELECTED['PRODUCT PRICE'].split()[0])  #EXTRACTING THE PRICE AS FLOAT
                        Order_ID = ORDER_ID()  #MAKING THE USER ID
                        print(Fore.CYAN +f"𝙔𝙊𝙐𝙍 𝙊𝙍𝘿E𝙍 𝙉𝙐𝙈𝘽𝙀𝙍 𝙄𝙎 {Order_ID} 😍") #PRINTHING THE USER ID
                        while AMOUNT_DUE > 0: #WHILE LOOP FOR DUE AMOUNT
                            try:
                                PAYMENT_WAY = input(Fore.RED +"𝙒𝙊𝙐𝙇𝘿 𝙔𝙊𝙐 𝙇𝙄𝙆𝙀 𝙏𝙊 𝙋𝘼𝙔 𝘾𝘼𝙍𝘿 𝙊𝙍 𝘾𝘼𝙎𝙃❓💲").strip().lower() #ASKING PAYMENT METHOD
                                if PAYMENT_WAY == "CASH".lower(): # IF THE USER CHOOSE CASH
                                    PAYMENT = float(input(Fore.CYAN +f"𝙋𝙇𝙀𝘼𝙎𝙀 𝙄𝙉𝙎𝙀𝙍𝙏 {AMOUNT_DUE:.2f} 𝘼𝙀𝘿💞: ")) #TAKING PAYMENT IN CASH
                                    if PAYMENT >= AMOUNT_DUE: #CHECKING IF THE AMOUNT IS MORE
                                        CHANGE = PAYMENT - AMOUNT_DUE #CREATING CHANGE CONCEPT
                                        print(Fore.RED +f"𝙏𝙃𝘼𝙉𝙆 𝙔𝙊𝙐 𝙁𝙊𝙍 𝙔𝙊𝙐𝙍 𝙋𝙐𝙍𝘾𝙃𝘼𝙎𝙀 ❗ 𝙔𝙊𝙐𝙍 𝘾𝙃𝘼𝙉𝙂𝙀 𝙄𝙎{CHANGE:.2f} 𝘼𝙀𝘿.") #PRINTING CHANGE STATEMENT
                                        STOCK_UPDATE(Items, SELECTED_ITEM_CODE)  #UPDATING STOCK AFTER PURCHASE
                                        Cart.append({'ORDER ID': Order_ID, 'PRODUCT NAME': PRODUCT_SELECTED['PRODUCT NAME'], 'PRICE': PRODUCT_SELECTED['PRODUCT PRICE'],
                                         'QUANTITY': 1,'AMOUNT PAID': PAYMENT, 'CHANGE': CHANGE}) #ADDING PURCHASED ITEM TO THE CART
                                        TOTAL_AMOUNT += AMOUNT_DUE  #ADDING PRICE TO THE TOTAL AMOUNT
                                        break
                                    else:
                                        NEW_AMOUNT = AMOUNT_DUE - PAYMENT # CHECKING IF THE PAYMENT IS MORE
                                        print(Fore.CYAN +f"𝙄𝙉𝙎𝙐𝙁𝙁𝙄𝘾𝙀𝙉𝙏 𝙋𝘼𝙔𝙈𝙀𝙉𝙏. 𝙋𝙇𝙀𝘼𝙎𝙀 𝘼𝘿𝘿  {NEW_AMOUNT:.2f} 𝘼𝙀𝘿 𝙈𝙊𝙍𝙀🐼.")# PRINT STATEMENT FOR MORE PAYMENT
                                        AMOUNT_DUE = NEW_AMOUNT  #NEW AMOUNT FOR MORE PAYMENT
                                elif PAYMENT_WAY == "CARD".lower(): #IF USER CHOOSE CARD
                                    input(Fore.RED +f"𝙋𝙇𝙀𝘼𝙎𝙀 𝙄𝙉𝙎𝙀𝙍𝙏 𝙔𝙊𝙐𝙍 𝘾𝘼𝙍𝘿 𝙔𝙊𝙐𝙍 𝙋𝘼𝙔𝙈𝙀𝙉𝙏 𝘼𝙈𝙊𝙐𝙉𝙏 𝙄𝙎 {AMOUNT_DUE:.2f} 𝘼𝙀𝘿 (𝙒𝙍𝙄𝙏𝙀 𝙔𝙀𝙎 𝙒𝙃𝙀𝙉 𝙔𝙊𝙐𝙍 𝘿𝙊𝙉𝙀)😎:") #PRINT STATEMENT FOR CARD PAYMENT
                                    STOCK_UPDATE(Items, SELECTED_ITEM_CODE)  #STOCK UPDATE
                                    Cart.append({'ORDER ID': Order_ID, 'PRODUCT NAME': PRODUCT_SELECTED['PRODUCT NAME'], 'PRICE': PRODUCT_SELECTED['PRODUCT PRICE'],
                                     'QUANTITY': 1}) #ADDING PURCHASD ITEM TO THE CART
                                    TOTAL_AMOUNT += AMOUNT_DUE  #ADDDING THE TOTAL PRICE
                                    break
                                else:
                                    print(Fore.CYAN +"𝙄𝙉𝙑𝘼𝙇𝙄𝘿 𝙋𝘼𝙔𝙈𝙀𝙉𝙏 𝙈𝙀𝙏𝙃𝙊𝘿 𝙋𝙇𝙀𝘼𝙎𝙀 𝙏𝙍𝙔 𝘼𝙂𝘼𝙄𝙉🌞.") #PRINT STATEMENT FOR INVALID PAYMENT METHOD
                            except ValueError:
                                print(Fore.RED +"𝙄𝙉𝙑𝘼𝙇𝙄𝘿 𝙄𝙉𝙋𝙐𝙏 𝙋𝙇𝙀𝘼𝙎𝙀 𝙀𝙉𝙏𝙀𝙍 𝘼 𝙑𝘼𝙇𝙄𝘿 𝘼𝙈𝙊𝙐𝙉𝙏🐻.") #PRINT STATEMENT FOR INVLID AMOUNT
                        break
        if not PROD_FOUND :  #IF THE PRODUCT IS NOT FOUND
           print(Fore.CYAN + "𝙄𝙉𝙑𝘼𝙇𝙄𝘿 𝙋𝙍𝙊𝘿𝙐𝘾𝙏 𝘾𝙊𝘿𝙀 ❗ 𝙋𝙇𝙀𝘼𝙎𝙀 𝙏𝙍𝙔 𝘼𝙂𝘼𝙄𝙉.")  #PRINT STATEMENT FOR ASKING FOR NEW PRODUCT CODE
        SUGGEST_ITEM = suggesteditem() #MAKING THIS EQUAL
        print(Fore.CYAN + f"𝙒𝙀 𝙒𝙊𝙐𝙇𝘿 𝙎𝙐𝙂𝙂𝙀𝙎𝙏 𝙔𝙊𝙐 𝙏𝙊 𝙏𝙍𝙔: {SUGGEST_ITEM}👌 ") #PRINTING THE SUGGESTED ITEM
        MORE_ITEMS = input(Fore.RED + "𝘿𝙊 𝙔𝙊𝙐 𝙒𝘼𝙉𝙏 𝙏𝙊 𝘼𝘿𝘿 𝙈𝙊𝙍𝙀 𝙄𝙏𝙀𝙈𝙎❓ (𝙔𝙀𝙎/𝙉𝙊):").strip().lower()  #PRINT STATEMENT FOR MORE ITEMS
        if MORE_ITEMS != "yes":  # IF USER SAYS NO
           print(Fore.RED +"""
▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█   █▀▀ █▀█ █▀█   █▀ █░█ █▀█ █▀█ █▀█ █ █▄░█ █▀▀   █░█░█ █ ▀█▀ █░█   █░█ █▀ █
░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█   █▀░ █▄█ █▀▄   ▄█ █▀█ █▄█ █▀▀ █▀▀ █ █░▀█ █▄█   ▀▄▀▄▀ █ ░█░ █▀█   █▄█ ▄█ ▄""")#THANKYOU PRINT STATEMENT
           print(Fore.CYAN +f"𝙏𝙊𝙏𝘼𝙇 𝘼𝙈𝙊𝙐𝙉𝙏 𝙄𝙎: {TOTAL_AMOUNT:.2f} 𝘼𝙀𝘿") #TOTAL AMOUNT PRINT STATEMENT
           print(Fore.RED +"𝘼𝙇𝙇 𝙏𝙃𝙀 𝙄𝙏𝙀𝙈𝙎 𝙃𝘼𝙎 𝘽𝙀𝙀𝙉 𝘿𝙀𝙎𝙋𝙀𝙉𝘾𝙀𝘿. 𝙋𝙇𝙀𝘼𝙎𝙀 𝘾𝙊𝙇𝙇𝙀𝘾𝙏 𝙄𝙏🐣")
           print(Fore.CYAN +"""
█░█ █▀▀ █▀█ █▀▀   █ █▀   █▄█ █▀█ █░█ █▀█   █▀▀ ▄▀█ █▀█ ▀█▀   █▀ █░█ █▀▄▀█ █▀▄▀█ ▄▀█ █▀█ █▄█ ▀
█▀█ ██▄ █▀▄ ██▄   █ ▄█   ░█░ █▄█ █▄█ █▀▄   █▄▄ █▀█ █▀▄ ░█░   ▄█ █▄█ █░▀░█ █░▀░█ █▀█ █▀▄ ░█░ ▄""") #CART DETAILS PRINT STATEMENT
           Table = PrettyTable() #MAKING TABLE FOR CART
           Table.field_names = [Fore.GREEN + 'ORDER ID', 'PRODUCT NAME', 'PRICE', 'QUANTITY', 'CHANGE'] #CHOOSING FEILD NAMES OF TH FIELDS
           for item in Cart: #FOR LOOP FOR ALL THE ITEMS IN CART
                Table.add_row([Fore.RED + item['ORDER ID'], item['PRODUCT NAME'], item['PRICE'], item['QUANTITY'],  item.get('CHANGE', '-')]) #PRINTING THE ROWS
           print(Table) #PRINTING THE TABLE
           LUCKY_CHANCE = input(Fore.CYAN + "𝙒𝙊𝙐𝙇𝘿 𝙔𝙊𝙐 𝙇𝙄𝙆𝙀 𝙏𝙊 𝙋𝘼𝙔 🔟 𝘼𝙀𝘿 𝙁𝙊𝙍 𝘼 𝙍𝘼𝙉𝘿𝙊𝙈 𝙋𝙍𝙊𝘿𝙐𝘾𝙏 𝘼𝙉𝘿 𝙏𝙀𝙎𝙏 𝙔𝙊𝙐𝙍 𝙇𝙐𝘾𝙆? (𝙔𝙀𝙎/𝙉𝙊)🎮:").strip().lower()#GAME INTRO
           if LUCKY_CHANCE == "yes":  #ENSURING THE USER ANSWER IS CASE INSENSITIVE
                   LUCKY_CHANCE_MONEY = input(Fore.RED +"𝙋𝙇𝙀𝘼𝙎𝙀 𝙀𝙉𝙏𝙀𝙍 𝙀𝙓𝘼𝘾𝙏𝙇𝙔 🔟 𝘼𝙀𝘿 𝙏𝙊 𝙒𝙄𝙉 𝙏𝙃𝙄𝙎 𝙂𝘼𝙈𝙀(𝙀𝙭𝙖𝙢𝙥𝙡𝙚: 🔟):💰 ").strip()#ASKING MONEY FOR THE GAME
                   try:
                       if float(LUCKY_CHANCE_MONEY) == 10: #CONVERTING STRING INTO FLOAT FOR COMPARISON
                        print(Fore.GREEN + f"𝘾𝙊𝙉𝙍𝘼𝙏𝙀𝙎! 𝙔𝙊𝙐 𝙒𝙊𝙉 {SUGGEST_ITEM}. 𝙋𝙇𝙀𝘼𝙎𝙀 𝘾𝙊𝙇𝙇𝙀𝘾𝙏 𝙄𝙏 𝙒𝙄𝙏𝙃 𝙏𝙃𝙀 𝙊𝙏𝙃𝙀𝙍 𝙄𝙏𝙀𝙈𝙎🏅")#IF THE USER ENTERS THE RIGHT AMOUNT
                        break
                       else:
                        print(Fore.CYAN + "𝙏𝙃𝙀 𝙀𝙉𝙏𝙀𝙍𝙀𝘿 𝘼𝙈𝙊𝙐𝙉𝙏 𝙄𝙎 𝙉𝙊 🔟 𝘼𝙀𝘿. 𝘽𝙀𝙏𝙏𝙀𝙍 𝙇𝙐𝘾𝙆 𝙉𝙀𝙓𝙏 𝙏𝙄𝙈𝙀!🫡")#IF THE USER ENTERS WRONG AMOUNT
                   except ValueError:
                     print(Fore.RED +"𝙄𝙉𝙑𝘼𝙇𝙄𝘿 𝙄𝙈𝙋𝙐𝙏! 𝙋𝙇𝙀𝘼𝙎𝙀 𝙀𝙉𝙏𝙀𝙍 𝘼 𝙑𝘼𝙇𝙄𝘿 𝙉𝙐𝙈𝘽𝙀𝙍 𝙁𝙊𝙍 𝙋𝘼𝙔𝙈𝙀𝙉𝙏.🤨")#IF THE USER ENTER WRONG KEYWORD
           else:
                print(Fore.CYAN +"𝙉𝙊 𝙋𝙍𝙊𝘿𝙐𝘾𝙏. 𝘽𝙀𝙏𝙏𝙀𝙍 𝙇𝙐𝘾𝙆 𝙉𝙀𝙓𝙏 𝙏𝙄𝙈𝙀!🤗")#IF THE USER SAYS NO FOE THE GAME
VENDING_MACHINE()
