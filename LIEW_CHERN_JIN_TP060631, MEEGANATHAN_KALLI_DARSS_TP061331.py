#MEEGANATHAN A/L KALLI DARSS TP061331
#LIEW CHERN JIN  TP060631

# overall main menu
def mainMenu(): 
    print('''
Enter 0 to exit
Enter 1 to access admin
Enter 2 to access customers
Enter 3 to access registered customers
''')
    login = int(input('enter number here>>>')) #choosing their options
    print('-' * 40)
    return login

# admin main menu
def admin():
    print('Enter admin username and password')
    details = access()
    if (adminLogin(details[0], details[1])): #admin login
        while True:
            print('''
Enter 1 to add cars for rental
Enter 2 to modify car details
Enter 3 to display all records and car details
Enter 4 to search records
Enter 5 to return a rental car
Enter 6 to Exit
''')
            option = int(input('Enter option here>>>'))
            print('-' * 40)
            if option == 1:
                available()  # add car into txt file
                print('succesfully added')
            elif option == 2:
                print('Modifying car details')  # modify car details
                modifyCar()
            elif option == 3:
                print('Display all records and car details') #showing all records and car details
                showRecords()
                print(' ')
                print('Display all car details')
                showCars() 
            elif option == 4:
                print('Searching for specific record') #looking for specific information
                searchRecords()
            elif option == 5:  # returned car from customer
                returned()
            elif option == 6: #exit admin main menu
                print('Exit')
                break
            else:
                print('Invalid input')
    else:
        print('Wrong admin username or passowrd')

# customer main menu
def customer():
    while True:
        print('''
Enter 1 to access cars available for rent
Enter 2 to register as member
Enter 3 to Exit
''')
        option = int(input('Enter option here>>>'))
        print('-' * 40)
        if option == 1: #showing cars available for rent
            print('Cars available for rent')
            print('-' * 40)
            print(' ')
            show()
            print(' ')
            print('-' * 40)
        elif option == 2:
            register() #register to become registered customer
            break
        elif option == 3: #exit customer main menu
            print('Exit')
            break
        else:
            print('Invalid input')

# registered customer main menu
def registeredCustomer():
    details = access()
    if (userLogin(details[0], details[1])):  # member login
        while True:
            print('''
Enter 1 to modify personal details
Enter 2 to view rental history
Enter 3 to view details of cars to be rented out
Enter 4 to Book car
Enter 5 to do payment
Enter 6 to top up
Enter 7 to check balance available
Enter 8 to exit
''')
            option = int(input('Enter option here>>>'))
            print('-' * 40)
            if option == 1: #modifying users personal details
                print('Modifying personal information')
                modifyUserInfo(details[0],details[1])
                return start()
            elif option == 2: #users viewing their own rental history
                print('Viewing personal rental history')
                personalRecords(details[0])
            elif option == 3: #viewing cars booked 
                print('Viewing details of cars to be rented out')
                booked(details[0])
            elif option == 4: #making a booking 
                booking(details[0])
            elif option == 5: #users making payment for cars they booked
                print('Making Payment')
                payment(details[0])
            elif option == 6: #adding money into the e wallet
                topUp(details[0])
            elif option == 7: #checking balance available in e wallet
                balance(details[0])
            elif option == 8: #exit registered customer main menu
                print('Exit')
                break
            else:
                print('Invalid input')
    else:
        print('wrong username or password')

# input name and password for user/admin login
def access():
    userName = input('Enter user name>>>')
    password = input('Enter password>>>')
    return userName, password

# accessing admins text file
def adminLogin(userName, password):
    try:
        file = open('admins.txt', 'r')  # open users txt file and read data in txt file
    except:
        print('Unable to open file')
        return
    success = overallLogin(file, userName, password)
    file.close()
    return success


# accessing users text file
def userLogin(userName, password):
    try:
        file = open('users.txt', 'r')  # open users txt file and read data in txt file
    except:
        print('Unable to open file')
        return
    success = overallLogin(file, userName, password)
    file.close()
    return success

# checking whether the text file and the inputted name and password is tally or same
def overallLogin(file, userName, password):
    success = False
    for line in file:
        a, b = line.split(',')  # a=username and b=password and defining ',' as the separation
        b = b.strip()  # removing the empty line after checking the data
        if (a == userName and b == password):
            print('login succesful')
            success = True
            break
    file.close()
    return success

