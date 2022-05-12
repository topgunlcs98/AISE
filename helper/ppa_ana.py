f1 = open("./data/small/dev.gold").readlines()
f2 = open("./data/small/dev.output").readlines()

line_len = len(f1)
same_pair = 0
for i in range(line_len):
    if f1[i] == f2[i]:
        same_pair += 1

print("Same pair num: " + str(same_pair))
print("PPA: ", str(same_pair/line_len))
