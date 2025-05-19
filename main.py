import random
import time 

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)

    answer = eval(expr)
    return expr, answer

wrong = 0

input("\n🔢 Press Enter to start the Timed Math Challenge!")
print("\n" + "=" * 40)
print("          TIMED MATH QUIZ          ")
print("=" * 40)

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True: 
        guess = input(f"Problem #{i:2}: {expr} = ")
        if guess.strip() == str(answer):
            break
        wrong += 1
end_time = time.time()

total_time = round(end_time - start_time, 2)
print("\n" + "=" * 45)
print("|{:^43}|".format(" SCOREBOARD"))
print("|" + "_" * 43 + "|")
print("|{:^43}|".format(""))
print(f"|   Total Problems Solved : {TOTAL_PROBLEMS:<16}|")
print(f"|   Incorrect Attempts    : {wrong:<16}|")
print(f"|   Time Taken            : {total_time:.0f} seconds      |")
print("|" + "_" * 43 + "|")
print("|{:^43}|".format(" Well done! Keep practicing!"))
print("=" * 45)

