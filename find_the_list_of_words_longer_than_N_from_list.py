str = "the quick brown world"
a=str.split(" ")
b=[]
n= 3
for i in a:

    if (len(i)> n) :

        b.append(i)

print("list of words : ",b)