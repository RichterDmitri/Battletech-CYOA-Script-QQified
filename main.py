import random
import sys
import textwrap

width = 80
def splt_print(msgstart, message):
  global width
  message = textwrap.wrap(message, width-37)
  if(message[-1][:-1] != '.'): message[-1] += '.'
  print(msgstart + ' ' + message[0])
  if (len(message) > 1):
    for _ in message[1:-1]:
      if (_[0] == ' '): _ = _[2:]
      if (_[-1] == ','): _ = _[:-1]
      print('\t\t\t\t\t\t: ' + _)
    print('\t\t\t\t\t\t: ' + message[-1])



Gender = ['Female', 'Male','Player Choice','Masculine True Hermaphrodite','Feminine True Hermaphrodite','Androgynous True Hermaphrodite', ]
Location = [['Lyran Commonwealth', 'Tharkad', 'Tharkad City'],
            ['Free Worlds League', 'Atreus', 'Atreus City'],
            ['Capellan Confederation', 'Sian', 'Forbidden City'],
            ['Federated Suns', 'New Avalon', 'Avalon City'],
            ['Draconis Combine', 'Luthien', 'Luthien'],
            ['Outworlds Alliance', 'Alpheratz', 'Famindas'],
            ['Taurian Concordat', 'Taurus', 'Samantha'],
            ['Magistracy of Canopus', 'Canopus IV', 'Crimson'],
            ['Terra', 'Terra', 'Geneva'],
            ['Gillfillan\'s Gold','Gillfillan\'s Gold','Maroo'],
            ['Player Choice']
           ]
Heir = ['Female, legitimate, doesn\'t care about you',
        'Female, legitimate, is angry at your existence',
        'Male, legitimate, doesn\'t care about you',
        'Male, legitimate, is angry at your existence',
        'Distant female cousin who has no idea who you are',
        'Distant male cousin who has no idea who you are',
        'Granddaughter who wants to find out more about you',
        'Grandson who\'s ashamed of his grandfather\'s lecherous ways',
        'Adopted ward from a tragic background',
        'No one, but due to a quirk of law, you can\'t get the title']
Jumpships = ['One Invader-Class and one Scout-Class JumpShip',
             'One Invader-Class and one Merchant-Class JumpShip',
             'Two Invader-Class JumpShips',
             'One Invader-Class and one Tramp-Class JumpShip',
             'One Invader-Class and one Star Lord-Class JumpShip',
             'One Monolith-Class JumpShip']
Dropships = ['Three Union-Class, one Triumph-Class, one Condor-Class DropShip',
             'Two Union-Class, one Fortress-Class, one Triumph-Class, one Leopard-CV DropShip',
             'Three Fortress-Class, one Mule-Class, one Union-CV DropShip',
             'One Overlord-Class, one Mule-Class, one Triumph-Class, one Union-CV DropShip',
             'Two Overlord-Class, one Mule-Class, one Union-CV DropShip',
             'One Excalibur-Class, one Mule-Class, one Triumph-Class, one Vengeance DropShip']
Battlemechs = [[0,0,16,24],
               [0,4,12,24],
               [0,8,16,16],
               [4,12,12,12],
               [8,16,16,0],
               [12,24,4,0]]
ASF = [[0,0,4,16],
       [0,0,10,10],
       [0,0,20,0],
       [0,6,8,6],
       [0,10,10,0],
       [0,16,4,0]]
AFV = [[0,12,20,48],
       [4,12,16,48],
       [8,12,24,36],
       [12,12,28,28],
       [16,16,24,24],
       [20,28,24,8]]
Inheritance = ['You have Crew for one of the JumpShips and one of the DropShips',
               'Crew for all your Jump- and DropShips has already been hired',
               'No Dropship and Jumpship damage and they are all fully crewed',
               'Double your available starting cash',
               'Loyal Minions, surviving members of your father\'s old crew (12 Mech jocks, 2 ASF pilots, 4 tank crews, 1 Platoon), ~none of them are even eighteen',
               'In a sealed case, that only opens to your blood, a map and a key to a very special location. This is on a chip that only decodes to a drop of your blood: ']
