# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bg normal = "background.png"
image bg black = "blackBG.png"
image room good = "niceRoom.jpg"
image room bad = "badRoom.jpg"

# Declare characters used by this game.
define t = Character('Master Teacher', color="#c8ffc8")

# Declare variables used within the game.
init:
    # Configuration variables/settings
    $ config.name = "A Semester as a Teacher"
    $ config.window_title = "A Semester as a Teacher"
    $ config.main_menu_music = "Main_Menu_BGM_B.mp3"
    
    # Stat variables
    $ grading = int(0)
    $ planning = int(2)
    $ testPrep = int(0)
    $ meeting = False # Checks to see if there is a meeting, 
                      # if so set to true and that week's school related thing is null and void, still decrease.
    $ familyHappiness = 3 # Value of family's happiness, must keep at or above 0.
    $ goodRoom = False
    $ fallBreak = False
    $ weekCnt = int(-3)
    
    # Only shows the extra text on the choices on the first time they were picked.
    # Helps stop the repetition and blind clicking.
    $ gradingText = False
    $ planningText = False
    $ testPrepText = False
    $ familyHappinessText = False
    $ statMultiplier = int(1)
    
#START Stat Screen Code
screen button:
    vbox xalign 0.0 yalign 0.0:
        textbutton "Statistics" action ui.callsinnewcontext("stat_screen_label")
            
screen stat_screen:
    frame:
        has vbox
        text "Week #[weekCnt]"
        text "Grading pile-up: [grading] weeks"
        text "Lesson Plans Left: [planning] weeks"
        text "Tests Prepared: [testPrep] tests"
        text "Family Happiness: [familyHappiness] points"
        if goodRoom == True:
            text "Good classroom"
        else:
            text "Dull classroom"
        textbutton "Return" action Return()

label stat_screen_label:
    call screen stat_screen
    return
#END Stat Screen Code

# The game starts here.
# This is the main loop/area of the game.
label start:
    show bg normal
    stop music fadeout 3.0
    play music "BGM01_B.mp3" fadein 1.0 loop
    "Welcome to your first semester as an Elementary School teacher."
    "It is up to you whether or not you can withstand the pressures that will come your way."
    
    "-- 3 Weeks Before Classes Start --"
    "As an elementary school teacher, it is important to have a room that is interesting to the children and enough suppiles to last a while."
    "Given this, you must decide how much to spend on these suppiles for your room."
    "Keep in mind that most teachers, starting off, only make about $35000 a year and you have to take care of everything else in life on top of this."
    
    menu:
        "$750.00":
            $ supplySpending = int(750)
        "$500.00":
            $ supplySpending = int(500)
        "$250.00":
            $ supplySpending = int(250)
        "$0.00":
            "You hope that the supplies the school gives you will be enough to get through the semester."
            $ supplySpending = int(0)

    "You go out and buy what supplies you can with your intended budget, hopefully it is enough to look nice without breaking the bank."
    
    $ weekCnt += 1
    "-- 2 Weeks Before Classes Start --"
    "It is the time for new teacher training."
    "Throughout the week an older and more experienced teacher in a similar grade will help you get ready for the upcoming year."
    t "Now to help you all out, I will provide two weeks of sample lesson plans that you can use."
    t "You've got to start somewhere and hopefully these provide a solid foundation upon which you can build your teaching carrers."
    "With these lesson plans, you don't have to worry about making them for the first week or so of classes."
    
    $ weekCnt += 1
    "-- 1 Week Before Classes Start --"
    "This is the first week that you've had access to your room."
    "As such your time is comprosed of getting your classroom ready and staff meetings."
    "These meetings comprise of going over the basics, the goals for the year, the who's who of team leaders and generally getting the teachers motivated."
    
    if supplySpending >= 500:
        hide bg normal
        with fade
        show room good
        with dissolve
        $ goodRoom = True
        "This is what your classroom looks like with supplies that you, yourself, have provided."
        "The students will enter the year with increased vigor for learning and they will also be more attentive."
    else:
        hide bg normal
        with fade
        show room bad
        with dissolve
        if supplySpending == 0:
            "This is what your classroom looks like with only the supplies provided by the school."
            "The classroom looks drab and dull."
        if supplySpending == 250:
            "While you spent some money on pencils and other necessities, the classroom looks drab and dull."
        "As such, the students will be less attentive and are less likely to put their best foot forward."
        
    # Has to be two as otherwise you'd start on week 0, which is weird to most people.
    $ weekCnt += 2 
    "-- The week classes start --"    
    "This is the first week of classes, the students begin to arrive and you follow the plans that the master teacher had made for your grade and you do a good job."
    "You realize that you have to balance your grading, planning, test prep and your family life in such a manner to get through this semester."    
    "If you don't spend enough time prepping or grading, the students will lose sight of their learning which will impact them later down the road."
    "Yet, if you don't spend enough time at home your family will get sad and you'll begin to miss important events in your children's lives."
    "It is this dichotomy of things where the real stuggle as a tacher lies as the work doesn't end when the students go home."
    "In order to make things easier for you, there is a stats panel in the upper left corner that shows your current workload."
    
    show screen button
    
    "Would you like to see a description of the statistics?"
    menu:
        "Yes":
            "Grading is accumulative, so you want it as close to zero as possible and it will increase by one each week."
            "Lesson plans are used each week and, as such, you want it above zero at all times."
            "Test prep is unique as you can only prep for two weeks in advance as they would become less effective as time progresses."
            "Tests are, normally, given at week 7, which is before fall break, and week 18, in place of a final."
            "Family happiness is simply a point system wherein it must be above zero and it decreases by one each week."
            #play music "BGM02.mp3" fadein 1.0 loop
        "No":
            #play music "BGM02.mp3" fadein 1.0 loop
            jump weekStart
