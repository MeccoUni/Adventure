
print("You are solo wanderer. You travel kingdom to kingdom. Not staying in one place long.")
print("You were currently in a small town. Nothing, but your trusty bow and arrows with you.")
print("You notice a shiny necklace in the window of a shop.")
print("Do you STEAL or LEAVE it?")

do = input(":: ")
if do == "STEAL":
    print("You steal the necklace, but you are spotted in the process.")
    print("RUN or TURN IN yourself?")

    do = input(":: ")
    if do == "TURN IN":
        print("Well, you got arrested.")
        print("Now you're in jail. :(")

    elif do == "RUN":
        print("You take off to the woods. Unfortunately, guards are on your tail.")
        print("Run to the LEFT or RIGHT to escape?")

        do = input(":: ")
        if do == "RIGHT":
            print("You get away by squeezing through tall bramble bushes. You have a few nicks and scrapes.")
            print("Hunger hits due to the running. Lucky for you, you see a deer. HUNT or SPARE the deer?")

            do = input(":: ")
            if do == "HUNT" or "SPARE":
                print("Before you can do anything roots from the ground entangle you. You can't free yourself.")
                print("You hear a voice asking 'Who are you?' You say you won't answer unless they show themself.")
                print("A figure steps out from behind a tree. You can't get a good look, only a silhouette.")
                print("Maybe you should have asked for them to step into the light? Either way you give a fake name.")
                print("'I know that's not your really name.' Huh? How did they know?")
                print("'You can not fool a guardian.' The woman you now see stepping out. You're in trouble.")
                print("You could SHOW how sorry you are or NOT.")

                do = input(":: ")
                if do == "SHOW":
                    print("You manage to slip your hand free to show the necklace you stole.")
                    print("You ask is it enough for forgiveness.")
                    print("The woman comes closer to get a better look at the necklace. Her eyes light up.")
                    print("Before you know it she goes on about how she thought she lost it forever.")
                    print("She releases your root restraints and thanks you. Adding you are welcome to come back.")
                    print("Strangely enough you agree. Having a guardian as a friend isn't too bad, right?")

                elif do == "NOT":
                    print("You say she's crazy even though you are tangled in roots. That definitely made her upset.")
                    print("The roots get tighter. So tight, let just say you are aliven't.")

        elif do == "LEFT":
            print("You're met with a cliff and no where else to go.")
            print("Guess you're going to jail after all. :(")

elif do == "LEAVE":
    print("You walk pass the shop and go back to your ordinary life.")
    print("Maybe you could have changed that?")
