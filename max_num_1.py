s="srisitarassss"
most_rep_ele=None
most_rep_times=0
for i in s:
    count=s.count(i)
    if count>most_rep_times:
        most_rep_times=count
        most_rep_ele=i
print(most_rep_ele,most_rep_times)