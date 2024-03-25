#Test contains 5 bits 
# if 1 options are correct in a bit then for each correct option you secure 0.5 marks
# if 2 options are correct in a bit then for each correct option you secure 0.5 marks
# if 3 options are correct in a bit then for each correct option you secure 0.33 marks
# if 4 options are correct in a bit then for each correct option you secure 0.25 marks
# and for each wrong question -10 marks are removed
# student should enter the options in abcd only


   
def Eval():
    def NoofAnswers(a):
        count=0
        for i in a:
            if i == 1:
                count=count+1
        return count
    def option(x,y,z,i):
        if x =="a":
            ans1=[1,0,0,0]
        elif x =="b":
            ans1=[0,1,0,0]
        elif x =="c":
            ans1=[0,0,1,0]
        elif x =="d":
            ans1=[0,0,0,1]

        if y =="a":
            ans2=[1,0,0,0]
        elif y =="b":
            ans2=[0,1,0,0]
        elif y =="c":
            ans2=[0,0,1,0]
        elif y =="d":
            ans2=[0,0,0,1]

        if z =="a":
            ans3=[1,0,0,0]
        elif z =="b":
            ans3=[0,1,0,0]
        elif z =="c":
            ans3=[0,0,1,0]
        elif z =="d":
            ans3=[0,0,0,1]
        else:
            ans3=[0,0,0,0]
        ans=[]
        for i in range(len(ans1)):
            z=ans1[i]+ans2[i]+ans3[i]
            ans.append(z)
        return ans
    
    Answer       =[[1,1,1,1],[1,0,0,0],[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,0,0],[1,1,1,0],[1,1,1,1]]
    StudentAnswer=[]
    print("Enter the options in Alpabhetical Order(abcd)")
    for i in range(len(Answer)):
        print(i+1,". Enter the Answer :")
        n=2
        while(n>1):
            er=input()
            if er in ["a","b","c","d","ua","ab","ac","ad","bc","bd","cd","abc","abd","acd","bcd","abcd"]:
                StudentAnswer.append(er)
                n=n-1
            else:
                print("Please ReEnter the options in Alpabhetical Order(abcd)")
    print(StudentAnswer)
    for i in range(len(StudentAnswer)):
        if StudentAnswer[i] in ["UA","ua"]:
            StudentAnswer[i]=[0,0,0,0]
        elif len(StudentAnswer[i])==1:
            if StudentAnswer[i]=="a":
                StudentAnswer[i]=[1,0,0,0]
            if StudentAnswer[i]=="b":
                StudentAnswer[i]=[0,1,0,0]
            if StudentAnswer[i]=="c":
                StudentAnswer[i]=[0,0,1,0]
            if StudentAnswer[i]=="d":
                StudentAnswer[i]=[0,0,0,1]
        elif len(StudentAnswer[i])==2:
            str1=StudentAnswer[i][:1]
            str2=StudentAnswer[i][1:]
            str3="z"
            StudentAnswer[i]=option(str1,str2,str3,i)
        elif len(StudentAnswer[i])==3:
            str1=StudentAnswer[i][:1]
            str2=StudentAnswer[i][1:2]
            str3=StudentAnswer[i][2:]
            StudentAnswer[i]=option(str1,str2,str3,i)
        elif len(StudentAnswer[i])==4:
            StudentAnswer[i]=[1,1,1,1]
    print(StudentAnswer)
    Total=160
    Score=0
    for i in range(len(Answer)):
        Bitscore=0
        b=NoofAnswers(Answer[i])
        count0=0
        Partially=0
        for j in range(len(Answer[i])):
            if Answer[i][j]==StudentAnswer[i][j]:
                if StudentAnswer[i][j]==1 and Partially==0:
                    if b==1:
                        Bitscore=Bitscore+20
                    elif b==2:
                        Bitscore=Bitscore+10
                    elif b==3:
                        Bitscore=Bitscore+6.66
                        if Bitscore==19.98:
                            Bitscore=20
                    elif b==4:
                        Bitscore=Bitscore+5
                else:
                    count0=count0+1
            else:
                if  StudentAnswer[i][j]==0:
                    count0=count0+1
                elif StudentAnswer[i][j]==1:
                    Bitscore=0
                    Partially=1                 
        if Bitscore==20:
            Score=Score+Bitscore
            print(i+1,"Correct Answer           :",Bitscore)
        elif count0==4:
            Score=Score+Bitscore
            print(i+1,"Question Unattempted     :",Bitscore)
        elif Bitscore==0 and count0<4:
            Bitscore=Bitscore-10
            Score=Score+Bitscore
            print(i+1,"Wrong Answer             :",Bitscore)
        elif Bitscore<20 and Bitscore>0:
             Score=Score+Bitscore
             print(i+1,"Partially Correct        :",Bitscore)
    print("Marks                      :",Score)
    print("Percentage                 :",(Score/Total)*100,"%")
    import ram
    ram.Grade(int((Score/Total)*100))
Eval()
