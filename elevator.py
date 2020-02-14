
n=4
n+=1

C=8
sum_path=[]      #συνολο λυσεων του προβληματος

logic=False
while not logic:
    s=0
    minimum=n**n
    E=3
    p=[0,4,5,6,7]

    state=4
    laststate=state
    path=[]

    ma=[i for i in range(1,n) if True]       #μετωπο αναζητησης
    ma_index=[state]
    
    print("................")
    while p[0]!=sum([p[i] for i in range(n) if True])+E:

        path.append(state)
        
        k=min(C-E,p[state]) # αριθμος ατομων που μπορει να παρει το ανσανσερ απο οροφο
        E+=k            #για καθε οροφο (state) γεμισε οσο μπορει 
        p[state]-=k     #διαγραφη ατομων απο τον οροφο που μπικαν στο ανσανσερ

        
        
        if p[state]==0:  #διαγραφη οροφου απο το μετοπο αναζητησης αν ο αριθμος των ατομων ειναι 0
            for i in range(len(ma)):
                if ma[i]==state:
                    del ma[i]
                    break
                
        s+=state-laststate          #το διαστημα που κανει το ανσανσερ
        
        if E==C or len(ma)==0:        #οταν το ανσανσερ ειναι γεματο πηγενε στο ισογειο και αδιασε
            state=0
            p[0]+=E
            E=0
            path.append(state)

            
        laststate=state         #τελευταιος οροφος 

        
        ########################
        d=[]
        index_path=[] #λιστα για της ομοιες διαδρομες με την παρουσα
        ma1=[ma[i] for i in range(len(ma)) if True] #πιθανες διαδρομες
        if len(sum_path)!=0: #αν υπαρχει τουλαχιστον μια λυση διαδρομης
            d=sum_path
            for z in range(len(ma_index)): #για την μεχρι τωρα διαδρομη
                for i in d: # αν το path συμπιπτει τοτε append σε λιστα την διαδρομη
                    if i[1][z]==ma_index[z]: index_path.append(i)
                d=index_path
                index_path=[]
        for i in d: #το d προκυπτει η λιστα με της ομοιες μεχρι τωρα διαδρομες
            #print("i[1] in d",i[1])
            if len(i[1])>len(ma_index):
                k=[len(ma1)-i-1 for i in range(len(ma1)) if True]
                
                for j in k: # αποριπτω τις ομοιες λυσεις και ετσι επιλεγω το επομενο βημα διαφορετικο απο τις προηγουμενες λυσεις
                    if i[1][len(ma_index)] == ma1[j]:
                        #print("j in ma1",ma1[j])
                        del ma1[j]
                        #print("ma1",ma1) 

        if len(ma1)!=0: 
            state=ma1[0]            #επιλογεας καταστασεων (state)            
        elif len(ma)!=0:
            state=ma[0]
        else:
            state=0
        #######################

        #for i in ma: state=i
        

        
        ma_index.append(state)
        
        #print([p[i] for i in range(n) if True],ma,"state:",state," E:",E)


    sum_path.append([path,ma_index])

    if len(sum_path)>1:
        for i in range(len(sum_path)):
            for j in range(i+1,len(sum_path)):
                if sum_path[i][1]==sum_path[j][1]:
                    #print("i",'j',sum_path[i][1],sum_path[j][1])
                    logic=True
            
    
    

    if s<minimum:
        minimum=s
        sum_path_min=[path,ma_index]
    #print("sum_path: ",sum_path)
print(sum_path_min[0])
print("END")



