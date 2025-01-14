import random

def game_play():
    print("Objective, Beat the Computer, Stats: Both Players start with 75 Hp, Not being able to to damage outside of the distance 2 or -2")
    
                         
    d_user = 0
    d_comp = 5
    hp_user = 75
    hp_comp = 75
    
    
#User inputs
    while hp_user >= 0 or hp_comp >= 0:
        Tru = 0
        user = input("Rules Type: 'slash', 'forwards', 'backwards', or 'dash' ")
        
        
        while (user != 'slash') and (user != 'block') and (user != 'parry') and (user != 'forwards') and (user != 'backwards') and (user!= 'dash'):
            user = input("Enter either: 'slash', 'forwards', 'backwards', or 'dash' ")
            
#User Movement
        if user == 'forwards':
            d_user += 1
            if d_comp - d_user >= 2 or d_user - d_comp >= 2:
                print(d_user, "Your distance forward far, End Turn")
            if d_comp - d_user == 2 or d_user - d_comp == 2:
                print(d_user, "Your distance forward medium, End Turn")
            if d_comp - d_user == 1 or d_user - d_comp == 1:
                print(d_user, "Your distance forward close, End Turn")
            if d_comp - d_user == 0:
                print(d_user, "Your distance forward very close, End Turn")
            
        if user == 'backwards':
            d_user -= 1
            if d_comp - d_user >= 2 or d_user - d_comp >= 2:
                print(d_user, "Your distance backwards far, End Turn")
            if d_comp - d_user == 2 or d_user - d_comp == 2:
                print(d_user, "Your distance backwards medium, End Turn")
            if d_comp - d_user == 1 or d_user - d_comp == 1:
                print(d_user, "Your distance backwards close, End Turn")
            if d_comp - d_user == 0:
                print(d_user, "Your distance backwards very close, End Turn")
            
        if user == 'dash':
            user = input("Move: 'forwards' or 'backwards' ")
            while (user != 'forwards') and (user != 'backwards'):
                user = input("Enter either: 'forwards', 'backwards'")
            if user == 'forwards':
                d_user += 2
                if d_comp - d_user >= 2 or d_user - d_comp >= 2:
                    print(d_user, "Your distance dash_f far, End Turn")
                if d_comp - d_user == 2 or d_user - d_comp == 2:
                    print(d_user, "Your distance dash_f medium, End Turn")
                if d_comp - d_user == 1 or d_user - d_comp == 1:
                    print(d_user, "Your distance dash_f close, End Turn")
                if d_comp - d_user == 0:
                    print(d_user, "Your distance dash_f very close, End Turn")
               
            if user == 'backwards':
                d_user -= 2
                if d_comp - d_user >= 2 or d_user - d_comp >= 2:
                    print(d_user, "Your distance dash_b far, End Turn")
                if d_comp - d_user == 2 or d_user - d_comp == 2:
                    print(d_user, "Your distance dash_b medium, End Turn")
                if d_comp - d_user == 1 or d_user - d_comp == 1:
                    print(d_user, "Your distance dash_b close, End Turn")
                if d_comp - d_user == 0:
                    print(d_user, "Your distance dash_b very close, End Turn")
                
#User Conditions
        if user == 'slash':        
            if (d_comp - d_user) > 2 or (d_user - d_comp) > 2:
                print("Far Move failed")
        
            if (d_comp - d_user) == 2 or (d_user - d_comp) == 2:
                user_damage = random.choice([10, 5, 0])
                hp_comp = hp_comp - user_damage 
                if user_damage == 25:
                    print("Medium Move Landed, Critical Hit,", user_damage, "Damage Done", hp_comp, "HP Remaining, End Turn")
                if user_damage == 10:
                    print("Medium Move Landed,", user_damage, "Damage Done", hp_comp, "HP Remaining, End Turn")
                if user_damage == 0:
                    print("Medium Move Missed,", user_damage, "Damage Done", hp_comp, "HP Remaining, End Turn")
            
            if (d_comp - d_user) == 1 or (d_user - d_comp) == 1:
                user_damage = random.choice([15, 8, 8, 0])
                hp_comp = hp_comp - user_damage 
                if user_damage == 25:
                    print("Close Move Landed, Critical Hit,", user_damage, "Damage Done", hp_comp, "HP Remaining, End Turn")
                if user_damage == 10:
                    print("Close Move Landed,", user_damage, "Damage Done", hp_comp, "HP Remaining, End Turn")
                if user_damage == 0:
                    print("Close Move Missed,", user_damage, "Damage Done", hp_comp, "HP Remaining, End Turn")
                        
            if (d_comp - d_user) == 0:
                user_damage = random.choice([25, 10, 10, 10, 8, 0])
                hp_comp = hp_comp - user_damage 
                if user_damage == 25:
                    print("Very Close Move Landed, Critical Hit", user_damage, "Damage Done", hp_comp, "HP Remaining, End Turn")
                if user_damage == 10 or user_damage == 8:
                    print("Very Close Move Landed", user_damage, "Damage Done", hp_comp, "HP Remaining, End Turn")
                if user_damage == 0:
                    print("Very Close Move Missed", user_damage, "Damage Done", hp_comp, "HP Remaining, End Turn")
        Tru = True
        if hp_comp <= 0:
            return print("You Won")
