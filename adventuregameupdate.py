print("Hello Adventurer!")                            #Adventure Game Jan 2024
print("Welcome to 'The Lone Road'")                   #Title: The Lone Road
print("Print choices seen in CAPS")
print("GOOD LUCK")

def exit():                                           #Functions
    print("That answer is not correct.")
def exit1():
    print("That answer is not the secret.")

answer = input("Are you ready, YES or NO? ").lower()

if answer == "no":
    print("You will never be truly ready")
    quit()
elif answer == "yes": 
    print("Can you find the path? Here we go!!!!")
else:
    print("You answer doesn't make sence...")
    quit()
    
answer = input("You are walking down a road and come to a 4 way split, do you go STRAIGHT LEFT RIGHT or BACK? ").lower() 

if answer == "left":                                    #left route
    answer = input("You come to a thicket of bushes, go AROUND or THRU? ").lower()

    if answer == "around":
        answer = input("You come to a sandy beach, WALK the beach or SWIM the waters? ").lower()
    
        
        if answer == "walk":
            answer = input("You walked for a while until you see a path, do you walk the PATH or follow the BEACH? ").lower()
        
            
            if answer == "path":
                print("The path leads you to Treasures, what a wild adventure!!!! YOU WIN")
            elif answer == "beach":
                print("You continue down the beach for days until you can no longer walk!!!! YOU LOSE")   
            else:
                exit()
        elif answer == "swim":
            print("You attempted to brave the waters, to no avail!!!! YOU LOSE")
        else:
            exit()
    elif answer == "thru":
        print("You got stuck in the thicket and eaten by misqitos!!!! YOU LOSE")
    else:
        exit()
elif answer == "right":                                #right route
    answer = input("You walk for awhile coming to another split in the road, do you go LEFT or RIGHT? ").lower()
    
    if answer == "right":
        print("You continue right yet again, only to be wrong, a GIANT snake eats you!!!! YOU LOSE")
    elif answer == "left":
        answer = input("You continue until you hear a sound, do you investigate YES or NO? ").lower()
        
        if answer == "yes":
            print("You investigate, you head around the corner and see a DRAGON sitting upon a pile of gold, he turns you to ash!!!! YOU LOSE")
        elif answer == "no":
            answer = input("You ignore the sound and keep going, you see a clearing, head TOWARDS or AWAY from the clearing? ").lower()
                
            if answer == "away":
                print("You head away for the clearing, the forest darkens and you lose your way!!!! YOU LOSE")
            elif answer == "towards":
                answer = input("You head thru the clearing and onto a beach, you see a path, follow the PATH or BEACH? ").lower()
                
                if answer == "path":
                    print("The path leads you to Treasures, what a wild adventure!!!! YOU WIN")
                elif answer == "beach":
                    print("You continue down the beach for days until you can no longer walk!!!! YOU LOSE")
                else:
                    exit()
            else:
                exit()
        else:
            exit()
    else:
        exit() 
