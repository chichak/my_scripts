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

    
#### Here i wanted to write files in different locations based on the data values ####
    
# Here i create a labeled slice of the data to write it into files
# I created a new slice and labeled entries "a" and "b"
labeled_df = df.iloc[0:10,]
labeled_df["labels"]=0
labels_list = labeled_df["labels"].values.tolist()
for i in range(len(labels_list)):
    if i%2 == 0:
        labeled_df.loc[i,"labels"] = "a"
    else:
        labeled_df.loc[i,"labels"] = "b"

# Then if label == "a" i store the element in folder1 else in folder2

# This to write each dataframe element in a separate file

indexlist = labeled_df.index.values.tolist()
titlelist = labeled_df['Title'].values.tolist()
abstractlist = labeled_df['Abstract'].values.tolist()
labelslist = labeled_df['labels'].values.tolist()


for elem in indexlist:
    #print(labelslist[elem])
    if labelslist[elem] == "a":
        i = indexlist.index(elem)
        #print(i)
        file = open("/home/wisha/Desktop/scopus/lupus/text_%d.txt" %(i), "+w")
        file.write("%s\n" %(titlelist[i]))
        file = open("/home/wisha/Desktop/scopus/lupus/text_%d.txt" %(i), "+a")
        file.write(abstractlist[i])
        file.close()
    else:
        i = indexlist.index(elem)
        file = open("/home/wisha/Desktop/scopus/other/text_%d.txt" %(i), "+w")
        file.write("%s\n" %(titlelist[i]))
        file = open("/home/wisha/Desktop/scopus/other/text_%d.txt" %(i), "+a")
        file.write(abstractlist[i])
        file.close()


