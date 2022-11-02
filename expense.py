from PyInquirer import prompt
import csv
from user import select_user

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
]



def new_expense(*args):
    infos = prompt(expense_questions)
    user = select_user()
    if (user == None):
        print("Can't add expense")
        return False
    # We read the file. If an expense with the same label exists, the new one is not registered.
    # Each line has a label, an amount and the spender (in this order)
    with open('expense_report.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if row[0] == infos["label"]:
                print("An expense with this label already exists.")
                return False
    # Add the new expense
    with open('expense_report.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([infos["label"], infos["amount"], user])
    
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True


