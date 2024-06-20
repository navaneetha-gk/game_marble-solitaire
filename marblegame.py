import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import sys
points=0

import mysql.connector as m
try:
    

    status=""
    o={   -2:{-1:"X",0:"X",1:"X",2:"X",3:"X",4:"X",5:"X",6:"X",7:"X",8:"X",9:"X"},
          -1:{-1:"X",0:"X",1:"X",2:"X",3:"X",4:"X",5:"X",6:"X",7:"X",8:"X",9:"X"},
           0:{-1:"X",0:"X",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"X",9:"X"},
           1:{-1:"X",0:"X",1:"X",2:"X",  3:"O",4:"O",5:"O",  6:"X",7:"X",8:"X",9:"X"},
           2:{-1:"X",0:"X",1:"X",2:"X",  3:"O",4:"O",5:"O",  6:"X",7:"X",8:"X",9:"X"},
           3:{-1:"X",0:"X",  1:"O",2:"O",3:"O",4:"O",5:"O",6:"O",7:"O",  8:"X",9:"X"},
           4:{-1:"X",0:"X",  1:"O",2:"O",3:"O",4:" ",5:"O",6:"O",7:"O",  8:"X",9:"X"},
           5:{-1:"X",0:"X",  1:"O",2:"O",3:"O",4:"O",5:"O",6:"O",7:"O",  8:"X",9:"X"},
           6:{-1:"X",0:"X",1:"X",2:"X",  3:"O",4:"O",5:"O",  6:"X",7:"X",8:"X",9:"X"},
           7:{-1:"X",0:"X",1:"X",2:"X",  3:"O",4:"O",5:"O",  6:"X",7:"X",8:"X",9:"X"},
           8:{-1:"X",0:"X",1:"X",2:"X",3:"X",4:"X",5:"X",6:"X",7:"X",8:"X",9:"X"},
           9:{-1:"X",0:"X",1:"X",2:"X",3:"X",4:"X",5:"X",6:"X",7:"X",8:"X",9:"X"}
       }


    def reset():
        global o
        global flag1
        flag1=0
        o={   -2:{-1:"X",0:"X",1:"X",2:"X",3:"X",4:"X",5:"X",6:"X",7:"X",8:"X",9:"X"},
          -1:{-1:"X",0:"X",1:"X",2:"X",3:"X",4:"X",5:"X",6:"X",7:"X",8:"X",9:"X"},
           0:{-1:"X",0:"X",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"X",9:"X"},
           1:{-1:"X",0:"X",1:"X",2:"X",  3:"O",4:"O",5:"O",  6:"X",7:"X",8:"X",9:"X"},
           2:{-1:"X",0:"X",1:"X",2:"X",  3:"O",4:"O",5:"O",  6:"X",7:"X",8:"X",9:"X"},
           3:{-1:"X",0:"X",  1:"O",2:"O",3:"O",4:"O",5:"O",6:"O",7:"O",  8:"X",9:"X"},
           4:{-1:"X",0:"X",  1:"O",2:"O",3:"O",4:" ",5:"O",6:"O",7:"O",  8:"X",9:"X"},
           5:{-1:"X",0:"X",  1:"O",2:"O",3:"O",4:"O",5:"O",6:"O",7:"O",  8:"X",9:"X"},
           6:{-1:"X",0:"X",1:"X",2:"X",  3:"O",4:"O",5:"O",  6:"X",7:"X",8:"X",9:"X"},
           7:{-1:"X",0:"X",1:"X",2:"X",  3:"O",4:"O",5:"O",  6:"X",7:"X",8:"X",9:"X"},
           8:{-1:"X",0:"X",1:"X",2:"X",3:"X",4:"X",5:"X",6:"X",7:"X",8:"X",9:"X"},
           9:{-1:"X",0:"X",1:"X",2:"X",3:"X",4:"X",5:"X",6:"X",7:"X",8:"X",9:"X"}
              }
        global root
        #root.destroy()
        status=""
        game(o)



    def win(l):
        #If other moves are not there
        if l[4][4]=="O":
            for y in range(1,8):
                for x in range(1,8):
                    if y!=4 or x!=4:
                        if l[y][x]=="O":
                            return(0)   
            return(1)


    def alter(l):
        m=0
        global points
        for i in range(1,8):
            a=list(l[i].values())
            m=m+a.count("O")
        #print(m)
        if m==1:
            status="Brilliant Game! you have only 1 marble left. Next time try to bring it to the centre\nYou gained 75 points"
            points=75
        elif m==2:
            status="Amazing! You have only 2 marbles left. Aim for one next time.\nYou gained 50 points"
            points=50
        elif m>=3:
            status="Good try! You have "+str(m)+" marbles left. Better luck next time.\nYou gained 10 points"
            points=10
        return (status)



    def validstarts(x,y):
        if o[y][x]==" " or o[y][x]=="X":
            return False
        validity_start=0
        if o[y][x+1] =='O':
            if o[y][x+2]==' ':
                validity_start=1
        if o[y][x-1] =='O':
            if o[y][x-2]==' ':
                validity_start=1
        if o[y+1][x] =='O':
            if o[y+2][x]==' ':
                validity_start=1
        if o[y-1][x] =='O':
            if o[y-2][x]==' ':
                validity_start=1
        
            
        if validity_start==1:
            return True
        else:
            return False



    def validfinals(sx_,sy_,fx_,fy_):
        if sx_==fx_:
            if sy_==fy_ or abs(sy_-fy_)!=2 or o[(sy_+fy_)/2][sx_]!="O" or o[fy_][fx_]!=" " or (fx_,fy_)in t:
            #invalid conditions
            #starting and end point is same OR marble move is long OR No marble between start and end point OR end point is not vacant OR end point is out of the cross
                
                return False
            else:
                
                return True
                
        elif sy_==fy_:
            #shifting along x axis
            if sx_==fx_ or abs(sx_-fx_)!=2 or o[sy_][(sx_+fx_)/2]!="O" or o[fy_][fx_]!=" " or (fx_,fy_)in t:
                #invalid conditions
                #starting and end point is same OR marble move is long OR No marble between start and end point OR end point is not vacant OR end point is out of the cross
                
                return False
            else:
                return True
        else:
            return False



    def moves(l):
        moves_present=0
        for y in range(1,8):
            for x in range(1,8):
                if l[y][x]=="O":
                    #if ((l.get(y,)).get(x+1)=="O" and (l.get(y)).get(x+2)==" ") or ((l.get(y)).get(x-1)=="O" and (l.get(y)).get(x-2)==" ") or ((l.get(y+1)).get(x)=="O" and (l.get(y+2)).get(x)==" ") or ((l.get(y-1)).get(x)=="O" and (l.get(y-2)).get(x)==" ") :
                    if validstarts(x,y):
                        #if moves are there
                        moves_present=1
        if moves_present==1:
            return True
        #root=tk.Tk()
        #if moves are not there
        if win(l)==1:
            global points
            root=tk.Tk()
            points=100
            label1=tk.Label(root,text="You won!! Congratulations \n You gained 100 points")
            
        else:
            
            master.destroy()
            root=tk.Tk()
            label1=tk.Label(root,text=alter(l))
        label1.grid(column=1,row=1)
        label2=tk.Label(root,text='Do you wish to play once more?')
        button2=tk.Button(root,text="Yes",command=lambda: [reset(),root.destroy()])
        button3=tk.Button(root,text="Exit",command=lambda: root.destroy())
        label2.grid(column=1,row=2)
        button2.grid(column=1,row=3)
        button3.grid(column=1,row=4)
        
     
    startscurrent=()


    def which_button(button_press):
        
        global flag1
        global startscurrent
          
        x1=button_press[0]
        y1=button_press[1]
        if flag1==0:#implies start button is clicked
            
            if validstarts(x1,y1):
                colr='blue'
                startscurrent=(x1,y1)
                flag1=1
            else:
                colr='red'
            if o[y1][x1]=="O":
                button1=tk.Button(master,text='🧿',bg=colr)
            else:
                button1=tk.Button(master,text=' ',bg=colr)
            button1.grid(column=x1,row=y1,padx=5,pady=5)        
        elif flag1==1:#implies final button is clicked
            sy=startscurrent[1]
            sx=startscurrent[0]
            fx=x1
            fy=y1
            if validfinals(sx,sy,fx,fy):
                #actions
                if sx==fx:
                    o[(sy+fy)//2][sx]=" "
                    button1=tk.Button(master,text=' ',bg='green')
                    button1.grid(column=sx,row=(sy+fy)//2,padx=5,pady=5)
                    o[fy][fx]="O"
                    button1=tk.Button(master,text='🧿',bg='green')
                    button1.grid(column=fx,row=fy,padx=5,pady=5)
                    o[sy][sx]=" "
                    button1=tk.Button(master,text=' ',bg='green')
                    button1.grid(column=sx,row=sy,padx=5,pady=5)
                    
                    if moves(o):
                        #If moves are there
                        pass
                    else:
                        return
                if sy==fy:
                    o[sy][(sx+fx)//2]=" "
                    button1=tk.Button(master,text=' ',bg='green')
                    button1.grid(column=(sx+fx)//2,row=sy,padx=5,pady=5)
                    o[fy][fx]="O"
                    button1=tk.Button(master,text='🧿',bg='green')
                    button1.grid(column=fx,row=fy,padx=5,pady=5)
                    o[sy][sx]=" "
                    button1=tk.Button(master,text=' ',bg='green')
                    button1.grid(column=sx,row=sy,padx=5,pady=5)
                    if moves(o):
                        #If moves are there
                        pass
                    else:
                        return
                flag1=0
                for i in range(1,8):
                    for j in range(1,8):
                        if o[i][j]=="O":
                            button1=tk.Button(master,text='🧿',bg='green',command=lambda m=(j,i):which_button(m))
                        else:
                            button1=tk.Button(master,text=' ',bg='green',command=lambda m=(j,i):which_button(m))
                        button1.grid(column=j,row=i,padx=5,pady=5)
                button5=tk.Button(master,text="EXIT GAME",bg='red',command=lambda: master.destroy())
                button5.grid(column=8,row=8)
            else:
                button1=tk.Button(master,text=o[y1][x1],bg='red')
                button1.grid(column=x1,row=y1,padx=5,pady=5)
                
        return(button_press)




    t=[(1,1),(1,2),(2,1),(2,2),(6,1),(6,2),(7,1),(7,2),(1,6),(1,7),(2,6),(2,7),(6,6),(6,7),(7,6),(7,7)]
    k=[(4,1),(4,2),(4,6),(2,4),(6,4),(4,7),(1,4),(7,4)]
    flag1=0




    def game(l):
        global master
        master=tk.Tk()
        master.geometry("350x275")
        master.title('GAME ON')
        for i in range(1,8):
            for j in range(1,8):
                if o[i][j]=="O":
                    button1=tk.Button(master,text='🧿',bg='green',command=lambda m=(j,i):which_button(m))
                else:
                    button1=tk.Button(master,text=' ',bg='green',command=lambda m=(j,i):which_button(m))
                button1.grid(column=j,row=i,padx=5,pady=5)
        button5=tk.Button(master,text="EXIT GAME",bg='red',command=lambda: master.destroy())
        button5.grid(column=8,row=8)
        master.mainloop()




    #LOGIN WINDOW
    def click():
        global username
        global age
        global f
        username=username_entry.get()
        age=age_entry.get()
        if username.isalpha() and age.isdigit() and int(age)<100 and int(age)>3:
            
            f=1
            pass
        else:
            invalidinput1=tk.Label(sqlwind, text="ENTER ONLY ALPHABETS FOR USERNAME\nENTER ONLY NUMBERS BETWEEN 3 and 100", bg='red')
            invalidinput1.grid(column=0,row=3, sticky=tk.W, padx=5, pady=5)
            f=0
            return
        
        sqlwind.destroy()
    sqlwind=tk.Tk()
    sqlwind.geometry("400x150")
    sqlwind.title('Login')

    username_label = tk.Label(sqlwind, text="Username:")
    username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

    username_entry = tk.Entry(sqlwind)
    username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

    age_label = tk.Label(sqlwind, text="Age:")
    age_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

    age_entry = tk.Entry(sqlwind)
    age_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

    login_button = tk.Button(sqlwind, text="Login",command=lambda:click())
    login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

    sqlwind.mainloop()
    if f==1:
        
        con=m.connect(host="localhost",user="root",passwd="navi",database="navaneetha")
        if con.is_connected():
            mycursor=con.cursor()
            sql="Create table if not exists marble(id int primary key, name varchar(50),age varchar(3), score int default 0)"
            mycursor.execute(sql)
            con.commit()
            sql='select count(*) from marble;'
            mycursor.execute(sql)
            nr=int(mycursor.fetchall()[0][0])
            sql='select name from marble;'
            mycursor.execute(sql)
            existingusers=mycursor.fetchall()
            
            c=0
            for i in existingusers:
                if username==i[0]:
                    c=1
                    break
                else:
                    continue
            if c==0:
                sql1="insert into marble (id,name,age,score) values(%s,%s,%s,0)"
            
                #val=[(1,'megz',40),(2,'navi',30),(3,'saanvi',40)]
                mycursor.execute(sql1,(nr+1,username,age))
                con.commit()
            else:
                print("not connected")
    else:
        pass
    

    #RULES WINDOW
    def click2():
        ruleswind.destroy()
        game(o)
        
    ruleswind=tk.Tk()
    ruleswind.geometry("700x500")
    ruleswind.configure(bg='blue')
    ruleswind.title("BRAINVITA MARBLE SOLITAIRE")
    s="Welcome to the computer version of the Brainvita Marble game\nThe rules are simple:-\n1. You press the start and end point to move the O-marble.\n2. A marble must be there between the start and end point.\n3. The start point must have a marble.\n4. The end point must be vacant.\n5. When you move a marble the from start to end point the marble in between those two points is removed from the board.\n6. Invalid move is shown by the red button\n7. WINNING-You continue moving and removing the marbles to finally bring it down to one marble at the centre coordinate(4,4)."
    rules_label = tk.Label(ruleswind, text=s)
    rules_label.configure(bg='green')
    rules_label.grid(column=0, row=1, padx=5, pady=5)

    image1 = Image.open("marblesolitaireimg.jpg")
    test = ImageTk.PhotoImage(image1)
    Label1=tk.Label(image=test)
    Label1.image = test
    Label1.grid(column=0, row=2, padx=5, pady=5)

    play_button = tk.Button(ruleswind, text="LETS PLAY THE GAME",bg='pink',command=lambda:click2())
    play_button.grid(column=0, row=3, padx=5, pady=5)

    ruleswind.mainloop()
    
    sql2="update Marble set score=score+{} where name='{}'".format(points,username)
    
    mycursor.execute(sql2)

    
    
    con.commit()
    con.close()
except m.Error as e:
    print("error",e)
             

