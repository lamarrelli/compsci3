with open("rosalind_ctbl.txt") as infile:
    newick = infile.read().lower()

newnode = 0
nodes = []
leaves_nodes = {}
letters = "abcdefghijklmnopqrstuvwxyz_"
for i in range(len(newick)):
    if newick[i] == "(":
        nodes.append(newnode)
        newnode += 1
    if newick[i] == ")":
        nodes.pop()
    if newick[i] in letters and newick[i-1] not in letters:
        leafname = newick[i]
        j = i + 1
        while newick[j] in letters:
            leafname += newick[j]
            j += 1
        leaves_nodes[leafname] = list(nodes)

snodes = [leaves_nodes[x] for x in sorted(leaves_nodes)]

output = []
for i in range(len(snodes)):
    output += [[0] * len(snodes)]
    for j in range(len(snodes)):
        if i in snodes[j]:
            output[i][j] = 1
    if output[-1] == [0] * len(snodes):
        output.pop()
        break

output_nodupes = []
[output_nodupes.append(x) for x in output if x not in output_nodupes]
output = output_nodupes

for x in output:
    for y in x:
        if not x == [1] * len(snodes):
            print(y,end="")
    print()