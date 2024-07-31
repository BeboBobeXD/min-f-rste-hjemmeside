from random import randint
spil_igen = True
score = 0
while spil_igen:
 gameover = randint(1, 3)
 valg = input('1,2 eller 3?')
 valg_num = int(valg)

 if valg_num == gameover:
    
  print ('hej med dig jeg hedder Kaj hehe')
  print ('Du har tabt fordi Kaj har fanget dig')
  print('din score er ',+ score)
  spil_igen = False

 else:
    
  print('Du var heldig denne gang')
  score = score + 1
  print('din score er nu',+ score)


