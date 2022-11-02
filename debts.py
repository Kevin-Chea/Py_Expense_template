import csv
import shutil
from tempfile import NamedTemporaryFile

deptsFile = 'debts.csv'

def update_debt_of_user(user_to_update, value_to_add, to_who):
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    findUser = False
    findToWho = False
    with open(deptsFile, 'r') as oldfile, tempfile:
        reader = csv.reader(oldfile, delimiter=' ', quotechar='|')
        writer = csv.writer(tempfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if not findUser and row[0] == user_to_update:
                findUser = True
                for i in range(1, len(row)):
                    if row[i] == to_who:
                        row[i+1] = str(float(row[i+1]) + float(value_to_add))
                        findToWho = True
                        break
                if not(findToWho):
                    row.append(to_who)
                    row.append(value_to_add)
            
            writer.writerow(row)
        if not findUser:
            row = [user_to_update, to_who, str(value_to_add)]
            print(row)
            writer.writerow(row)
    shutil.move(tempfile.name, deptsFile)
    return True

def add_debts(spender, users, totalAmount):
    amount = float(totalAmount)
    amoutPerUser = amount / (len(users) + 1)
    for user in users:
        if not update_debt_of_user(user, amoutPerUser, spender):
            print("Error during debts update")
            return False
    return True

def show_debts():
    with open('debts.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            user = row[0]
            to = []
            amounts = []
            for i in range(1, len(row), 2):
                if (row[i + 1] != '0'):
                    to.append(row[i])
                    amounts.append(row[i + 1])
            if (len(to) > 0):
                print(user + " owes:", end='')
                for j in range(len(to)):
                    print(amounts[j] + " to " + to[j] + "; ", end='')
                print("")
            else :
                print("nothing")
                