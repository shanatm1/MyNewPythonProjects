
# ----------------------------
def new_game():
    guesses = []
    correct_guessess = 0
    question_num = 1
    for key in questions:
         print("---------------------------")
         print(key)
         for i in Options[question_num-1]:
            print(i)
         guess = input("Enter (A, B, C or D): ")
         guess = guess.upper()
         guesses.append(guess)

         check_answer(questions.get(Key)
         question_num+=1
# ----------------------------
def check_answer(answer, guess):
    pass
# ----------------------------
def show_score():
    pass
# ----------------------------
def play_again():
    pass
# ----------------------------

questions = {"shana's favorate food?": "C",
             "which is shana's dream destination?": "B",
             "what is shana's hobby?": "B",
             "who is shana's x lover?": "C"}
Options = [["A.fish curry", "B.noodels", "C.biriyani", "D.rice & beef curry" ],
           ["A.Dubai", "B.Greece", "C.Switzerland","D.Kerala"],
           ["A.painting", "B.cooking", "C.sleeping", "D.Cycling"],
           ["A.Nithin", "B.Nitin", "C.Mithun", "D.Riyas"]]

new_game()