label weekStart:
    jump statCheck
    
label statCheckEnd:
    if weekCnt <= 18:
        if weekCnt == 4:
            $ meeting = True
        if weekCnt == 6:
            "Next week is midterm exams and you are expected to have one ready by then."
        if weekCnt == 7:
            "It is the week of tests."
            jump testCheck
            #Something about mid-term testing.
        if weekCnt == 8:
            "It is Fall Break, as such you have the ability to get double the work done."
            "You can make two choices this week, and you won't lose in the other categories."
            $ fallBreak = True
            $ statMultiplier = 0
        if weekCnt == 17:
            "The last test before winter break and the end of the semester is next week."
            "Be prepared for this as you are required to give one to the students."
        if weekCnt == 18:
            "It is the week of final exams, should you have an exam ready to give you are home free for winter break!"
            #"Hopefully you've realized the immense work load that teachers have that many don't realize." # <- Kinda heavy handed line, may need to rework.
            jump testCheck
        
        jump chooseForWeek

label endGame:
    return
#END MAIN GAME CODE    

#This is a function/call that deals with the variables for each week.
label chooseForWeek:
    
    if meeting == False:
        "It is week #[weekCnt] and you must choose what to devote your time to for this coming week."
        menu:
            "Work on grading assignments and tests.":
                $ grading -= 2 # Grading accumulates, therefore it needs to be lessened.
                $ planning -= 1 * statMultiplier
                $ testPrep -= 1 * statMultiplier
                $ familyHappiness -= 1 * statMultiplier
                if not(gradingText):
                    "You decide to spend your time working on the pile up of assignments to grade."
                    "You managed to get a few weeks worth of assignments taken care of."
                    $ gradingText = True
            
            "Work on lesson plans for the coming weeks.":
                $ grading += 1 * statMultiplier
                $ planning += 2
                $ testPrep -= 1 * statMultiplier
                $ familyHappiness -= 1 * statMultiplier
                if not(planningText):
                    "You decide to spend your time working on lesson plans and coming up with new ideas about things to teach the students."
                    "Hopefully they will enjoy your lessons and be able to learn efficiently from it."
                    $ planningText = True
                
            "Prepare tests for the coming weeks.":
                $ grading += 1  * statMultiplier
                $ planning -= 1 * statMultiplier
                $ testPrep = 2
                $ familyHappiness -= 1 * statMultiplier
                if not(testPrepText):
                    "You realize tests are coming up and as such, you spend your week thinking of questions you can ask to gague how your students are doing."
                    "These tests will last a few weeks, but too much longer and the students will be well past that material."
                    $ testPrepText = True
                
            "Spend time with the family.":
                $ grading += 1 * statMultiplier
                $ planning -= 1 * statMultiplier
                $ testPrep -= 1 * statMultiplier
                $ familyHappiness += 3
                if not(familyHappinessText):
                    "With all of the work you've been putting in, you realize you ought to spend some time with the family."
                    "They are happy to have your company and you go on to make some good memories that should last for awhile."
                    "With that said, grades are piling up and lesson plans are being used while you do this."
                    $ familyHappinessText = True
                    
            "Spend more money to improve the room." if not(goodRoom):
                $ grading += 1 * statMultiplier
                $ planning -= 1 * statMultiplier
                $ testPrep -= 1 * statMultiplier
                $ familyHappiness -= 1 * statMultiplier
                $ goodRoom = True
                "You spend more money on supplies and spend time throughout the week improving your room."
                "While you weren't able to get to grading or lesson planning, this will help improve the students' learning."
                hide room bad
                with fade
                show room good
                with dissolve
                
            
    if meeting == True:
        #ie. Meetings this week
        "It is week [weekCnt]."
        "You have meetings in the evening this week, and they take up what time you'd use towards preparing for classes."
        $ grading += 1
        $ planning -= 1 * statMultiplier
        $ testPrep -= 1 * statMultiplier
        $ familyHappiness -= 1 * statMultiplier
        $ meeting = False
        
    #Enforces minimum values
    if grading < 0:
        $ grading = 0
    if testPrep < 0:
        $ testPrep = 0
        