elif answer == "straight":                             #straight route
    answer = input("The road seems to go on forever. Eventually you arrive at a cottage, do you go in YES or NO? ").lower()

    if answer == "no":
        print("You continue walking for days and daze only to become dazed!!!! YOU LOSE")
    elif answer == "yes":
        answer = input("You enter the cottage, it appears to have been abandoned for quite some time, you scavenge food and water, do you spend the night, STAY or GO? ").lower()
        
        if answer == "stay":
            print("You fall asleep with a full belly next to a warm fire. A bear smells your good fortune, ravenges the cottage and tears you to shreds!!!! YOU LOSE")
        elif answer == "go":
            answer = input("You ate some rations and headed back out. You see a trail behind the cottage, ROAD or TRAIL? ").lower()

            if answer == "road":
                print("The route was rough and hard to traverse, you run into a blockade of cars, forcing you to stop for the night. You eat sleep and tell spooky stories to yourself over your makeshift campfire. Becoming quite attached to yourself You dont lose but you also dont win, you live your life as a nomad and wandering drifter meandering from town to village in search of an exact clone of yourself to keep you company for the rest of your drifting days.")
            elif answer == "trail":
                answer = input("The route was rough and hard to traverse it took longer than expected, you arrive at a hill, do you go AROUND or CLIMB the hill? ").lower()

                if answer == "climb":
                    print("You climb the hill that seems like a mountain, immensely tired now you fall climbing down the hill breaking your ankle!!!! YOU LOSE")
                elif answer == "around":
                    answer = input("You go around the hill safely coming a to river, do you CROSS or FOLLOW the river? ").lower()

                    if answer == "cross":
                        print("You attempt to cross the river but are swept away by current!!!! YOU LOSE")
                    elif answer == "follow":
                        answer = input("You follow the river it leads to a beach, do you SWIM or WALK the beach? ").lower()

                        if answer == "swim":
                            print("You swim and swim, until a shark eats you!!!! YOU LOSE")
                        elif answer == "walk":
                            answer = input("You walk the beach until you see a path, go down the path NOW or LATER? ").lower()

                            if answer == "now":
                                print("The path leads you to Treasures, what a wild adventure!!!! YOU WIN")
                            elif answer == "later":
                                print("The path leads you to Treasures, what a wild adventure!!!! YOU WIN")
                            else:
                                exit()
                        else:
                            exit()
                    else:
                        exit()
                else:
                    exit()
            else:
                exit()
        else:
            exit()
    else:
        exit()
elif answer == "back":                                 #back route
    answer = input("You go back the way you came, BACK or NO? ").lower()

    if answer == "back":
        print("You go back again, your stuck in a loop, not a real loop, just a loopy loop!!!! YOU LOSE")
    elif answer == "no":
        answer = input("You stopped going back just as you began to not recognize the reverse route you took, theres a road that looks promicing do you go LEFT or RIGHT? ").lower()

        if answer == "left":
            print("You go left you come to a downed tree blocking your route, you try moving the tree, to no avail. All your energy is spent you sit down for a little bit, Kirby comes around the corner and sucks you up!!!! YOU LOSE")
        elif answer== "right":
            answer = input("You go down the right way you feel quite confident this will lead to somewhere promicing, a land of riches perhaps. Halfway thru your daydream you come to a stream do you SWIM or FOLLOW the stream? ").lower()

            if answer == "swim":
                print("You go for a dip enjoying the perfect water temp until you get eaten by piranhas!!!! YOU LOSE")
            elif answer == "follow":
                answer = input("You follow the stream, it has to lead somewhere but theres nothing in sight so far do you STRAY away or FOLLOW the stream? ").lower()

                if answer == "stray":
                    print("You stray away from the stream knowing it wasnt a good idea. You walk and walk through feilds of flowers, feilds of wheat, and feilds of cows but you dont find a land of riches, you find cows!!!! YOU LOSE")
                elif answer == "follow":
                    answer = input("You continue to follow the stream for a day, stopping only to catch a fish do you stop to make CAMP or NOT? ").lower()

                    if answer == "not":
                        print("You decide to continue without making camp, you are mighty hungry by the time night falls, and so are the wolves that just picked up your scent. Its not long before you are swarmed by a PACK of wolves!!!! YOU LOSE")
                    elif answer == "camp":
                        answer = input("You made camp setting up a makeshift shack out of sticks and tree limbs also building a fire and cooking your delicious fish you caught earlier. Eating it and enoying the beutiful clear night. In the morning you wake up with a full belly and plenty of energy ready to tackle the day. You pack up camp do you FOLLOW the stream or NOT? ").lower()

                        if answer == "not":
                            print("You do not continue to follow the stream instead walking in a diffent direction. This leads to a herd of bulls, you are wearing red so all the bulls charge at you!!!! YOU LOSE")
                        elif answer == "follow":
                            answer = input("Knowing this will lead the right way you follow the stream, after walking for miles you finally see a BEACH and PATH which way will you go? ").lower()

                            if answer == "beach":
                                print("You walk the beach and enjoy the sand going swimming at one point, tasting the water, knowing that you would be as salty as the ocean when you never reach the path to treasure!!!! YOU LOSE")
                            elif answer == "path":
                                print("The path leads you to Treasures, what a wild adventure!!!! YOU WIN")
                            else:
                                exit()
                        else:
                            exit()
                    else:
                        exit()
                else:
                    exit()
            else:
                exit()
        else:
            exit()
    else:
        exit()
