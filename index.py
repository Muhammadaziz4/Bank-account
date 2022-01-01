def print_options():
    print('''
1 - list accounts
2 - transfer money
3 - open a new account
4 - logout
    ''')

def list_accounts(user):
    print('Your accounts:')
    for i in range(3, len(user)):
        print(f'{i - 2}. {user[i][0]} - Balance: {user[i][1]} RUB')
    
def count_accounts(user):
    return len(user) - 3

def transfer_money(user):
    acc_number = count_accounts(user)
    if acc_number == 1: 
        print('You need to have at least two accounts for this operation')
    else: 
        list_accounts(user)
        while True:
            src_acc = request_input('Select the source account: ')
            if int(user[src_acc + 2][1]) == 0:
                print('Source account balance should have non-zero amount of funds. Please choose another source account') 
            else: break

        target_acc = request_input('Select the target account: ')
        src_acc, target_acc = check_accounts(src_acc, target_acc, acc_number)
        money_amount = request_input('Enter the amount to transfer: ')
        src_acc_balance = int(user[src_acc + 2][1])
        target_acc_balance = int(user[target_acc + 2][1])
        money_amount = check_balance(src_acc_balance, money_amount)
        user[src_acc + 2][1] = str(src_acc_balance - money_amount)
        user[target_acc + 2][1] = str(target_acc_balance + money_amount)
        list_accounts(user)

def check_accounts(src, tgt, number):
    while src <= 0 or src > number or tgt <= 0 or tgt > number:
        print('You are referencing non-existing account(s)')
        src, tgt = (request_input('Select the source account: '), request_input('Select the target account: '))
    
    while tgt == src: 
        print('You are trying to transfer money between same accounts')
        src, tgt = (request_input('Select the source account: '), request_input('Select the target account: '))
    return src, tgt

def check_balance(acc_balance, money):
    while True:
        if acc_balance - money < 0: 
            print("Insufficient amount of funds")
            money = request_input('Enter the amount to transfer: ')
        else: return money   

def request_input(msg): return int(input(msg))

def enter_option():
    option = input('Choose an option: ')
    return option

def input_credentials():
    username_input = input('Enter username: ').strip()
    while True:
        if username_input == '':
            print('You have entered empty string or spaces. Please enter username again')
            username_input = input('Enter username: ').strip()
        else: break
    password_input = input('Enter password: ').strip()
    while True:
        if password_input == '':
            print('You have entered empty string or spaces. Please enter password again')
            password_input = input('Enter password: ').strip()
        else: break
    return username_input, password_input
  
def read_data():
  with open ('./bankdata.txt','r') as user:
      constData = user.readlines()
      output = list()
      info = list()
      account_num = int()
      for dt in constData:
          if account_num == 0:
              info = []
              info += dt.split(";")[0:3]
              account_num = int(dt.strip().split(";")[3])
          else:
              info.append(dt.strip().split(";"))
              account_num -= 1
              if account_num == 0:
                  output.append(info)
      return output


def write_data(data):
    pass

def create_acc(user):
    from random import randint
    acc_num = randint(10**15, 10**16 - 1)
    while True: 
        for accounts in user[3::]:
            if acc_num == int(accounts[0]):
                acc_num = randint(10**15, 10**16 )
        else: break
    user.append([acc_num, '0'])
    print(user)

def check_data(l, p, data):
    for datum in data:
        if l == datum[1] and p == datum[2]: 
            return [True, datum]
    return [False, None]

def logout():
    print('Welcome to the online bank!')

def auth():
    login, password = input_credentials()
    db = read_data()
    authenticated, userData  = check_data(login, password, db)
    if authenticated: 
        print(f'Welcome, {userData[0]}!')
        while True:
            print_options()
            option = enter_option()
            if option == '1':
                list_accounts(userData)
            elif option == '2':
                transfer_money(userData)
            elif option == '3':
                create_acc(userData)
            elif option == '4':
                logout()
                break
            else: print("Incorrect option! Please choose listed options from 1 to 4")
    else: print('Incorrect username/password!')

while True:
    auth()