# registration form for non registered customers
def register():
    try:
        file = open('users.txt', 'r')
    except:
        print('Unable to open file')
        return
    print('Enter user name and password to register')
    detail = access() #call function
    for users in file:
        a, b = users.split(',')
        b = b.strip()
        if detail[0] == a:
            print('Username taken')  # if username same then deny registration
            file.close()
            return
    file.close()
    if bankRegister(detail[0]) == 1: #call function
        return
    try:
        file = open('users.txt', 'a')  # open users txt file and append data into txt file
    except:
        print('Unable to open file')
        return
    file.write(detail[0] + ',' + detail[1]+'\n' )  # open a new line and input data into the txt file
    file.close()


#bank registration form 
def bankRegister(username): 
    try:
        file = open('bankInfo.txt', 'a')
    except:
        print('Unable to open file')
        return
    x = 1 #will return 1 if failed and cancel registration
    bankNumb = int(input('Enter bank account number>>>'))
    veri = int(input('Enter verification code for bank account(6 digit)>>>'))
    veri1 = int(input('Confirm verification code>>>'))
    bankNumb = str(bankNumb)
    if (len(bankNumb) >= 10 and len(bankNumb) <= 12): #checking whether is valid bank account
        if len(str(veri)) == 6: #checking is the verification code the same
            if veri == veri1:
                file.write(username + ',' + bankNumb + ',' + str(veri) + ',0\n')
                print('succesfully registered')
            else:
                print('Verification code does not match')
                return x
        else:
            print('Length of verification code is not 6')
            return x
    else:
        print('Invalid bank number')
        return x
    file.close()


# adding cars that is available for rent
def available():
    try:
        file = open('carDetails.txt', 'a')
    except:
        print('Unable to open file')
        return
    brand = input('Enter car brand>>>') #enter new car details
    model = input('Enter car model>>>')
    price = input('Enter price per day>>>')
    file.write(brand + ',' + model + ',' + price + ',available\n') #add into car details to be rented
    file.close()

#showing all car details
def showCars():
    try:
        file = open('carDetails.txt', 'r')
    except:
        print('Unable to open file')
        return
    for line in file:
        line = line.strip()
        print(line) #display all the car details
    file.close()

    
# print cars available to be rented
def show():
    try:
        file = open('carDetails.txt', 'r')
    except:
        print('Unable to open file')
        return
    for line in file:
        line = line.strip()
        if 'available' in line:
            print(line) #display all the cars available for rent
    file.close()


# cars returned to the owner
def returned():
    try:
        file = open('carDetails.txt', 'r')
    except:
        print('Unable to open file')
        return
    add = False #set return status to fail at default
    for lines in file:
        if 'booked' in lines.lower(): #showing cars that can be returned
            lines=lines.strip()
            print(lines)
    print('-'*40)
    temp = []
    try:
        file = open('carDetails.txt', 'r')
    except:
        print('Unable to open file')
        return
    model = input('Enter returned rental car model (second column)>>>')
    for lines in file: #changing details of car into available for rent
        a, b, c, d = lines.split(',')
        d = d.strip()
        if model.lower() == b.lower() and d == 'booked':
            temp.append(a + ',' + b + ',' + c + ',available\n')
            add = True #return status to successful
        else:
            temp.append(lines)
    file.close()
    if add:
        print('Returned succesfully')
    else:
        print('Invalid input')
        return 
    try:
        file = open('carDetails.txt', 'w')
    except:
        print('Unable to open file')
        return
    for lines in temp: #replacing details of cars in text file
        file.write(lines)
    file.close()


# modifying car details
def modifyCar():
    show() #showing cars that can be modified
    carList = []
    try:
        file = open('carDetails.txt','r')
    except:
        print('Unable to open file')
        return
    process = False #set default status to fail
    model = input('Enter the car model (second column) that needs to be modified>>>')
    for lines in file:
        a,b,c,d = lines.split(',')
        if model.lower() in b.lower(): #if the model is same, then allow modification of details
            name =input('Enter modified car brand>>>')
            model =input('Enter modified car model>>>')
            price =input('Enter modified car price per day>>>')
            carList.append(name+','+model+','+price+','+'available\n')
            process = True #set status to success
        else:
            carList.append(lines)
    file.close()
    if process:
        print('Succesfully modified')
    else:
        print('Invalid Input')
        return
    try:
        file1 = open('carDetails.txt','w')
    except:
        print('Unable to open file')
        return
    for ele in carList: #replacing car details
        file1.write(ele)
    file1.close()