Inheritance2 = ['Moon base in an isolated system in the ruins of the Terran Hegemony, ',
                'Hidden underground in the Deep Periphery of the Lyran Commonwealth, ',
                'A submarine factory on a planet boxed in between Oriente, Andurien, and Regulus, ',
                'Built into a tropical island with an active volcano in the Magistracy, ',
                'A massive asteroid in the Hyades built overtop an ancient Hegemony listening post built before the Reunification War, ',
                'Hidden beneath a distillery on a planet in the Outworlds Alliance, ']
Inheritance3 = ['Star League era medical technology (stasis pods, cyberware)',
                'Star League era air filtration systems',
                'Star League era water filtration systems',
                'Star League era terraforming systems (non Water Filtration)',
                'industrial Mechs',
                'military equipment (all L1)']
Quirks = ['You are directly related to someone who went with Kerensky',
          'Your childhood involved a lot of travel, you\'re certified on spacesuits and comfortable in Zero G',
          'You are distantly related to the ruling family of your nation (on the wrong side of the sheets)',
          'You have the potential for Phantom Mech/ASF',
          'You are notably bright and finished a Business & Management degree',
          'You are enrolled in a proper military university and begin training in April']
Disadvantage = ['Hated and Reviled: You are probably descended from the Amaris family',
                'Barred from Service: You can never work for your starting location or your father\'s Origin',
                'A Hated Foe: A mercenary Colonel is your undying rival',
                'Suffer the Stars: You suffer a severe case of TDS',
                'Thou Art No Knight: You cannot use a Neurohelmet',
                'Countersuit: The Armed Forces of your home have filed a counterclaim to your inheritance',
                'Bad Reputation: Your reputation is tarred due to something you or your father did',
                'Gold Diggers: Your massive inheritance hasn\'t gone unnoticed and now you\'re being stalked by those wanting a piece of the pie',
                'The Sins of the Father: You are wanted in your father\'s home state',
                'The Sins of the Child: You are wated in your home state, once the inheritance of your gear is made public (',
                'In the Name of Blake: Comstar is being very helpful in filling your unit out for you']

try:
  if (sys.version_info >= (3,0)):
    width = int(input("Introduce text width (default: 80, min: 40) "))
  else:
    width = int(raw_input("Introduce text width (default: 80, min: 40) "))
except:
    width = 80
if (width < 40): width = 80
if (width > 5000): width = 80

if (sys.version_info >= (3,0)):
    dbtoggle = (input("Generate a random disadvantage or will you pick two instead (y/n)? ")).lower()
else:
    dbtoggle = (raw_input("Generate a random disadvantage or will you pick two instead (y/n)? ")).lower()
if (dbtoggle == "yes" or dbtoggle == "y"): dbtoggle = True
else: dbtoggle = False

