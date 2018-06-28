secret = input()
secret = list(secret)
guess = input()
guess = list(guess)
i=k=bulls=cows=0
for k in range(0,4):
    for i in range(0,4):
        if(guess[i] == secret[k]  and i == k):
            bulls+=1
            secret[k] = 'A'
        elif(guess[i] == secret[k] and guess[i] != secret[i]):
            cows+=1
            secret[k] = 'A'
print("{}A{}B".format(bulls,cows))
