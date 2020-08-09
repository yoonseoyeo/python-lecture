def search_name(stu_no,stu_name,find_num):
    n = len(stu_no)
    name = '?'
    for i in range(0,n):
        if find_num == stu_no[i]:
            return stu_name[i]
    return"?"
stu_no = [39,14,67,105]
stu_name = ["Justin","John","Mike","summer"]


print (search_name(stu_no,stu_name,39))
print(search_name(stu_no,stu_name,14))
print(search_name(stu_no,stu_name,105))
print(search_name(stu_no,stu_name,110))