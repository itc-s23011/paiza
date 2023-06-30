def count_votes(votes):
    yes = votes.count("yes")
    no = votes.count("no")

    if yes > no:
        return "yes"
    else:
        return "no"


votes = []
for i in range(5):
    vote = input().strip()
    votes.append(vote)


result = count_votes(votes)
print(result)
