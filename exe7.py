birthday = {"Albert Einstein":"14/3/1879",
            "Benjamin Franklin":"17/1/1706","Ada Lovelac":"10/12/1815"}
print("Welcome to the birthday dictionary.We know the birthdays of:\n"
      'Albert Einstein\n'
       'Benjamin Franklin\n'
      'Ada Lovelac\n')
ques = input("Who birthday do u want to look up?")
if ques in birthday:
    print(birthday.get(ques))
else:
    print("sorry,no such name")
      
      


    
