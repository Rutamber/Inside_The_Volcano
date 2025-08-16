#This is the alpha version of the text based rpg game, inside the volcano! It is a text based game giving you 2 choices, which affect the story. This is a python game, made only using if-else stataments and print statements. 
print("Welcome to the game, inside the volcano! It is a text based game giving you 2 choices, which affect the story. Enjoy:)")
print("To begin, Please first select Your Age")

age = int(input("Enter your age: "))
if age >= 13: 
    print("You are old enough to play!\n")
  
    print("""The continent of Ingens has very interesting yet powerful kingdoms present on its surface, but the most strongest and the biggest of these kingdoms is the middle kingdom of ‘Inigins Mediora’. Known as the economic and military superpower of the entire known world, Inigins Mediora is quite a famous place among its allies and quite a powerful yet undefeatable force among its foes\n.

 Despite being an almost dreamlike kingdom it is, Inigins Mediora is currently facing a major problem inside its long borders. Mount Caladius, the biggest volcano of Ingens, is repeatedly erupting after every 15 dawns, causing tremendous loss to all the neighbouring areas.\n""") 

    print ("You are king Vetus 3 of Ignis Mediora, How will you approach this problem?\n")
    print ("Choice 1: Will you ask a team of Mages and scholars to analyse the volcano and decide on their findings. To choose this option, Type 1\n")
    print("Choice 2: Meh, Who cares? To choose this option, Type 2\n")
    print("______________________________________________________________________________________________________________")
      
    choice = int(input("Enter your choice: "))
    if choice == 1:
      print("You have chosen to ask a team of mages and scholars to analyse the volcano and decide on their findings.\n")
      print("You have chosen the right option, The team of mages have discovered an ancient rune near the volcano, which has asked you the king, to send your best military forces to the volcano, to stop the eruption.\n")
      print("Now You must first choose your character!")
      print("You have 2 choices, Choose wisely!\n")

      print("Name: Harald, Age: 34, Gender: Male, Race: Human, Occupation: Retired Army Knight now turned Blacksmith, Special Ability: Diplomacy, Sword Mastery, Blacksmithing. To choose Harald, Type 1\n")

      print("Name: Elara, Age: 28, Gender: Female, Race: Elf, Occupation: Retired Assassin, Now turned Farmer, Special Ability: Archery, Stealth, Nature's Blessing. To choose Elara, Type 2")
      print("__________________________________________________________________________________________________________________________")
        
      character = int(input("Enter your choice: \n"))
      if character == 1:
          print("You have chosen Harald!")
          print("Now that you have chosen your character, you may now enter the world of Ignis Mediora!\n ")
          print("""Harald, in his little shack, in the golden sunlight of the morning, was busy with his work, when suddenly he heard a knock on his door, he opened the door and saw a messenger, who was carrying a letter, the messenger said, "This is for you, from King Vetus 3.
          Harald, looked at the letter, and read it, it said, "Harald, I need your help, the volcano is erupting, and I need your help to stop it, please come to the castle, and I will explain everything to you.
          You report to the castle still a bit skeptical, but you know that you have to help your nation, fot if you refuse to help, you will be considered a traitor, and you will be executed.
          You are greeted by King Vetus 3, He explains all about the volcano, and the ancient rune, and how it is asking for your help, to stop the eruption.\n""")
          print("Now you have two choices, either to accept King's request to go near tha volcano or politely object the king's request. If you choose to accept the request, Type 1, if you choose to object the request, Type 2\n")
          print("__________________________________________________________________________________________________________________________")

          choice = int(input("Enter your choice: \n"))
          if choice == 1:
              print("You have chosen to accept King's request to go near the volcano!\n\n")
              print("""[HARALD]: MY LIEGE, YOUR WISH IS MY COMMAND, I SHALL GO TO THE DEPTHS OF THIS MIGHTY EARTH IF I HAVE TO, I SWEAR I WILL NOT FAIL YOU!
              [KING VETUS 3]: HARALD, I KNOW YOU WILL NOT FAIL ME, I KNOW YOU WILL RETURN SAFE AND SOUND! NOW BEFORE YOU GO, I WANT YOU TO MEET MY, ELARA, SHE IS A RETIRED ASSASSIN, NOW TURNED FARMER, SHE IS A GREAT ARCHER, AND A GREAT WARRIOR, SHE WILL BE YOUR COMPANION ON THIS JOURNEY!
              
              [HARALD]: MY LIEGE, I AM HONOURED TO HAVE AN ASSASSIN AS A COMPANION, I KNOW WE WILL RETURN SAFE AND SOUND! NOW WITH YOUR BLESSING, WE ARE HEADING TO THE VOLCANO!
              
              [VETUS 3]: GOOD LUCK, HARALD, AND ELARA, MAY THE GODS BE WITH YOU!\n\n""")
              
              print("""Harald and Elara, set out on their journey to the edge of the volcano which was located at the edge of the kingdom of Ignis Mediora, It was a long and tiring Journey, but they were determined to stop the eruption of the volcano, and save their nation from the destruction of the volcano. They reached the edge of the volcano, and saw the ancient rune, which was glowing with a bright light, and before they could react, A dark black fog surrounded them and blinded them.
              
              [HARALD]: *Coughs* *coughs* WHAT IS THIS SORCERY? WHAT IS HAPPENING HERE!!?
              [ELARA]: *screams* 
              [HARALD]: ELARAAA! WHAT HAPENED!?!?
              
              what will you do now?
              choice 1: If wish to look for Elara?  type 1
              Choice 2: If you want to keep pressing on near the ancient rune, while abandoning Elara, type 2""")
              print("__________________________________________________________________________________________________________________________")
              if choice == 1:
                  print ("You have chosen to look for Elara!\n\n")
                  print("""You run and search through the fog to look for your companion while calling out her name, but you can't find her, suddenly you stumble across something, which was Elara lying on the ground unconcious, you bend down to check her pulse and what happened to her but before you could do so, you were also hit from behind and now you are also unconcious.

                  You later wake up to find yourself in binds near the rim of the volcano, you can see the gigantic volcano head and all the magma beneath it, You are surrounded by dark hooded creatures, who appear to be cultist and are waiting for Elara to wake up as well.

                  [HARALD]: WHAT DO YOU WANT YOU MONSTERS!?!?

                  [CULTISTS (in unison)]: OH GREAT ORC LEADER! SPARE THY SOUL! OH GREAT ORC LEADER SPARE THY SOUL! ACCEPT THIS HUMAN AND THIS ELF AS OUR OFFERING AND SPARE US OF THIS MYSERY!! OH GREAT ORC LEADER SPARE THY SOUL! OH GREAT ORC LEADER SPARE THY SOUL!

                  From all this ruckus Elara wakes up and see the problem they are in, she looks a bit frightened but control herself and then like you.
                  [ELARA]: WHAT THE HELL YOU WANT YOU MONSTERS!?!? 

                  the cultists continue their chanting! and later gather around Harald and Elara chanting more agressively before throwing both of them with their weapons inside the mouth of the volcano

                  both of them yelled NOOOO! but it was too late, they were about to touch the magma and die a fiery death, but, they touched the lava but didn't burned but rather drowned without burning and sinking deeper and deeper into another realm inside the volcano.                                        you sank
                    and sank 
                    and sank
                    now you are again unconcious but still alive but now after 3 long hours you finally fell down from the sky, but were not hurt, and you open yout eyes and see elara waking up as well, you look at your surroundings and see everything is different, You have waoken up not in Ignis Mediora, not in Ignes but in another world, Huge Houses made of Bones and mud surround you in a glowing orange skies, with red lava rivers and orc children playing around you, you look at Elara and she looks at you and you both are just shocked and confused, And then it hits you and your companion, You are in the underworld, in the orcish civilisation of Haldoviin, The same kingdom told in legends you grew up reading, And now you must decide what to do next.""")


              
              elif choice == 2:
                  print("You have chosen to keep pressing on near the ancient rune, while abandoning Elara!\n\n")
                  print("""You keep pressing on near the ancient rune, while abandoning Elara knowing she was just a dead weight and press forward towards the Ancient rune, you saw it glowing with a bright light inside the dark fog but the minute you touch it, you were hit by eerie voices coming from the stone knowcking you unconcious as well.

                  You later wake up to find yourself in binds near the rim of the volcano, you can see the gigantic volcano head and all the magma beneath it, You are surrounded by dark hooded creatures, who appear to be cultist and were waiting for you to wake up only.

                  [HARALD]: WHAT DO YOU WANT YOU MONSTERS!?!?

                  [CULTISTS (in unison)]: OH GREAT ORC LEADER! SPARE THY SOUL! OH GREAT ORC LEADER SPARE THY SOUL! ACCEPT THIS HUMAN AS OUR OFFERING AND SPARE US OF THIS MYSERY!! OH GREAT ORC LEADER SPARE THY SOUL! OH GREAT ORC LEADER SPARE THY SOUL!

                  [HARALD]: I SAID, WHAT THE HELL YOU WANT YOU CULTISTS!?!? 

                  the cultists continue their chanting! and later gather around Harald, now chanting more agressively before throwing him twith his weapons inside the mouth of the volcano

                  Harlad yelled NOOOO! but it was too late, He was about to touch the magma and die a fiery death, but, when He touched the lava, he didn't burned but rather drowned without burning and sinking deeper and deeper into another realm inside the volcano.                                              you sank
                    and sank 
                    and sank
                    now you are again unconcious but still alive but now after 3 long hours you finally fell down from the sky, but were not hurt, and you open yout eyes and see elara waking up as well, you look at your surroundings and see everything is different, You have waoken up not in Ignis Mediora, not in Ignes but in another world, Huge Houses made of Bones and mud surround you in a glowing orange skies, with red lava rivers and orc children playing around you, you look at Elara and she looks at you and you both are just shocked and confused, And then it hits you and your companion, You are in the underworld, in the orcish civilisation of Haldoviin, The same kingdom told in legends you grew up reading, And now you must decide what to do next.""")


              
              else:
                  print ("You have not chosen a valid option, You think you escape this moral dilemma, Hah! Now try again and show some some courage!""")

          

          elif choice == 2:
              print("You have chosen to object King's request to go near the volcano!\n\n")
              print("""[HARALD]: MY LIEGE, I AM SORRY, BUT I CANNOT GO TO THE DEPTHS OF THIS MIGHTY EARTH, I HAVE RETIRED FROM THE ARMY, AND I HAVE NO INTEREST IN GOING TO THE VOLCANO, I AM SORRY, BUT I CANNOT HELP YOU!
              
              [VETUS 3]: HARALD, MY CHILD. I KNOW YOU HAVE RETIRED FROM MY ARMY AND HAVE GIVEN ME FAITHFUL SERVICE FOR PAST FEW DECADES, BUT I NEED YOU HELP. YOU ARE STILL ONE OF THE FINEST WARRIORS I HAVE EVER SEEN, AND I NEED YOUR HELP TO STOP THE ERUPTION OF THE VOLCANO!
              
              Hearing this, Harald's heart was filled with sorrow, he knew that he had to help his nation, but he also knew that he had to help his king, he knew that he had to make a choice, and he made a choice to help his nation and his king, and he said,
              
              [harald]: "MY LIEGE, I WILL GO TO THE DEPTHS OF THIS MIGHTY EARTH, I WILL NOT FAIL YOU! 
              
              [KING VETUS 3]: HARALD, I THANK YOU FROM THE BOTTOM OF MY HEART TO HELP OUR NATION AND I KNOW YOU WILL NOT FAIL ME, I KNOW YOU WILL RETURN SAFE AND SOUND! NOW BEFORE YOU GO, I WANT YOU TO MEET, ELARA, SHE IS A RETIRED ASSASSIN, NOW TURNED FARMER, SHE IS A GREAT ARCHER, AND A GREAT WARRIOR, SHE WILL BE YOUR COMPANION ON THIS JOURNEY!
              
              [HARALD]: MY LIEGE, I AM HONOURED AN ASSASSIN, I KNOW WE WILL RETURN SAFE AND SOUND! NOW WITH YOUR BLESSING, WE ARE HEADING TO THE VOLCANO!
              
              [VETUS 3]: GOOD LUCK, HARALD, AND ELARA, MAY THE GODS BE WITH YOU!\n\n""")
              
              print("""Harald and Elara, set out on their journey to the edge of the volcano which was located at the edge of the kingdom of Ignis Mediora, It was a long and tiring Journey, but they were determined to stop the eruption of the volcano, and save their nation from the destruction of the volcano. They reached the edge of the volcano, and saw the ancient rune, which was glowing with a bright light, and before they could react, A dark black fog surrounded them and blinded them.

                [HARALD]: *Coughs* *coughs* WHAT IS THIS SORCERY? WHAT IS HAPPENING HERE!!?
                [ELARA]: *screams* 
                [HARALD]: ELARAAA! WHAT HAPENED!?!?

                what will you do now?
                choice 1: If wish to look for Elara?  type 1
                Choice 2: If you want to keep pressing on near the ancient rune, while abandoning Elara, type 2""")
              print("__________________________________________________________________________________________________________________________")
              
              choice = int(input("Enter your choice: \n"))
              
              if choice == 1:
                    print ("You have chosen to look for Elara!\n\n")
                    print("""You run and search through the fog to look for your companion while calling out her name, but you can't find her, suddenly you stumble across something, which was Elara lying on the ground unconcious, you bend down to check her pulse and what happened to her but before you could do so, you were also hit from behind and now you are also unconcious.
                    
                    You later wake up to find yourself in binds near the rim of the volcano, you can see the gigantic volcano head and all the magma beneath it, You are surrounded by dark hooded creatures, who appear to be cultist and are waiting for Elara to wake up as well.
                    
                    [HARALD]: WHAT DO YOU WANT YOU MONSTERS!?!?
                    
                    [CULTISTS (in unison)]: OH GREAT ORC LEADER! SPARE THY SOUL! OH GREAT ORC LEADER SPARE THY SOUL! ACCEPT THIS HUMAN AND THIS ELF AS OUR OFFERING AND SPARE US OF THIS MYSERY!! OH GREAT ORC LEADER SPARE THY SOUL! OH GREAT ORC LEADER SPARE THY SOUL!
                   
                    From all this ruckus Elara wakes up and see the problem they are in, she looks a bit frightened but control herself and then like you.
                    [ELARA]: WHAT THE HELL YOU WANT YOU MONSTERS!?!? 
                    
                    the cultists continue their chanting! and later gather around Harald and Elara chanting more agressively before throwing both of them with their weapons inside the mouth of the volcano
                    
                    both of them yelled NOOOO! but it was too late, they were about to touch the magma and die a fiery death, but, they touched the lava but didn't burned but rather drowned without burning and sinking deeper and deeper into another realm inside the volcano.
                    you sank
                    and sank 
                    and sank
                    now you are again unconcious but still alive but now after 3 long hours you finally fell down from the sky, but were not hurt, and you open yout eyes and see elara waking up as well, you look at your surroundings and see everything is different, You have waoken up not in Ignis Mediora, not in Ignes but in another world, Huge Houses made of Bones and mud surround you in a glowing orange skies, with red lava rivers and orc children playing around you, you look at Elara and she looks at you and you both are just shocked and confused, And then it hits you and your companion, You are in the underworld, in the orcish civilisation of Haldoviin, The same kingdom told in legends you grew up reading, And now you must decide what to do next.
                          To be continued""")
                  


              elif choice == 2:
                    print("You have chosen to keep pressing on near the ancient rune, while abandoning Elara!\n\n")
                    print("""You keep pressing on near the ancient rune, while abandoning Elara knowing she was just a dead weight and press forward towards the Ancient rune, you saw it glowing with a bright light inside the dark fog but the minute you touch it, you were hit by eerie voices coming from the stone knowcking you unconcious as well.
                    
                    You later wake up to find yourself in binds near the rim of the volcano, you can see the gigantic volcano head and all the magma beneath it, You are surrounded by dark hooded creatures, who appear to be cultist and were waiting for you to wake up only.

                    [HARALD]: WHAT DO YOU WANT YOU MONSTERS!?!?

                    [CULTISTS (in unison)]: OH GREAT ORC LEADER! SPARE THY SOUL! OH GREAT ORC LEADER SPARE THY SOUL! ACCEPT THIS HUMAN AS OUR OFFERING AND SPARE US OF THIS MYSERY!! OH GREAT ORC LEADER SPARE THY SOUL! OH GREAT ORC LEADER SPARE THY SOUL!

                    [HARALD]: I SAID, WHAT THE HELL YOU WANT YOU CULTISTS!?!? 

                    the cultists continue their chanting! and later gather around Harald, now chanting more agressively before throwing him twith his weapons inside the mouth of the volcano

                    Harlad yelled NOOOO! but it was too late, He was about to touch the magma and die a fiery death, but, when He touched the lava, he didn't burned but rather drowned without burning and sinking deeper and deeper into another realm inside the volcano.
                    you sank
                    and sank 
                    and sank
                    now you are again unconcious but still alive but now after 3 long hours you finally fell down from the sky, but were not hurt, and you open yout eyes and see elara waking up as well, you look at your surroundings and see everything is different, You have waoken up not in Ignis Mediora, not in Ignes but in another world, Huge Houses made of Bones and mud surround you in a glowing orange skies, with red lava rivers and orc children playing around you, you look at Elara and she looks at you and you both are just shocked and confused, And then it hits you and your companion, You are in the underworld, in the orcish civilisation of Haldoviin, The same kingdom told in legends you grew up reading, And now you must decide what to do next.
                          To Be Continued""")


              else:
                    print ("You have not chosen a valid option, You think you escape this moral dilemma, Hah! Now try again and show some some courage!""")

        
          else:
              print("You have not chosen a valid option, You think you escape this moral dilemma, Hah! Now try again and show some some courage!")
        
      elif  character == 2:
            print("You have chosen Elara!")
            print("Now that you have chosen your character, you may now enter the world of Ignis Mediora!\n")
            print("Work In Progress!, You may Play Harald's character for now please!")
      else:
         print("You have not chosen a valid character!")

    elif choice == 2:
        print ("You have chosen to ignore the problem, You have chosen the wrong option, The volcano has erupted, taking your castle, the Kingdom is destroyed, You have lost the game!")
        exit()
    else:
        print("You have not chosen a valid option!")
      
      


elif age == 11:
    print("This is not Hogwarts bro, To enter the world of Ignis Mediora, You must be 13 or older!")
    exit()
else: 
    print("You are not old enough to play!, but don't worry, You may play it once you are 13!")
    exit()
