from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)

    # We read the file. If an user with the same name exists, the new one is not registered.
    # Each line has a name in the file
    with open('users.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if row[0] == infos["name"]:
                print("A user with this name already exists.")
                return False
    # Add the new expense
    with open('users.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([infos["name"]])
    
    print("User Added !")
    return True

def get_users():
    # Return the list of users
    users = []
    with open('users.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            users.append(row[0])
    return users

def select_user():
    users = get_users()
    if (len(users)) == 0:
        print("No existing user !")
        return None
    select_user_questions = [
        {
            "type":"list",
            "name":"user_options",
            "message":"Choose a spender among the list",
            "choices": users
        }
    ]
    option = prompt(select_user_questions)
    return option['user_options']