# Fall Break Loop START
    # If break, disable loop and allow another choice.
    if fallBreak:
        $ fallBreak = False 
        jump chooseForWeek
            
    # statMultiplier is only 0 during Fall Break
    # Allows choices to only be positive during this time.
    # This resets the multiplier after the break is over.
    if statMultiplier == 0:
        if goodRoom:
            $ statMultiplier = int(1)
        else:
            $ statMultiplier = int(1) #May add detriment to bad room.
# Fall Break Loop END
            
    #Increment week counter
    $ weekCnt += 1
    
    #Go to the label weekStart which then jumps to statCheck.
    #This is the easiest way I could think of doing functions with the limited time I have and the unknown-ness of Ren'py.
    jump weekStart
return

# START StatCheck
label statCheck:
    if grading > 5:
        show bg black
        with fade
        play music "Bad_End.mp3" fadein 1.0 loop
        "You fell behind on grading. So much so that you cannot get out of this pit without outside help."
        "You ask other teachers for help and some do, at the expense of their own time for grading and planning their own classes."
        "You feel as though you owe a debt that will take awhile to pay off and as such, you redouble your efforts."
        "GAME OVER"
        jump endGame
        
    if planning <= 0:
        show bg black
        with fade
        play music "Bad_End.mp3" fadein 1.0 loop
        "You fell behind on lesson planning. So much so that you cannot get out of this pit without outside help."
        "You try as you might, but you worry that this will negatively impact the kids for years as they realize you have been doing impromptu teaching."
        "With some help of online resources, you manage to get things under control but things were never the same again."
        "GAME OVER"
        jump endGame
    #Something about testPrep, put it in on line 132 and 136
    
label familyBadEnd:
    if familyHappiness < 0:
        show bg black
        with fade
        play music "Bad_End.mp3" fadein 1.0 loop
        "While you have been at work planning or grading, life has gone on at home without you."
        "Your children have had important events come and pass and you were not there to experience it."
        "They may tell you about it around the dinner table, but it wasn't the same as being a part of it."
        "You try to devote more time at home, but with how things are it might be an idle promise."
        "Your children may give you a few more chances but they may not expect you to be there."
        "GAME OVER"
        jump endGame
        
    jump statCheckEnd
return
# END StatCheck

label testCheck:
    if testPrep != 0:
        "You, thankfully, had prepared a test in advance but recent enough to challenege the students."
        "They complain about the exam, but you know that it is a good measurement as to where they are."
        if goodRoom:
            "With the wonderful learning environment, they do fairly well on the exam."
            "There are some stragglers and exemplars, but all in all it falls along a standard bell curve."
        if not(goodRoom):
            "As the learning environment was not condusive to learning, the students may not do as well."
            "Their grades show a decreased interest in learning and your sour mood takes it toll on your family when you get home."
            $ familyHappiness -= 1
            if familyHappiness < 0:
                jump familyBadEnd
    else:
        jump testCheckBadEnd
        
    if weekCnt == 18:
        jump goodEnd
    else:
        jump chooseForWeek
return

label testCheckBadEnd:
    show bg black
    with fade
    play music "Bad_End.mp3" fadein 1.0 loop
    "You did not have a test prepared, as such you do not know where the students are in regards to their learning."
    "Thankfully another teacher in your grade had one ready and was willing to let you use it, but the deed has been done."
    "This has begun to sow the seeds of discontent among your peers and supervisors and it will take awhile to get back in good standing."
    "Hopefully you do not make this mistake again."
    "GAME OVER"
    jump endGame
return

# goodEnd goes here
label goodEnd:
    show bg normal
    with fade
    "CONGRATULATIONS!"
    "You survived the semester and made it to Winter Break!"
    "While there might have been issues along the way, you managed to surmount them and now you have two weeks before it all starts up again."
    "At least that time it would be summer break."
    if not(goodRoom):
        "You may want to spend a bit more on supplies over the break and \"Wow!\" the students when they get back with a good room."
        "Here is what your room could have looked like:"
        hide room bad
        with fade
        show room good
        with dissolve
    jump endGame
return