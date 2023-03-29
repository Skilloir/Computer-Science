######
# CSE Project 3.2.5 Strategy Game: PS Rock
#
# psrock.py implements a round-robin tournament of rock-paper-scissors
# To run a tournament, execute psrock_play.py, not this file.
# The students and teacher should modify psrock_play.py and not modify this file.
#
# Each player should have their own .py file containing 
# a function called move(my_history, their_history)
# These filenames (without the .py extension) are passed to the 
# round_robin() function as the 2nd, 3rd, etc. arguments.
# 
#######

def round(player1, player2, history1 = "", history2 = ""):
  """ Plays one round of rock paper scissors
  player1 and player2 are functions that each accept two strings and return "r", "p", or "s"
  history1 and history2 are the two players' histories against each other,
  passed to the two functions
  
  Returns move1, move2, score1, score2
      move1, move2 are single characters: the moves made by the two players
      score1 and score2 are each -1, 0, or +1 for loss, tie, win
  """
  # Get player 1's move. 
  move1 = player1(my_history = history1, their_history = history2)
  # Get player 2's move. 
  move2 = player2(my_history = history2, their_history = history1)
  
  if (valid(move1) and valid(move2)):      
    if (move1 == move2):
      score1, score2 = 0, 0
    elif (move1 + move2 in ["rs", "sp", "pr"]):
      score1, score2 = 1, -1
    else:
      score1, score2 = -1, 1
  else: # one of the moves was invalid
    if valid(move1): # only move2 was invalid
      move2 = "x"
      score1, score2 = 1, -1
    elif valid(move2): # only move1 was invalid
      move1 = "x"
      score1, score2 = -1, 1
    else: # Both moves invalid
      move1, move2 = 'x', 'x'
      score1, score2 = -1, -1
          
  return move1, move2, score1, score2

def valid(move):
  """ move should be a single character "r", "p", or "s".
  
  Returns True if that is the case, False otherwise.
  """
  if (len(move) == 1 and move in "rps"):
    return True
  else:
    return False        
            
def playoff(player1, player2, number_of_rounds = 60):
  """
  player1 and player2 are functions that accept two strings and return "r", "p", or "s"
  number_of_rounds is an int
  Plays a sequence of rounds between two players
  
  Returns record1, record2, my_history1, my_history2
       where record1, record2 are win-loss-tie tuples
       my_history1, my_history2 are strings representing what the players did
  """
  record1, record2 = (0,0,0),(0,0,0) # win,loss,tie
  my_history1, my_history2 = "", ""
  for round_number in range(number_of_rounds):
    move1, move2, new_score1, new_score2 = round(player1, player2, my_history1, my_history2)
    my_history1 += move1[0] # Just use first letter of move to record it
    my_history2 += move2[0]
    def new_record(record, new_score):
      if (new_score == -1):
        record = (record[0], record[1] + 1, record[2])
      if (new_score == 0):
        record = (record[0], record[1], record[2] + 1)
      if (new_score == 1):
        record = (record[0]+1, record[1], record[2])
      return record
    record1 = new_record(record1, new_score1)
    record2 = new_record(record2, new_score2)
      
  return record1, record2, my_history1, my_history2
    
def team_name(module):
  """
  Accepts a module that has been imported
  Returns the name of the module as a string
  """
  return str(module).split(' ')[1].replace('\'','')

def strategy_name(module):
  """
  Accepts a module that has been imported
  Returns the value of strategy_name in the imported file <module>
  """
  return module.strategy_name
    
def round_robin(number_of_rounds, *argv):
  """number_of_rounds is an int = 1 or more
  The remaining arguments become a list: argv
  argv is a list of functions, one per player
  """
  # Create report and scores[player1][player2] array
  scores = {} # scores[team_name] = [(W,L,T), (W,L,T), etc.]
  report = {} # report[team_name] = "Report string"
  team_names = [] # list of the module names
  strategy_names = {}
  for player1 in argv:
    # Append the module name to the team_names list
    team_name1 = team_name(player1)     
    team_names.append(team_name1)
    
    # Place the strategy name in the dictionary, keyed by the module name
    strategy_names[team_name1] = player1.strategy_name
    
    # Provide the first line of the report
    report[team_name1] = "Win-loss-tie report for " + team_name1 + ":\n"
    
    # Create an empty list that will get populated with (W,L,T) 3-tuples
    scores[team_name1] = []
  
  for player1 in argv:
    player1_name = team_name(player1) #repeat of above
    scores[player1_name].append('X')
    for player2 in argv[argv.index(player1) + 1:]:
      player2_name = team_name(player2)
      
      score1, score2, history1, history2 = playoff(player1.move, player2.move, number_of_rounds)
      scores[player1_name].append(score1)
      scores[player2_name].append(score2)
      score1 = str(score1[0]) + "-" + str(score1[1]) + "-" + str(score1[2])
      score2 = str(score2[0]) + "-" + str(score2[1]) + "-" + str(score2[2])
      
      report[player1_name] += "\n" + history1 + " " * 8 + player1_name + ": " + strategy_name(player1) + " " + score1 + "\n" + \
                              history2 + " " * 8 + player2_name + ": " + strategy_name(player2) + "\n"
                              
      report[player2_name] += "\n" + history2 + " " * 8 + player2_name + ": " + strategy_name(player2) + " " + score2 + "\n" + \
                              history1 + " " * 8 + player1_name + ": " + strategy_name(player1) + "\n"

        
  overall_record = {}
  for team in report:
    total_score = [0,0,0]
    for score in scores[team]:
      if score != "X":
        total_score[0] += score[0]
        total_score[1] += score[1]
        total_score[2] += score[2]
      overall_record[team] = total_score
  short_report = "-" * 80 + "\nWin-loss-tie report for round robin:\n\n"
  for team in overall_record:
    short_report += str(overall_record[team][0]) + \
                    "-" + str(overall_record[team][1]) + \
                    "-" + str(overall_record[team][2]) + \
                    " " * 8 + team + ": " + strategy_names[team] + "\n"
  return short_report, report
