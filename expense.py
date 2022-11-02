from PyInquirer import prompt
import csv
from user import select_user
from generics import yes_no_question
from debts import add_debts

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

    # We read the file. If an expense with the same label exists, the new one is not registered.
    # Each line has a label, an amount and the spender (in this order) and then other people involved
    with open('expense_report.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if row[0] == infos["label"]:
                print("An expense with this label already exists.")
                return False

    # Spender
    spender = select_user()
    if (spender == None):
        print("Can't add expense")
        return False

    # Add other users
    other_users = []
    while (yes_no_question("Do you want to add another user ?")):
        user = select_user()
        # If the user is already the spender or in the selected users
        if (user == None or user == spender or user in other_users):
            print("Error, this user is incorrect, cannot add expense")
            return False
        other_users.append(user)
    
    # Update the depts
    if not add_debts(spender, other_users, infos["amount"]):
        return False
    
    # List of the data to write
    dataToWrite = [infos["label"], infos["amount"], spender] + other_users
    
    # Add the new expense
    with open('expense_report.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(dataToWrite)
    
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True


