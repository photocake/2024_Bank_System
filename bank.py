import time
import os

class Bank:
    def __init__(self):
        self.bank_balance = 0
        self.lastname = None
        self.bank_choice = None

    def log_in_panel(self):
        print('\tWelcome to PC Bank')
        print('Enter <Log> to log in your account')
        print('Enter <Reg> for registreation')
        choice = input('Enter your choice(type with lowercase) -> ')
        if choice == 'log':
            self.username = input('Please enter your username -> ')
            password = input('Please enter your password -> ')

            try:
                with open(self.username + ".txt", "r", encoding="utf-8-sig") as f:
                    for i in f:
                        acc = i.split()
                    check_username = acc[0]
                    check_password = acc[1]
                    if check_username == self.username and check_password == password:
                        print('Successfully signed in')
                        time.sleep(1.5)
                        os.system("cls")
                        try:
                            with open(self.username + "money.txt", "r", encoding="utf-8-sig") as f:
                                self.bank_balance = int(f.readline())
            
                        except FileNotFoundError:
                            self.bank_balance = 0
                            
                        self.bank_page()

                    else:
                        print('User is not found')
                        print('Please check your username / password')
                        time.sleep(1.5)
                        os.system("cls")
                        self.log_in_panel()
            
            except FileNotFoundError:
                os.system("cls")
                print('User is not found')
                print('Please check your username / password')
                time.sleep(1.5)
                os.system("cls")
                self.log_in_panel()
        
        elif choice == 'reg':
            self.username = input('Please enter username -> ')
            lastname = input('Please enter lastname -> ')
            password = input('Please enter password -> ')
            date = input('Enter your date -> ')
            month = input('Enter enter month -> ')
            year = input('Enter your year -> ')

            with open(self.username + "info.txt", "w", encoding="utf-8") as f:
                f.write('Name: ' + self.username + " " + lastname + '\n' + 'Password: ' + password + '\n' + 'Date: ' + date + '/' + month + '/' + year)

            with open(self.username + ".txt", "w", encoding="utf-8") as f:
                f.write(self.username + ' ' + password)

            print('You finished your registration')
            time.sleep(1.5)
            os.system("cls")
            self.bank_page()

        else:
            os.system("cls")
            print('Command is not found')
            print('Please try again!')
            time.sleep(1)
            os.system("cls")
            self.log_in_panel()

    def bank_page(self):
        print('\tWelcome to the Bank page', self.username)
        print('=============================================')
        print('| " << "[1] ---> Account info" << "         | ')
        print('| " << "[2] ---> Deposit" << "              | ')
        print('| " << "[3] ---> Check balance" << "        | ')
        print('| " << "[4] ---> Withdrawal" << "           | ')
        print('| " << "[5] ---> exit" << "                 | ')
        print('=============================================\n')

        while self.bank_choice != 5:
            self.bank_choice = int(input('Enter the command -> '))
            self.commands_panel()

    def commands_panel(self):
        if self.bank_choice == 0:
            os.system("cls")
            self.bank_page()

        elif self.bank_choice == 1:
            os.system("cls")
            self.account_info()
        
        elif self.bank_choice == 2:
            os.system("cls")
            self.deposit()
        
        elif self.bank_choice == 3:
            os.system("cls")
            self.balance()

        elif self.bank_choice == 4:
            os.system("cls")
            self.withdrawal()

        elif self.bank_choice == 5:
            with open(self.username + "money.txt", "w", encoding="utf-8") as f:
                f.write(str(self.bank_balance))
            print('You have left the Bank app')

        else:
            print('Command is not found')
            time.sleep(2)
            os.system("cls")
            self.bank_page()

    def account_info(self):
        print('\tYour personal information: ')
        with open(self.username + "info.txt", "r", encoding="utf-8-sig") as f:
            for line in f:
                print(line.strip())

        choice = input('Enter [0] to go back -> ')
        if choice == 0:
            self.bank_page()

    def deposit(self):
        print('\tDeposit page')
        money = int(input('Enter the amount of money -> '))
        if money > 1000:
            print('Loading...')
            time.sleep(1.5)
            print('Too big number. Please try again')
            time.sleep(2)
            os.system("cls")
            self.deposit()
        
        else:
            print('Loading...')
            time.sleep(1.5)
            self.bank_balance += money
            print('Deposit added successfully')
            time.sleep(2)
            self.bank_page()

    def balance(self):
        print('\tYour balance information: ')
        print('Name:', self.username, self.lastname)
        print('Your current balance is', self.bank_balance, '$')
        yn = input('Do you want to put money in your card? (y/n) -> ')
        if yn == 'y':
            money = int(input('Enter the amount of money -> '))
            self.bank_balance += money
            print('You got +', money, "$")
            print('Now your balance is', self.bank_balance, '$')
            time.sleep(2)
            os.system("cls")
            self.bank_page()

        elif yn == 'n':
            print('Your balance is still same')
            time.sleep(2)
            os.system("cls")
            self.bank_page()

        else:
            print('Command is not found. Please try again')
            time.sleep(2)
            os.system("cls")
            self.balance()

    def withdrawal(self):
        print('\tWithdrawal page')
        money = int(input('Enter amount of money -> '))
        if self.bank_balance < money:
            print('Loading...')
            time.sleep(1)
            print("You don't have enough money on your card!")
            time.sleep(2)
            os.system("cls")
            self.bank_page()

        else:
            print('Loading...')
            time.sleep(1)
            print('Withdrawal added successfully')
            self.bank_balance -= money
            time.sleep(2)
            os.system("cls")
            self.bank_page()


def main():
    bank = Bank()
    bank.log_in_panel()


if __name__ == "__main__":
    main()
