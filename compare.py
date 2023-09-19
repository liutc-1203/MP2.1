from scipy import stats
with open('bm25.avg_p.txt','r') as f:
    a= f.readlines()
# a.strip("\n")
bm25_list = []
for txt in a:
    bm25_list.append(float(txt.strip("\n")))
f.close()

with open('inl2.avg_p.txt','r') as f:
    a= f.readlines()
# a.strip("\n")
inl2_list = []
for txt in a:
    inl2_list.append(float(txt.strip("\n")))
# print(inl2_list)

result = stats.ttest_rel(bm25_list,inl2_list)
with open("significance.txt", "w") as f: 
    f.write(str(result.pvalue))