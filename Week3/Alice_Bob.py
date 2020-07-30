# Solving compare the triplets problem from hackerrank
# Saaniah Blankenberg
# 20/05/2020
# mood: trying something new

# a =[5, 6, 7]
# b =[3, 6, 10]
print("Enter the scores for Alice and Bob")
a = list(map(int, input().split()))
b =list(map(int, input().split()))

alice_score = sum([(1 if a[i] > b[i] else 0) for i in range(3)])
bob_score = sum([(1 if a[i] < b[i] else 0) for i in range(3)])
print(alice_score, bob_score)
