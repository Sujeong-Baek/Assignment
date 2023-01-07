# What did you buy? apples
# How many apples did you buy? 3
# What is the price of one apples? 1500
# You bought 3 apples for 4500 KRW.

# What did you buy? bananas
# How many bananas did you buy? 11
# What is the price of one bananas? 800
# You bought 11 bananas for 8800 KRW.

# What did you buy? chocolate
# How many chocolate did you buy? 1
# What is the price of one chocolate? 2200
# You bought 1 chocolate for 2200 KRW.

# What did you buy? coffee
# How many coffee did you buy? 2
# What is the price of one coffee? 2500
# You bought 2 coffee for 5000 KRW.

# What did you buy? 
# In total, you spent 20500 KRW

def shopping():
    spent = 0
    while True:
        buy = input("What did you buy? ")
        if buy == '':
            print('In total, you spent ' + str(spent))
            break
        many = int(input('How many ' + buy + ' did you buy? '))
        price = int(input('What is the price of one '+buy+ '? '))
        p = many * price
        spent += p
        print('You bouht '+ str(many) +' '+ buy +' for '+str(p)+' KRW')

# Shopping Calculator V0.2

# What did you buy? apples
# How many apples did you buy? 3
# What is the price of one apples? 1500
# You bought 3 apples for 4500 KRW.
# What did you buy? bananas
# How many bananas did you buy? 11
# What is the price of one bananas? 800
# You bought 11 bananas for 8800 KRW.
# What did you buy? chocolate 
# How many chocolate did you buy? 1
# What is the price of one chocolate? 2200
# You bought 1 chocolate for 2200 KRW.
# What did you buy? coffee
# How many coffee did you buy? 3
# What is the price of one coffee? 2500
# You bought 3 coffee for 7500 KRW.
# What did you buy? 
# Your purchases:
# 왼쪽정렬                          오른쪽정렬  오른쪽정렬
# -------------------------------------------------------------
# apples                               3 x 1500 KRW    4500 KRW
# bananas                             11 x  800 KRW    8800 KRW
# chocolate                            1 x 2200 KRW    2200 KRW
# coffee                               3 x 2500 KRW    7500 KRW
# -------------------------------------------------------------
# Total price:                                        23000 KRW

def shopping2():
    spent = 0
    lst = [] # [(apples, 3, 1500, 4500), (bananas, 11, 800, 8800)]
    while True:
        buy = input("What did you buy? ")
        if buy == '':
            print('Your purchases:')
            print('-'*55)
            for buy, many, price, p in lst:             # (apples, 3, 1500, 4500)
                print("{0:<20} {1:>10} {2:>1} {3:>1} {4:>1} {5:>7} {6}".format(buy, many,'x',price,'KRW', p,'KRW'))
            print('-'*55)
            print("{0:<20} {1:>30} {2} ".format('Total price: ', str(spent),'KRW'))
            break
        many = int(input('How many ' + buy + ' did you buy? '))
        price = int(input('What is the price of one '+buy+ '? '))
        p = many * price
        spent += p
        lst.append((buy, many, price, p))
        print('You bouht '+ str(many) +' '+ buy +' for '+str(p)+' KRW')



shopping2()

# lst = [('apple', 3, 1500, 4500), ('bananas', 11, 800, 8800)]
# for buy, many, price, p in lst:
#     print("buy: " + buy)
#     print("many: " + str(many))
#     print("price: " + str(price))
#     print("p: " + str(p))

'3                    3 x 1500 KRW 4500 KRW'