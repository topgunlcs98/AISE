import re
import numpy
from pprint import pprint

def levenshteinDistanceDP(token1, token2):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    printDistances(distances, len(token1), len(token2))
    return 0

def printDistances(distances, token1Length, token2Length):
    for t1 in range(token1Length + 1):
        for t2 in range(token2Length + 1):
            print(int(distances[t1][t2]), end=" ")
        print()

def printOps(distances, token1Length, token2Length):
    for t1 in range(token1Length + 1):
        for t2 in range(token2Length + 1):
            print(distances[t1][t2], end=" ")
        print()


def levenshteinDistanceDP(token1, token2):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))
    ops_matrix = [['' for i in range(len(token2)+1)] for j in range(len(token1)+1)]

    for t1 in range(len(token1)+1):
        distances[t1][0] = t1
        if t1 >= 1:
            ops_matrix[t1][0] = ops_matrix[t1-1][0] + "<del>"

    for t2 in range(len(token2)+1):
        distances[0][t2] = t2
        if t2 >=1 :
            ops_matrix[0][t2] = ops_matrix[0][t2-1] + "<ins>{}</ins>".format(token2[t2-1])

    a = 0
    b = 0
    c = 0

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1-1] == token2[t2-1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
                ops_matrix[t1][t2] = ops_matrix[t1-1][t2-1] + "<kep>"
            else:

                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]

                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                    ops_matrix[t1][t2] = (ops_matrix[t1][t2-1] + "<ins>{}</ins>".format(token2[t2-1]))
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                    ops_matrix[t1][t2] = (ops_matrix[t1-1][t2] + "<del>")
                else:
                    distances[t1][t2] = c + 1
                    ops_matrix[t1][t2] = (ops_matrix[t1-1][t2-1] + "<rep>{}</rep>".format(token2[t2-1]))

    # printDistances(distances, len(token1), len(token2))
    # print(ops_matrix[len(token1)][len(token2)])
    # pprint(ops_matrix)
    # printOps(ops_matrix, len(token1), len(token2))
    # return distances[len(token1)][len(token2)]
    return ops_matrix[len(token1)][len(token2)]


def gene_test():

    c1 = open("test_prevs.txt", "r").read().rstrip("\n").split(" ")
    c2 = open("test_next.txt", "r").read().rstrip("\n").split(" ")
    print(c1)
    # print(c2)
# c1_esp = re.escape(c1)
# print(c1_esp)
# print()
# c1_de_escp = bytes(c1_esp, "utf-8").decode("unicode_escape")
# print(c1_de_escp)
# print(c1)
    print(levenshteinDistanceDP(c1, c2))


def gene_tokens():
    file_size = ["medium", "small"]
    file_type = ["train"]

    for f_size in file_size:
        for f_type in file_type:

            f1_path = "./ProjectGroupData/{}/{}/data.prev_full_code".format(f_size, f_type)
            f2_path = "./ProjectGroupData/{}/{}/data.next_full_code".format(f_size, f_type)

            f1_lines = open(f1_path).read().splitlines()
            f2_lines = open(f2_path).read().splitlines()
            file_l = len(f1_lines)
            final_token_seqs = []
            for i in range(file_l):
                f1_tokens = f1_lines[i].split(" ")
                f2_tokens = f2_lines[i].split(" ")
                final_token_seqs.append(levenshteinDistanceDP(f1_tokens, f2_tokens))

            gene_path = "./GeneOps/{}/{}.txt".format(f_size, f_type)
            with open(gene_path, "w") as f:
                for i in final_token_seqs:
                    f.write(i + "\n")


if __name__ == "__main__":
    gene_tokens()
    # gene_test()
    # print(levenshteinDistanceDP("acd", "acd"))
