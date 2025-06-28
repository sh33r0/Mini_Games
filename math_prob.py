import random, time

total_questions = 10

def Mode(mode):
    min_num = 1
    max_num = 10
    if mode in 'medium' :
        max_num = 50
    elif mode in 'hard' :
        max_num = 100
    return(min_num , max_num)


def generate_problem(min_operand , max_operand):
    operators = [ "+" , "-" , "*" , "//" ]
    operator = random.choice(operators)

    left_operand = random.randint(min_operand , max_operand)
    right_operand = random.randint(min_operand , max_operand)

    expr = str(left_operand) + " " + operator + " " + str(right_operand)
    ans = eval(expr)
    return(expr , ans)
def play():
    difficulty = input("Enter Difficulty Level (Easy/ Medium/ Hard) : ").lower()
    Min_operand , Max_operand = Mode(difficulty)

    print('''Welcome to Math Problem Generator
          Correct answer = +5
          Wrong answer = -1''')
    input("Press Enter to start the Game:- ")

    start = time.time()
    score = 0
    for i in range(total_questions):
        expr,answer = generate_problem(Min_operand , Max_operand)
        guess = input("\nProblem #" + str(i+1) + " : " + expr + "= ")
        if guess == str(answer):
            print("Correct!! +5")
            score += 5
        else:
            print("Wrong!! -1")
            score -= 1
    end = time.time()
    total_time = round(end-start , 2)

    print("\nYour total Score is ", score , "/50")
    print("Total time to answer is ", total_time , "sec")