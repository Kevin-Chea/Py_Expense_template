from PyInquirer import prompt
import csv


# Ask a Yes / No question. Return true if yes
def yes_no_question(question):
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":question,
        "choices": ["Oui","Non"]
    }
    option = prompt(main_option)
    return option['main_options'] == "Oui"