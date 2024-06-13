bannned_user=["akshay","deekshay"]
prompt="\n add playet to yout team :-"
prompt+="\n Enter quit when you are done :-"

players=[]
while True:
    player=input(prompt)
    if player=="quit":
        break
    elif player in bannned_user:
        print(player+"is banned")
        continue
    else:
        players.append(player)
print("\n your team")
for player in players:
    print(player)