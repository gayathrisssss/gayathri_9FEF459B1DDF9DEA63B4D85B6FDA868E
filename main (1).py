class player:
  def play(self):
    print("The player is playing criket")
class batsman(player):
  def play(self):
    print("The batsman is batting")
class bowler(player):
  def play(self):
    print("The bowler is bowling")
obj1=batsman()
obj2=bowler()
obj1.play()
obj2.play()