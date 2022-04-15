import re

file_size = ["medium", "small"]
file_type = ["eval", "test", "train"]

def buggy_before():
    for f_size in file_size:
        for f_type in file_type:
            f1_path = "./ProjectGroupData/{}/{}/data.buggy_only".format(f_size, f_type)
            f2_path = "./ProjectGroupData/{}/{}/data.prev_full_code".format(f_size, f_type)
            # f1 = open(f1_path).readlines()
            # f2 = open(f2_path).readlines()
            f1 = open(f1_path).read().splitlines()
            f2 = open(f2_path).read().splitlines()
            file_l = len(f1)
            final_res_li = []
            for i in range(file_l):
                bug = f1[i]
                code = f2[i]
                search_kv = r'.+?(?={})'.format(re.escape(bug))
                re_res = re.search(search_kv, code)
                if re_res:
                    final_res_li.append(re_res.group(0))
                else:
                    final_res_li.append('')
            print("finish " + f_type + ", " + f_size)
            gene_path = "./BuggyBefore/{}/{}.txt".format(f_size, f_type)
            with open(gene_path, "w") as f:
                for i in final_res_li:
                    f.write(i + "\n")

def buggy_after():
    for f_size in file_size:
        for f_type in file_type:
            # if not (f_size=="small" and f_type=="eval"):
            #     continue
            f1_path = "./ProjectGroupData/{}/{}/data.buggy_only".format(f_size, f_type)
            f2_path = "./ProjectGroupData/{}/{}/data.prev_full_code".format(f_size, f_type)
            f1 = open(f1_path).read().splitlines()
            f2 = open(f2_path).read().splitlines()
            file_l = len(f1)
            final_res_li = []
            for i in range(file_l):
                bug = f1[i]
                code = f2[i]
                search_kv = r'(?<={}).*'.format(re.escape(bug))
                re_res = re.search(search_kv, code)
                if re_res:
                    final_res_li.append(re_res.group(0))
                else:
                    final_res_li.append('')
            gene_path = "./BuggyAfter/{}/{}.txt".format(f_size, f_type)
            # print(final_res_li)
            with open(gene_path, "w") as f:
                for i in final_res_li:
                    f.write(i + "\n")

if __name__ == "__main__":
    buggy_before()
    # buggy_after()