# modifying user's information
def modifyUserInfo(username,password):
    try:
        file = open('users.txt', 'r')
    except:
        print('Unable to open file')
        return
    userList = []
    newName = []
    for line in file:
        a, b = line.split(',')
        b = b.strip()
        if a == username and b == password: #checking which account to change
            after = input('Enter new username>>>')
            newName.append(after)
            after1 = input('Enter new password>>>')
            userList.append(after + ',' + after1 + '\n')
        else:
            userList.append(line)
    file.close()
    try:
        file = open('users.txt', 'r')
    except:
        print('Unable to open file')
        return
    for line in file:
        a,b = line.split(',')
        if newName[0] == a: #doesnt allow user to change if username taken
            print('Username taken')
            return
    file.close()
    try:
        file = open('users.txt', 'w')
    except:
        print('Unable to open file')
        return
    for ele in userList: #replacing with new information
        file.write(ele)
    file.close()
    try:
        file = open('allRecords.txt','r')
    except:
        print('Unable to open file')
        return
    records=[]
    newRecords = []
    for lines in file:
        records.append(lines)
    for string in records:
        a,b,c,d,e,f,g = string.split(',')
        if username == b:
            newRecord = string.replace(b,newName[0])#replacing old username with new username in all records
            newRecords.append(newRecord)
        else:
            newRecords.append(string)
    file.close
    try:
        file = open('allRecords.txt','w')
    except:
        print('Unable to open file')
        return
    for record in newRecords: #replacing information in all records
        file.write(record)
    print('Succesfully modified')

# booking for customers
def booking(username): 
    try:
        file = open('carDetails.txt', 'r')  # read available car to be booked
    except:
        print('Unable to open file')
        return
    carDetails = []
    returned = []
    show() #show cars available for rent
    process = False #set default status to fail
    book = input('Enter car model (second column) to be booked>>>') #entering details of rental cars
    date = input('Enter starting rental date (YYYY-MM-DD)>>>')
    finish = input('Enter return car date (YYYY-MM-DD)>>>')
    for lines in file:
        a, b, c, d = lines.split(',')
        if book.lower() == b.lower(): #changing status of car
            carDetails.append(a + ',' + b + ',' + c + ',booked\n')
            price = c 
            process = True
        else:
            carDetails.append(lines)
    year, month, day = map(int, date.split('-'))
    bookDay = year * 365 + month * 30 + day #calculating starting rental date
    year, month, day = map(int, finish.split('-'))
    returnDay = year * 365 + month * 30 + day #calculating end of rental date
    price = float(price) 
    amount = (returnDay - bookDay) * price #calculating the total amount to be paid
    amount = str(amount)
    file.close()
    
    if process:  #if fail then break function
        print('Succesfully booked')
    else:
        print('Invalid Input')
        return
    try:
        file = open('carDetails.txt', 'w')
    except:
        print('Unable to open file')
        return
    for ele in carDetails:
        file.write(ele)
    file.close()
    file1 = open('allRecords.txt', 'r')
    for record in file1:
        a, b, c, d, e, f, g = record.split(',')
    a = int(a) + 1 #adding new record
    newRecord = str(a)
    file1.close()
    try:
        file1 = open('allRecords.txt.', 'a')
    except:
        print('Unable to open file')
        return
    file1.write(newRecord + ',' + username + ',' + book + ',' + date + ',' + finish + ',' + amount + ',pending\n')
    file1.close()
    

#display all records
def showRecords():
    try:
        file = open('allRecords.txt', 'r')
    except:
        print('Unable to open file')
        return
    for lines in file: #showing all records
        lines = lines.strip()
        print(lines)
    file.close()

#searching for specific records
def searchRecords():
    try:
        file = open('allRecords.txt', 'r')
    except:
        print('Unable to open file')
        return
    search = input('Enter data to be searched>>>') #searching for specific information
    for lines in file:
        lines = lines.strip()
        if search.lower() in lines.lower():
            print(lines)
    file.close()

#showing customers personal records
def personalRecords(username):
    try:
        file = open('allRecords.txt', 'r')
    except:
        print('Unable to open file')
        return
    for lines in file:
        a,b,c,d,e,f,g = lines.split(',')
        if username == b: #showing personal record
            lines = lines.strip()
            print(lines)
    file.close()

#users checking cars they booked
def booked(username):
    try:
        file = open('allRecords.txt', 'r')
    except:
        print('Unable to open file')
        return
    cars = []
    date = input("Enter today's date in YYYY-MM-DD format>>>")
    year, month, day = map(int, date.split('-'))
    today = year * 365 + month * 30 + day #calculating todays date
    for lines in file:
        a, b, c, d, e, f, g = lines.split(',')
        if username == b:
            year, month, day = map(int, d.split('-'))
            numbDays = year * 365 + month * 30 + day
            if (numbDays - today) > 0: #finding cars that have yet to be rented out
                cars.append(c)
    file.close()
    try:
        file = open('allRecords.txt', 'r')
    except:
        print('Unable to open file')
        return
    for lines in file:
        lines = lines.strip()
        a,b,c,d,e,f,g = lines.split(',')
        for car in cars: #displaying cars that the users booked
            if username == b and car == c:
                print(lines)
    file.close()

