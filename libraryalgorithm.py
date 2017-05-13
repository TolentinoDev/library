# Ryan Tolentino
#Library Algorithm


#Convert .xls to .csv 
#Seperate it by a "|"
#Ex: Title|Subject|Desc|Url

#!/usr/bin/python

#if description contrains[x] terms:
	#insert(y) 
with open('output1.csv','a') as e:
	with open('db.csv','r')as f:
		for line in f:
			tokens = line.split("|")
			description = tokens[2]
			subject = tokens[1]
			if len(subject) == 0:
                                with open ('subject.csv','r')as g:
                                        for line in g:
                                                if line in description:
                                                        new=tokens[0]+"1"+line+tokens[2]
                                                        e.write(new+"\n")
                                                else:
                                                        e.write("|".join(tokens))