elif answer == "secret":                               #secret route
    answer = input("You have found a secret hatch that is sealed, you can LOOK around or PRY or SMACK the lock. ").lower()

    if answer == "look":
        answer = input("You look around, there is a MAT a ROCK, and a HOLE in the wall. ").lower()

        if answer == "mat":
            answer = input("You look under the mat on the floor, spotting a key that unlocks the lock, do you go THRU or WAIT? ").lower()

            if answer == "thru":
                print("You go thru the secret hatch finding jawas that trade you a few good droids for the right amount of credits!!!!YOU WIN but so do the jawas")
            elif answer == "wait":
                print("You wait and go nowhere, it seems you are still where you started!!!! YOU LOSE")
            else:
                exit1()
        elif answer == "rock":
            answer = input ("You pick up the rock, finding no key under it you can either put the rock DOWN or SMASH the lock? ").lower()

            if answer == "down":
                answer = input("You put the rock down also letting yourself down. Obi Wan is not here there is no HOPE!!!! You Lose ").lower()

                if answer == "hope":
                    print("OBI WAN was with us, he is always with us, you use the force and i am compelled to give you all the riches in this game!!!! YOU WIN")
                else:
                    exit1()
            elif answer == "smash":
                answer = input("You decide the only thing left to do is smash the lock. With a great hurl and flawless technique the rock smashes the lock breaking the mechanism and crumbiling the rock also, the hatch flings open. Do you go THRU or WAIT? ").lower()

                if answer == "thru":
                    print("You go thru the secret hatch finding Luke Skywalker!!!!YOU WIN")
                elif answer == "wait":
                    print("You wait and go nowhere, it seems you are still where you started!!!! YOU LOSE")
                else:
                    exit1()
            else:
                exit1()
        elif answer == "hole":
            print("You spot a hole in the wall, thinking it could be something useful you reach in. To no surprise you lose your arm and the game to the secret and arm eating monster!!!! YOU LOSE")
        else:
            exit1()
    elif answer == "pry":
        answer = input("You PRY and PRY, oh how you PRY. ").lower()

        if answer == "pry":
            answer = input("You PRY some more finally having some luck, it budges. ").lower()

            if answer == "pry":
                answer = input ("With a little intuition on your side you pry again with all your might, the hatch opens what awaits you? Go THRU or WAIT? ").lower()

                if answer == "thru":
                    print("You have found GrandMaster Yoda!!!! ")
                    print("Found me you have, in order, congragulations is!!!! YOU WIN")
                elif answer == "wait":
                    print("You wait for a bit your gut tells you to go thru at a peculiar time")
                    print("You have found GrandMaster Yoda. You hear.... ")
                    print("Patience you covet, Found me you have, in order congragulations is!!!! You study under the great Grandmaster Yoda for years and become a far greater jedi than I could ever be. He grants you the Rank of MASTER!!!! YOU WIN")
                else:
                    exit1()
            else:
                exit1()
        else:
            exit1()
    elif answer == "smack":
        answer = input("You smack, hear a whack, and it opens go THRU or WAIT? ").lower()

        if answer == "thru":
            print("You go thru the secret hatch finding Princess Leia in the Jaba slave outfit!!!! YOU WIN")
        elif answer == "wait":
            print("You wait and go nowhere, it seems you are still where you started!!!! YOU LOSE")
        else:
            exit1()
    else:
        exit1()
else:
    exit()
