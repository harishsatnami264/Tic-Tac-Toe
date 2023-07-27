
i = int(input("do you want to play 1 for yes    0 for no"))
while i !=0:

    print("its your turn")
    j = input("choose the symbol    X     or      O")
    if j == "X":
        k="O"
    else :
        k="X"
    in1 = " "
    in2 = " "
    in3 = " "
    in4 = " "
    in5 = " "
    in6 = " "
    in7 = " "
    in8 = " "
    in9 = " "
    li = [123, in1, in2, in3, in4, in5, in6, in7, in8, in9]
    def show():
        print(f"""
   |   |   |   |
   | {li[1]} | {li[2]} | {li[3]} |
    --- --- --- 
   |   |   |   |
   | {li[4]} | {li[5]} | {li[6]} |
    --- --- --- 
   | {li[7]} | {li[8]} | {li[9]} |
   |   |   |   |
        """)
    show()
    def prio():
        if li[1]==li[2] and li[1]==j:
            if li[3]!=k:
                li[3]=k
                return 1
        if li[1]==li[3] and li[1]==j:
            if li[2]!=k:
                li[2]=k
                return 1
        if li[3]==li[2] and li[3]==j:
            if li[1]!=k:
                li[1]=k
                return 1
        if li[4]==li[5] and li[4]==j:
            if li[6]!=k:
                li[6]=k
                return 1
        if li[4]==li[6] and li[4]==j:
            if li[5]!=k:
                li[5]=k
                return 1
        if li[5]==li[6] and li[5]==j:
            if li[4]!=k:
                li[4]=k
                return 1
        if li[7]==li[8] and li[7]==j:
            if li[9]!=k:
                li[9]=k
                return 1
        if li[7]==li[9] and li[7]==j:
            if li[8]!=k:
                li[8]=k
                return 1
        if li[9]==li[8] and li[9]==j:
            if li[7]!=k:
                li[7]=k
                return 1
        if li[1]==li[4] and li[1]==j:
            if li[7]!=k:
                li[7]=k
                return 1
        if li[1]==li[7] and li[1]==j:
            if li[4]!=k:
                li[4]=k
                return 1
        if li[7]==li[4] and li[7]==j:
            if li[1]!=k:
                li[1]=k
                return 1
        if li[2]==li[5] and li[2]==j:
            if li[8]!=k:
                li[8]=k
                return 1
        if li[2]==li[8] and li[2]==j:
            if li[5]!=k:
                li[5]=k
                return 1
        if li[8]==li[5] and li[8]==j:
            if li[2]!=k:
                li[2]=k
                return 1
        if li[3]==li[6] and li[3]==j:
            if li[9]!=k:
                li[9]=k
                return 1
        if li[3]==li[9] and li[3]==j:
            if li[6]!=k:
                li[6]=k
                return 1
        if li[9]==li[6] and li[9]==j:
            if li[3]!=k:
                li[3]=k
                return 1
        if li[1]==li[5] and li[1]==j:
            if li[9]!=k:
                li[9]=k
                return 1
        if li[1]==li[9] and li[1]==j:
            if li[5]!=k:
                li[5]=k
                return 1
        if li[9]==li[5] and li[9]==j:
            if li[1]!=k:
                li[1]=k
                return 1
        if li[3]==li[5] and li[3]==j:
            if li[7]!=k:
                li[7]=k
                return 1
        if li[3]==li[7] and li[3]==j:
            if li[5]!=k:
                li[5]=k
                return 1
        if li[7]==li[5] and li[7]==j:
            if li[3]!=k:
                li[3]=k
                return 1
    def prio2():
        if li[1]==li[2] and li[1]==k:
            if li[3]!=j:
                li[3]=k
                return 1
        if li[1]==li[3] and li[1]==k:
            if li[2]!=j:
                li[2]=k
                return 1
        if li[3]==li[2] and li[3]==k:
            if li[1]!=j:
                li[1]=k
                return 1
        if li[4]==li[5] and li[4]==k:
            if li[6]!=j:
                li[6]=k
                return 1
        if li[4]==li[6] and li[4]==k:
            if li[5]!=j:
                li[5]=k
                return 1
        if li[5]==li[6] and li[5]==k:
            if li[4]!=j:
                li[4]=k
                return 1
        if li[7]==li[8] and li[7]==k:
            if li[9]!=j:
                li[9]=k
                return 1
        if li[7]==li[9] and li[7]==k:
            if li[8]!=j:
                li[8]=k
                return 1
        if li[9]==li[8] and li[9]==k:
            if li[7]!=j:
                li[7]=k
                return 1
        if li[1]==li[4] and li[1]==k:
            if li[7]!=j:
                li[7]=k
                return 1
        if li[1]==li[7] and li[1]==k:
            if li[4]!=j:
                li[4]=k
                return 1
        if li[7]==li[4] and li[7]==k:
            if li[1]!=j:
                li[1]=k
                return 1
        if li[2]==li[5] and li[2]==k:
            if li[8]!=j:
                li[8]=k
                return 1
        if li[2]==li[8] and li[2]==k:
            if li[5]!=j:
                li[5]=k
                return 1
        if li[8]==li[5] and li[8]==k:
            if li[2]!=j:
                li[2]=k
                return 1
        if li[3]==li[6] and li[3]==k:
            if li[9]!=j:
                li[9]=k
                return 1
        if li[3]==li[9] and li[3]==k:
            if li[6]!=j:
                li[6]=k
                return 1
        if li[9]==li[6] and li[9]==k:
            if li[3]!=j:
                li[3]=k
                return 1
        if li[1]==li[5] and li[1]==k:
            if li[9]!=j:
                li[9]=k
                return 1
        if li[1]==li[9] and li[1]==k:
            if li[5]!=j:
                li[5]=k
                return 1
        if li[9]==li[5] and li[9]==k:
            if li[1]!=j:
                li[1]=k
                return 1
        if li[3]==li[5] and li[3]==k:
            if li[7]!=j:
                li[7]=k
                return 1
        if li[3]==li[7] and li[3]==k:
            if li[5]!=j:
                li[5]=k
                return 1
        if li[7]==li[5] and li[7]==k:
            if li[3]!=j:
                li[3]=k
                return 1


    def bing():
        if li[1]==li[2] and li[2]==li[3]:
            if li[1]==j:
                print("you win")
            else:
                print("you lose")
            return 1
        if li[4]==li[5] and li[5]==li[6]:
            if li[4]==j:
                print("you win")
            else:
                print("you lose")
            return 1
        if li[7]==li[8] and li[8]==li[9]:
            if li[7]==j:
                print("you win")
            else:
                print("you lose")
            return 1
        if li[1]==li[4] and li[4]==li[7]:
            if li[1]==j:
                print("you win")
            else:
                print("you lose")
            return 1
        if li[2]==li[5] and li[5]==li[8]:
            if li[2]==j:
                print("you win")
            else:
                print("you lose")
            return 1
        if li[3]==li[6] and li[6]==li[9]:
            if li[3]==j:
                print("you win")
            else:
                print("you lose")
            return 1
        if li[1]==li[5] and li[5]==li[9]:
            if li[1]==j:
                print("you win")
            else:
                print("you lose")
            return 1
        if li[3]==li[5] and li[5]==li[7]:
            if li[3]==j:
                print("you win")
            else:
                print("you lose")
            return 1



    def step():
        if inp == 1:
            if li[5]!=j and li[5]!=k:
                li[5]=k
            elif li[9]==j:
                li[2]=k
            elif li[3]!=j and li[3]!=k:
                li[3]=k
            elif li[7]!=j and li[7]!=k:
                li[7]=k
            elif li[2]!=j and li[2]!=k:
                li[2]=k
            elif li[4]!=j and li[4]!=k:
                li[4]=k
            elif li[6]!=j and li[6]!=k:
                li[6]=k
            elif li[8]!=j and li[8]!=k:
                li[8]=k
            elif li[9]!=j and li[9]!=k:
                li[9]=k
        elif inp == 3:
            if li[5]!=j and li[5]!=k:
                li[5]=k
            elif li[7]==j:
                li[6]=k
            elif li[1]!=j and li[1]!=k:
                li[1]=k
            elif li[9]!=j and li[9]!=k:
                li[9]=k
            elif li[2]!=j and li[2]!=k:
                li[2]=k
            elif li[6]!=j and li[6]!=k:
                li[6]=k
            elif li[4]!=j and li[4]!=k:
                li[4]=k
            elif li[8]!=j and li[8]!=k:
                li[8]=k
            elif li[7]!=j and li[7]!=k:
                li[7]=k
        elif inp == 7:
            if li[5]!=j and li[5]!=k:
                li[5]=k
            elif li[3]==j:
                li[4]=k
            elif li[1]!=j and li[1]!=k:
                li[1]=k
            elif li[9]!=j and li[9]!=k:
                li[9]=k
            elif li[8]!=j and li[8]!=k:
                li[8]=k
            elif li[4]!=j and li[4]!=k:
                li[4]=k
            elif li[6]!=j and li[6]!=k:
                li[6]=k
            elif li[2]!=j and li[2]!=k:
                li[2]=k
            elif li[3]!=j and li[3]!=k:
                li[3]=k
        elif inp == 9:
            if li[5]!=j and li[5]!=k:
                li[5]=k
            elif li[1]==j:
                li[8]=k
            elif li[3]!=j and li[3]!=k:
                li[3]=k
            elif li[7]!=j and li[7]!=k:
                li[7]=k
            elif li[6]!=j and li[6]!=k:
                li[6]=k
            elif li[8]!=j and li[8]!=k:
                li[8]=k
            elif li[4]!=j and li[4]!=k:
                li[4]=k
            elif li[2]!=j and li[2]!=k:
                li[2]=k
            elif li[1]!=j and li[1]!=k:
                li[1]=k
        elif inp == 2:
            if li[5]!=j and li[5]!=k:
                li[5]=k
            elif li[1]!=j and li[1]!=k:
                li[1]=k
            elif li[7]!=j and li[7]!=k:
                li[7]=k
            elif li[3]!=j and li[3]!=k:
                li[3]=k
            elif li[9]!=j and li[9]!=k:
                li[9]=k
        elif inp == 4:
            if li[5]!=j and li[5]!=k:
                li[5]=k
            elif li[7]!=j and li[7]!=k:
                li[7]=k
            elif li[9]!=j and li[9]!=k:
                li[9]=k
            elif li[1]!=j and li[1]!=k:
                li[1]=k
            elif li[3]!=j and li[3]!=k:
                li[3]=k
        elif inp == 6:
            if li[5]!=j and li[5]!=k:
                li[5]=k
            elif li[3]!=j and li[3]!=k:
                li[3]=k
            elif li[1]!=j and li[1]!=k:
                li[1]=k
            elif li[7]!=j and li[7]!=k:
                li[7]=k
            elif li[9]!=j and li[9]!=k:
                li[9]=k
        elif inp == 8:
            if li[5]!=j and li[5]!=k:
                li[5]=k
            elif li[9]!=j and li[9]!=k:
                li[9]=k
            elif li[3]!=j and li[3]!=k:
                li[3]=k
            elif li[7]!=j and li[7]!=k:
                li[7]=k
            elif li[1]!=j and li[1]!=k:
                li[1]=k
        elif inp == 5:
            if li[1]!=j and li[1]!=k:
                li[1]=k
            elif li[3]!=j and li[3]!=k:
                li[3]=k
            elif li[7]!=j and li[7]!=k:
                li[7]=k
            elif li[9]!=j and li[9]!=k:
                li[9]=k
            elif li[2]!=j and li[2]!=k:
                li[2]=k
            elif li[4]!=j and li[4]!=k:
                li[4]=k
            elif li[6]!=j and li[6]!=k:
                li[6]=k
            elif li[8]!=j and li[8]!=k:
                li[8]=k
    h = 1
    while h < 6:
        inp = int(input("enter your choice 1-9"))
        if li[inp]!=j and li[inp]!=k:
            li[inp]=j
        else:
            inp = int(input("please do not select the used number"))
        show()
        m = prio2()
        if m ==1:
            print("game over")
            break
        elif prio()==1:
            show()
            h = h + 1
            continue
        else:
            step()
        show()
        h = h + 1
    n = bing()
    show()
    if n!=1:
        print("match draw, well played")

    i = int(input("do you want to play 1 for yes    0 for no"))








