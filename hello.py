# relationship_status
def relationship(): 
    name=input("\nenter your name:")
    a="married"
    b="mingle"
    c="single"
    d="i am not interested in love life"
    e="single but i have a crush,one side love"
    while True:
        relationship_status=input("\nchoose your relationship status:\n(a)merried\n(b)mingle\n(c)single\n(d)i am not intrested in love life\n(e)single but i have a crush,one side love\nyour ans=",)
        if(relationship_status=="a"):
            print(name,"You are married. Wishing you a happy life!")
            break
        elif(relationship_status=="b"):
            print(name,"Enjoying your love life 😄")
            break
        elif(relationship_status=="c"):
            print(name,"Single life is peaceful and focused!")
            break
        elif(relationship_status=="d"):
            print(name,"Full focus on goals. Respect!")
            break
        elif(relationship_status=="e"):
            print(name,"Wake up to reality.\nNothing ever goes as planned in this accursed world.\nThe longer you live, the more you realize that only pain, suffering, and futility exist")
            break
        else:
            print(name,"❌ Invalid choice! Please select only (a, b, c, d).")
relationship()







