player_count = int(input())
toddy_team = input().split()
opp_team = input().split()
score = 0
toddy_team.sort()
toddy_team.reverse()
for player in toddy_team:
    player = int(player)
    opp_index = toddy_team.index(str(player))
    if player > int(opp_team[opp_index]):
        score += 1
print(score)

