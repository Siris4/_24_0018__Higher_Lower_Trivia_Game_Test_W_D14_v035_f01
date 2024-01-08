import random

from _24_0018__D14_v01_f01_Higher_Lower_Trivia_Game_logo_W import logo, vs
from _24_0018__D14_v00_f01_Higher_Lower_Trivia_Game_gamedata_W import data

print(logo)



# def profile_A():
# global random_profile_index_number_picked_A
# random_profile_index_number_picked_A = random.randrange(0, 50)
# profile_a = data[random_profile_index_number_picked_A]
# print(f'The number was {random_profile_index_number_picked_A}')
# print(f"The profile number that was chosen is index #: {random_profile_index_number_picked_A}")
# print(profile_A)
# profile_b = ""

def game_on():
    global counter, profile_A, profile_B
    score = 0
    previous_index_holder = 0
    counter = 0
    previous_index_holder = 0

    while True:
        if counter >= 1:
            profile_A = profile_B
            profile_B = data[random_profile_index_number_picked_A]
        else:
            random_profile_index_number_picked_A = random.randrange(0, 50)
            profile_A = data[random_profile_index_number_picked_A]
            print(f"The profile number that was chosen is index #: {random_profile_index_number_picked_A}")
            # print(profile_A)
            profile_B = ""

        profile_name_A = profile_A.get('name')
        print(profile_name_A)
        hidden_profile_A_follower_count = int(profile_A.get('follower_count'))
        counter += 1
        # print(f'They have {hidden_profile_A_follower_count} million subscribers')

        print(vs)

        #Profile B: ##############################################################################################3
        global random_profile_index_number_picked_B
        random_profile_index_number_picked_B = random.randrange(0, 50)
        if random_profile_index_number_picked_B != random_profile_index_number_picked_A:
            profile_B = data[random_profile_index_number_picked_B]
        else:
            random_profile_index_number_picked_B = random.randrange(0, 50)
        profile_B = data[random_profile_index_number_picked_B]
        print(f"The profile number that was chosen is index #: {random_profile_index_number_picked_B}")
        previous_index_holder += random_profile_index_number_picked_B
        profile_name_B = profile_B.get('name')
        print(profile_name_B)
        hidden_profile_B_follower_count = int(profile_B.get('follower_count'))
        # print(f'They have {hidden_profile_B_follower_count} million subscribers')

        a_or_b_profile_user_pick = input(f"Do you think that A or B has more followers? (A or B): ").upper()
        if hidden_profile_A_follower_count > hidden_profile_B_follower_count and a_or_b_profile_user_pick == "A":
            print(f"Yay!! You got it right! {profile_name_A} has {hidden_profile_A_follower_count} million subscribers.")
            print(f"You got {counter} right in a row!")
            # return random_profile_index_number_picked_B

        elif hidden_profile_A_follower_count < hidden_profile_B_follower_count and a_or_b_profile_user_pick == "B":
            print(f"Yay!! You got it right! {profile_name_B} has {hidden_profile_A_follower_count} million subscribers.")
            print(f"You got {counter} right in a row!")
        else:
            print(f"Sorry, but you failed. {profile_name_A} has {hidden_profile_A_follower_count} million subscribers, and {profile_name_B} has {hidden_profile_B_follower_count} million subscribers.")
            counter = 0
            game_on = False

        continue_next_part = input("Shall we continue? (Y or N): ").upper()
        if continue_next_part == "Y":
            game_on = True
        else:
            print("OK then, good day to you too sir")
            return False




game_on()
play_again_option = input("Do you want to play again? (Y or N): ").upper()
if play_again_option == "Y":
    game_on()