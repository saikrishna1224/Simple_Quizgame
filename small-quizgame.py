#python game 
print('Hey, Welcome to the Sports Quiz game!')
print('Best of luck')

totalquestions = 5
score = 0

ans = input('1.who won the ipl 2019?')

if ans.lower() == "mumbai indians":
    print('correct!')
    score += 1
else:
    print('incorrect!')
    
ans = input('2.who won the uefa champions league 2020?')

if ans.lower() == "bayern munrich":
    print('correct!')
    score += 1
else:
    print('incorrect!')
    
ans = input('3.How many does royal challengers banglore went to finals in indina premier league?')

if ans=="2":
    print('correct!')
    score += 1
else:
    print('incorrect!')
    
ans = input('4.Cristino ronaldo current playing fow which club?')

if ans.lower()=="juventus":
    print('correct!')
    score += 1
else:
    print('incorrect!')

ans = input('5.Indian premier league 2020 was taking place on which country?')

if ans.lower()=="uae":
    print('correct!')
    score =+ 1
else:
    print('incorrect!')
    
print("Thank you for playing , you got" + str(score) + 'questions correct')
percent = (score/totalquestions)* 100
print("mark:" + str(int(percent)) + '%')

if percent >=75:
      print('Congrats you passed')
else:
      print('better luck next time ')

