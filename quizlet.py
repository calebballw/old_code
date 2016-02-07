def quizlet(question, answer):
    question = str(question)
    answer = str(answer)
    user = input(question)
    if user == answer:
        print ("Good Job")
    else:
        print ("Wrong answer")

while 1 == 1:
    quizlet(input("Type in a question: "), input("Type the answer to that question: "))
    continue
