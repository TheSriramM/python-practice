"""Try the two pointer method
Order toddy's players in ascending order
Match up Toddy's sorted list with Opponents unsorted list

Start with i = 0 (first player in Toddy’s sorted list) and j = 0 (first player in rival’s lineup).

If Toddy[i] > Rival[j]:

This means Toddy’s player can win, so count a win.

Move both pointers forward (i++ and j++) to find the next best matchup.

If Toddy[i] ≤ Rival[j]:

This means Toddy’s player is too weak to win, so move only i forward to try the next strongest player.

Repeat this process until we reach the end of one of the lists."""

n = int(input())
toddy_team = list(map(int, input().split()))
opp_team = list(map(int, input().split()))
toddy_team.sort()
opp_team.sort()
win_count = 0
index = 0
for i in toddy_team:
    if index < n and i > opp_team[index]:
        win_count += 1
        index += 1
print(win_count)
