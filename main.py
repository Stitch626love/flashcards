

class flashcard:
  def __init__(self):

    self.lines={'Welcome to the show':'Welcome to the show',
          'Long live the king':'Long live the king',
          'Warm strong':'Still atractive',
          'You remember that decree i made a little while ago about land and taxes?':'Yes, sire'}

  def quiz(self):
    while (True):

      que, line = random.choice(list(self.line.items()))

      print("what is the line {}".format(line))
      user_answer = input()

      if(user_answer.lower() == line):
        print("Correct answer")
      else:
        print("Wrong answer")

      option = int(input("enter 0 , if you want to play again : "))
      if (option):
        break

print("welcome to line quiz")
fc=flashcard()
fc.quiz()