#Computer Move
        if Tru == True:
            if d_comp - d_user >= 2:
                comp_move = random.choice(['forwards', 'dash', 'forwards', 'forwards'])
                if comp_move == 'forwards':
                    d_comp -= 1
                    print(d_comp, "Computer Distance", "forward, far")
                else:
                    d_comp -= 2
                    print(d_comp, "Computer Distance", "dash, far")
            if d_comp - d_user <= -2:
                comp_move = random.choice(['forwards', 'dash', 'forwards', 'forwards'])
                if comp_move == 'forwards':
                    d_comp += 1
                    print(d_comp, "Computer Distance", "forward, far")
                else:
                    d_comp += 2
                    print(d_comp, "Computer Distance", "dash, far")
            if d_user - d_comp == -2 or d_user - d_comp == 2:
                comp_move = random.choice(['slash', 'forwards', 'backwards', 'dash', 'slash', 'slash'])
                if comp_move == 'slash':
                    comp_damage = random.choice([10, 5, 0])
                    hp_user = hp_user - comp_damage 
                    if comp_damage == 25:
                        print("Computer Medium Move Landed, Critical Hit,", comp_damage, "Damage Done", hp_user, "HP Remaining, End Turn")
                    if comp_damage == 10:
                        print("Computer Medium Move Landed,", comp_damage, "Damage Done", hp_user, "HP Remaining, End Turn")
                    if comp_damage == 0:
                        print("Computer Medium Move Missed,", comp_damage, "Damage Done", hp_user, "HP Remaining, End Turn")
                if comp_move == 'forwards':
                    d_comp += 1
                    print(d_comp - d_user, "Computer distance forward, medium")
                if comp_move == 'backwards':
                    d_comp -= 1
                    print(d_comp - d_user, "Computer distance backwards, medium")
                if comp_move == 'dash':
                    comp_move = random.choice(['forwards', 'backwards'])
                    if comp_move == 'forwards':
                        d_comp += 2
                        print(d_comp - d_user, "Computer Distance dash_f, medium")
                    else:
                        d_comp -= 2
                        print(d_comp - d_user, "Computer distance dash_b, medium")
                        
            if (d_user - d_comp) == 1 or (d_user - d_comp) == -1:
                comp_move = random.choice(['slash', 'forwards', 'backwards', 'dash', 'slash', 'slash', 'slash', 'slash'])
                if comp_move == 'slash':
                    comp_damage = random.choice([15, 8, 8, 0])
                    hp_user = hp_user - comp_damage
                    if comp_damage == 25:
                        print("Computer Close Move Landed, Critical Hit,", comp_damage, "Damage Done", hp_user, "HP Remaining, End Turn")
                    if comp_damage == 10:
                        print("Computer Close Move Landed,", comp_damage, "Damage Done", hp_user, "HP Remaining, End Turn")
                    if comp_damage == 0:
                        print("Computer Close Move Missed,", comp_damage, "Damage Done", hp_user, "HP Remaining, End Turn")
                if comp_move == 'forwards':
                    d_comp += 1
                    print(d_comp - d_user, "Computer distance forwards, close")
                if comp_move == 'backwards':
                    d_comp -= 1
                    print(d_comp - d_user, "Computer distance forwards, close")
                if comp_move == 'dash':
                    comp_move = random.choice(['forwards', 'backwards'])
                    if comp_move == 'forwards':
                        d_comp += 2
                        print(d_comp - d_user, "Computer Distance dash_f, close")
                    else:
                        d_comp -= 2
                        print(d_comp - d_user, "Computer distance dash_b, close")
            
            if (d_user - d_comp) == 0:
                comp_move = random.choice(['slash', 'forwards', 'backwards', 'dash'])
                if comp_move == 'slash':
                    comp_damage = random.choice([25, 10, 10, 10, 8, 0])
                    hp_user = hp_user - comp_damage 
                    if comp_damage == 25:
                        print("Computer Very Close Move Landed, Critical Hit", comp_damage, "Damage Done", hp_user, "HP Remaining, End Turn")
                    if comp_damage == 10:
                        print("Computer Very Close Move Landed", comp_damage, "Damage Done", hp_user, "HP Remaining, End Turn")
                    if comp_damage == 0:
                        print("Computer Very Close Move Missed", comp_damage, "Damage Done", hp_user, "HP Remaining, End Turn")
                            
                if comp_move == 'forwards':
                    d_comp += 1
                    print(d_comp - d_user, "Computer distance forwards, very close")
                        
                if comp_move == 'backwards':
                    d_comp -= 1
                    print(d_comp - d_user, "Computer distance backwards, very close")
                        
                if comp_move == 'dash':
                    comp_move = random.choice(['forwards', 'backwards'])
                    if comp_move == 'forwards':
                        d_comp += 2
                        print(d_comp - d_user, "Computer Distance dash_f, very close")
                    else:
                        d_comp -= 2
                        print(d_comp - d_user, "Computer distance dash_b, very close")
      
        if hp_user <= 0:
            return print("You Lost")
                                
        print("[User Hp]", hp_user, "[User Dist]", d_user, "[Computer Hp]", hp_comp, "[Computer Dist]", d_comp)
        

game_play()
