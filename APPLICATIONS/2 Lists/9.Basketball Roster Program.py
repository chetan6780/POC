# Basketball Roster Program
print("**"*50)

# Welcome message.
print("Welcome To Basketball Roster Program.\n")

# creating lists
roster = []
team_pos = ['point guard', 'shooting guard',
            'small forward', 'power forward', 'center']
for pos in team_pos:
    roster.append(input(f"Who is your {pos} :",).title())

# Starting 5 players
print("\n\tYour starting 5 for the upcoming basketball season are...")
for i in range(0, 5):
    if i == 0 or i == 4:
        print("\t\t", team_pos[i]+":", "\t\t", roster[i])
    else:
        print("\t\t", team_pos[i]+":", "\t", roster[i])

# Information of injured player
rmvd_player = roster[2]
print("\nOh no,", rmvd_player, "is injured.")
print("\nYour roster only has 4 players.")
injured_player = roster.pop(2)
new_player = input(f"Who will take {rmvd_player}'s spot: ").title()
roster.insert(2, new_player)

# New Starting 5 players
print("\n\tYour starting 5 for the upcoming basketball season are...")
for i in range(0, 5):
    if i == 0 or i == 4:
        print("\t\t", team_pos[i]+":", "\t\t", roster[i])
    else:
        print("\t\t", team_pos[i]+":", "\t", roster[i])

# Wishing new player
print("\nGood luck", str(roster[2]), "you will do great!")
print("Your roster now has 5 players.")

# End of programm.
print("\nThank you for using this application!\n")
print("**"*50)
