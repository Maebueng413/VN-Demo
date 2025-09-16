# The script of the game goes in this file.
# The game starts here.

transform midleft:
    yalign 1.0
    xcenter 0.25

transform midright:
    yalign 1.0
    xcenter 0.75

label start:
    
    n"The breeze is uncomfortable. Normally people would praise a cool breeze on a summer day, 
    but you’re resenting it."
    
    n"You can feel every blow downwind, or more accurately downstairs."
    
    scene bg_icecream with dissolve
    play music outdoor_summer volume 3.0
    
    n"After a freak banana peel incident at the ice cream parlor, all your coworkers got a look 
    at your unmentionables when your pants decided to split."
    
    n"(It’s not funny...)"

    n"Your manager was nice enough to lend you apron, but this was barely longer than the hand
    towels at home"

    n"Normally you could count on your aunt, you've already called her for a ride, 
    but she's in the next county over for some type of squash competition. 
    She works all year long for these competitions"
    
    n"If there's one thing you can remember about your summer visits, it's that the humidity
    will make your shirt stick and Aunt Delilah will always bring a blue ribbon home"

    n"Though the situation wasn't ideal, hearing her voice brought a sense a relief.
    Even if it was drowned out by the festival in the back"

    auntdelialh "I'm so so sorry honey bumpkin!
    I'd be there if I could, but the traffic will be horrendous!"
    
    auntdelialh "Why don't you call your cousin? Chrissy left early this morning, she should be
    home by now!"
    
    auntdelialh "Oh, I gotta get going, love you! I'll make sure to bring back some funnel cake!"

    play audio end_call # always put sound effects before next line so there's no delay
    n "*Beep beep beep*"
    

    n "The call ended before you could get in your goodbye. You sit in silence for a few seconds before you contemplate on what to do next"

    n "You could take your aunt's advice and call your cousin to pick you up and wait as you have to deal with this annoying draft"

    n "Or you could just make a mad dash back to your house. More people would see your delicates but at least you'll be able to change sooner"

    # Choice tree

    menu:
        "Walk Home": 
            jump walk_home

        "Call Chrissy":
            jump call_chrissy


    # This ends the game.

    return

label walk_home:
    n "You could call her, but she might not be home yet. Or she could be busy, she's been very busy lately..."
            
    n "The walk wouldn't kill you! Though the heat might..."

    n "No use waiting around, you trudge forward and keep a hand clasped
    to the back of your pants so the apron wouldn't blow"

    n "It's akward and there's a soreness in your ice cream scooping arm,
    but the walk home was only a couple blocks"


    play audio k7_snicker volume 0.5
    n "There were a few stares, a pair of lovebirds on their porch whispered to
    themselves while some kids playing in the street laughed after you passed by"

    play audio car_stop
    n "Coming up the hill you can see your home in the distance when a familiar
    minivan slows to a roll right beside you"

    show chrissy_cheetah at midleft with dissolve # testing alignments
    mystery "Hey flasher! Need some help handling those goods?"

    n "High voice? Top 40's on the radio? Acrylic nails tapping
    against the wheel? No question about, it's Chrissy..."

    n "End of demo"

    return

label call_chrissy:
    n "This day couldn't get any worse. Guess it's time to break the 
    emergency glass, tough you doubt she'd pick up"
    play audio phone_ring
    n "*Brrrrrr*"
    

    n "It rings..."
    play audio phone_ring
    n "*Brrrrrr*"
    

    n "Come on..."
    play audio phone_ring
    n "*Brrrrrr*"
    

    n "Oh, for the love of-"

    chrissy "Hellaaurrr?"

    n "Her high pitched voice blares through your speaker. With a brief greeting you tentatively explain your condition"

    chrissy "Oh my gosh. That's literally insane- and on your shift too! You didn't have that 
    shift with the cutie this time, right?"
    chrissy "Wait, what am I saying... Do you need me to bring you some paints like right now right now?"

    mystery "You have your shorts for tennis tonight in the back-"

    chrissy "*GASP* Oh you're sooo right! Okay pookie, keep your butt parked right there!"
    chrissy "I'm like 20 minutes away, sit down on those benches out front. I'll be there in a jiffy!"

    n "Before you can get a goodbye in the line clicks. No point in telling her that in the same amount of time
    you could've walked home"

    n "As you sit down on one of the grated benches you try to ignore the patrons inside. There's no doubt they can see you
    through the big windows. A few people leave and give you stares. It's not a big deal, accidents happen all the-"
    
    play audio k7_snicker volume 0.5
    n "*Snicker*"
    

    n "Ah, that's right, they where inside the shop when it happened... You raise a hand to cover your face from view"

    play audio car_stop
    n "Before you know it, a beat up minivan slows to a roll in front of you"

    show chrissy_cheetah at midleft with dissolve
    chrissy "Hey stranger! Need a ride?"

    n "Shuffling in, you push away the random plushies she has piled in the back"

    show wren_fish at midright with dissolve
    wren "We don't have any fresh underwear but we can stop at a store and-"

    chrissy "No- No Sweetie, they split their pants, not shit them!"

    wren "OH! Sorry... I heard accident and assumed the worst..."

    n "End of demo"

    return