roll_again = "yes" or "y"
while (roll_again == "yes" or roll_again == "y"):
    i = [random.randint(1, 10) for _ in range(5)]
    i += [random.randint(1,6) for _ in range(14)]
    if (i[15] == 6): i+= [random.randint(1,6) for _ in range(2)]
    
    splt_print('Name\t\t\t\t\t:', '?')
    splt_print('Gender\t\t\t\t\t:', Gender[i[0]%7])
    splt_print('Age\t\t\t\t\t\t:','20')
    splt_print('Location & Citizenship\t:', Location[i[1]-1][2] + ', ' + Location[i[1]-1][1] + ', ' + Location[i[1]-1][0])
    money = (i[13]+i[14]+48-i[5]-i[8]-i[10]-i[11]-i[12])*4
    if (i[15] == 4): money *= 2
    splt_print('Money\t\t\t\t\t:', str(money) + ' million C-Bills')
    splt_print('Quirks\t\t\t\t\t:', Quirks[i[16]-1])    
    msg = Inheritance[i[15]-1]
    if (i[15] == 6):
        msg += Inheritance2[i[19]-1]
        if (i[20] == 5):
            msg += str(random.randint(2,4)) + ' ' + Inheritance3[i[20]-1]
        elif (i[20] == 6):
            msg += str(random.randint(1,2)) + ' ' + Inheritance3[i[20]-1]
        else:
            msg += Inheritance3[i[20]-1]
    splt_print('Special Inheritance\t\t:', msg)
    if (dbtoggle):
        msg = Disadvantage[i[17]+i[18]-2]
        if (i[17]+i[18] == 11): msg += ' ' + str(random.randint(2,4)) + ' months before a warrant is issued for your arrest)'
    else:
        msg = '--'
    splt_print('Disadvantages\t\t\t:', msg)
    splt_print('\nFather\'s Nationality\t:', Location[i[2]-1][0])
    splt_print('Siblings\t\t\t\t:', str(i[3]+1))
    splt_print('Father\'s Heir\t\t\t:', Heir[i[4]-1])

    print('\n------- Equipment -------')
    if (i[15] == 3):
        splt_print('- Jumpships\t\t\t\t:', Jumpships[i[5]-1])
        splt_print('- Dropships\t\t\t\t:', Dropships[i[8]-1])
    else:
        splt_print('- Jumpships\t\t\t\t:', Jumpships[i[5]-1] + ', ' + str(i[5]*(i[6]+i[7])*2) + ' million C-Bills of damage')
        splt_print('- Dropships\t\t\t\t:', Dropships[i[8]-1] + ', ' + str(i[8]*i[9]) + ' million C-Bills of damage')
    msg = ''
    if (Battlemechs[i[10]-1][0]): msg += str(Battlemechs[i[10]-1][0]) + ' Assault, '
    if (Battlemechs[i[10]-1][1]): msg += str(Battlemechs[i[10]-1][1]) + ' Heavy, '
    if (Battlemechs[i[10]-1][2]): msg += str(Battlemechs[i[10]-1][2]) + ' Medium'
    if (Battlemechs[i[10]-1][3]): msg += ', ' + str(Battlemechs[i[10]-1][3]) + ' Light'
    splt_print('- Battlemechs\t\t\t:', msg)
    msg = ''
    if (ASF[i[11]-1][0]): msg += str(ASF[i[11]-1][0]) + ' Assault, '
    if (ASF[i[11]-1][1]): msg += str(ASF[i[11]-1][1]) + ' Heavy, '
    if (ASF[i[11]-1][2]): msg += str(ASF[i[11]-1][2]) + ' Medium'
    if (ASF[i[11]-1][3]): msg += ', ' + str(ASF[i[11]-1][3]) + ' Light'
    splt_print('- ASFs\t\t\t\t\t:', msg)
    msg = ''
    if (AFV[i[12]-1][0]): msg += str(AFV[i[12]-1][0]) + ' Assault, '
    if (AFV[i[12]-1][1]): msg += str(AFV[i[12]-1][1]) + ' Heavy, '
    if (AFV[i[12]-1][2]): msg += str(AFV[i[12]-1][2]) + ' Medium'
    if (AFV[i[12]-1][3]): msg += ', ' + str(AFV[i[12]-1][3]) + ' Light'
    splt_print('- AFVs\t\t\t\t\t:', msg)
    splt_print('- Motor Pool\t\t\t:', 'APCs (3 Heavy Wheeled, 3 Heavy Hover, 4 Heavy Tracked), Field HQ, Mash Truck, Battlemech Recovery, 12 Engineering Vehicles, 40 Trucks (10 Tons), 6 towed Longtom Artillery, 12 towed Sniper Artillery')
    print('\n\n')
    if (sys.version_info >= (3,0)):
        roll_again = (input("Roll the dices again? ")).lower()
    else:
        roll_again = (raw_input("Roll the dices again? ")).lower()