#customers making payment
def payment(username): 
    try:
        file = open('bankInfo.txt', 'r')
    except:
        print('Unable to open file')
        return
    process = False #set default status to fail
    bankAcc = input('Enter your bank account number>>>') #verifying their account
    verify = input('Enter your verification code>>>')
    for lines in file:
        a, b, c, d = lines.split(',')
        if a == username and b == bankAcc and c == verify:
            d = d.strip()
            balance = float(d)
            process = True #set to success
    if process == False:# break function if fail
        print('Invalid bank account or verification code')
        return
    print(balance)
    file.close()
    try:
        file = open('allRecords.txt', 'r')
    except:
        print('Unable to open file')
        return
    usersPending=[]
    allRecords = []
    for lines in file:
        if username and 'pending' in lines: #showing users cars that needs to make payment
            usersPending.append(lines)
            lines = lines.strip()
            print(lines)
        else:
            allRecords.append(lines)
    file.close()
    try:
        file = open('allRecords.txt', 'r')
    except:
        print('Unable to open file')
        return
    
    if len(usersPending) != 0: #checking are there any payments need to be done
        rec = int(input('Select which record number to pay>>>'))
        for record in usersPending:
            a, b, c, d, e, f, g = record.split(',')
            if str(rec) == a: #checking which record
                if float(balance) > float(f): #checking are there sufficient balance
                    allRecords.append(a + ',' + b + ',' + c + ',' + d + ',' + e + ','+ f + ',paid\n')
                else:
                    print('Insufficient balance in wallet, please top up')
                    return
            else:
                allRecords.append(record)
    else:
        print('No payment needs to be done :D')
        return
    payment = float(f)
    file.close()
    try:
        file = open('allRecords.txt', 'w')
    except:
        print('Unable to open file')
        return
    for ele in allRecords:
        file.write(ele) #replacing the records to paid 
    file.close()

    bankUpdate = []
    try:
        file = open('bankInfo.txt','r')
    except:
        print('Unable to open file')
        return
    for lines in file:
        a,b,c,d = lines.split(',')
        if username == a:
            final = balance - payment #deducting the balance in the users e wallet
            bankUpdate.append(a+','+b+','+c+','+str(final)+'\n')
        else:
            bankUpdate.append(lines)
    file.close()
    try:
        file = open('bankInfo.txt','w')
    except:
        print('Unable to open file')
        return
    for ele in bankUpdate: #replacing the data with after deductions data
        file.write(ele)
    file.close()
    print('Payment successful')
            
#topping up balance in the e wallet
def topUp(username): 
    try:
        file = open('bankInfo.txt','r')
    except:
        print('Unable to open file')
        return
    process = False #set default status to fail
    records = []
    bank = int(input('Enter bank number>>>')) #getting users bank account
    verify = int(input('Enter verification code>>>'))
    for lines in file:
        a,b,c,d = lines.split(',')
        d = d.strip()
        if username == a and str(bank) == b and str(verify) == c: #checking does their account match
            amount = float(input('Enter top up amount>>>')) #entering their top up amount
            total = float(d) + amount
            records.append(a+','+b+','+c+','+str(total)+'\n')
            process = True #set process to true
        else:
            records.append(lines)
    file.close()
    if process:
        print('Top up succesful')
    else:
        print('Wrong username, bank number or verification code')
        return
    try:
        file = open('bankInfo.txt','w')
    except:
        print('Unable to open file')
        return
    for lines in records: #replacing the data with topped up amount
        file.write(lines)
    file.close()
            
#displaying the balance in the user's e wallet
def balance(username): 
    try:
        file = open('bankInfo.txt','r')
    except:
        print('Unable to open file')
        return
    for lines in file: 
        a,b,c,d = lines.split(',')
        d=d.strip()
        if username == a: #checking users account
            print(d) #printing users balance in e wallet
    file.close()
            
# Start of Program
def start(): 
    while True:
        login = mainMenu()
        if login == 0: #exit the whole program
            print('you have exited')
            break
        elif login == 1:
            print('accessing admin control')
            print('-' * 40)
            admin() #accessing admins main menu
        elif login == 2:
            print("accessing customers' control")
            customer() #accessing customer's main menu
        elif login == 3:
            print("accessing registered customers' control")
            registeredCustomer() #accessing registered customer main menu
        else:
            print('invalid input')

print('-'*26)
print('WELCOME TO MEDY CAR RENTAL')
print('-'*26)
start()#start the program
