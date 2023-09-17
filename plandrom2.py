def plandrom(name):
    rev=''
    for i in range(len(name)-1,-1,-1):
        rev=rev+name[i]

        
    if name == rev:
        print("plandrom")
    else:
         print("not plandrom")
        

names=['anirudh','annu','sts']
for i in names:
    plandrom(i)
 
   

    
