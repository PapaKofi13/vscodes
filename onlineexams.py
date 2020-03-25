from question import questions  # import the question class

#question prompt is an array to store the questions being asked
question_prompts = [
    "What is the color of an orange? \n(a)Red/Green\n(b)Black\n(c)Violet \n",
    "How many sides does a triangle have?\n(a)23\n(b)5\n(c)3\n",
    "Who is the President of Ghana? \n (a)Trump\n(b)Addo\n(c)Dumerlo \n"
]


#answers to question defined in this array
questions = [
    questions(question_prompts[0],"a"),
    questions(question_prompts[1],"c"),
    questions(question_prompts[2],"b"),

]
#main for loop to run the test and compare the quesrions
#also returns your answer
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print(f"you got {score} out of {len(questions)} questions correct ! ")
    if score >= 2:
        print(" congrats you smart kid")
    elif score <= 2:
        print(" GTFOH you dumbass !!! ")


run_test(questions)
