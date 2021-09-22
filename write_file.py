# I had a dataframe df and i wanted to write its elements into txt files (in order to perform some nlp tasks)


# This to write each dataframe element in a separate file

# Put columns into lists to store them later in files
titlelist = df['Title'].values.tolist()
abstractlist = df['Abstract'].values.tolist()

# Here, it depends on your loop: whether a range or over len(list)
for i in range(3):
    #i = shortlist.index(elem)
    # to write/create file
    file = open("/home/wisha/Desktop/scopus/other/text_%d.txt" %(i), "+w")
    file.write("%s\n" %(titlelist[i]))
    # To append 
    file = open("/home/wisha/Desktop/scopus/other/text_%d.txt" %(i), "+a")
    file.write(abstractlist[i])
    file.close()
