def add():
    b=enN.get()
    c=enT.get()
    d=enC.get()
    f=open('db.txt','a')
    f.write(b+' ')
    f.write(str(c)+' ')
    f.write(d+'|')
    f.close()



def search_contacts():  
    e=enNN.get()
    addressbook=open("db.txt")
    for line in addressbook:
        records=line.split('|')
        print(records)
        for record in records:
                if e in record:
                    contacts.insert(END,record)
                    break
                else:
                    print("Name not found,unlucky!!")
                    continue

                 
def delete_contact():
    e=enNNN.get()
    fdb=open("db.txt")
    
    nameExist=False
    for line in fdb:
        records=line.split('|')
        print (records)
        
        fout=open('db.txt','w+')
        for record in records:
            
            if e not in record:
                fout.write(str (record)+"|")
                fout.close            
            else:
                
                nameExist=True
                
    if not nameExist:
        print("Name not found,unlucky!!")

        
                                     
#ADD CONTACTS  
from tkinter import*

def add_contacts():
 ae=Tk()
 ae.title('ADD CONTACTS')
 ae.configure(background="#34495E")
 ae.geometry('250x200')
 global fr1
 fr1=Frame(ae,background="#34495E",padx=15, pady=15)
 fr1.pack()

 labN=Label(fr1,text="NAME",font='Times 10 bold')
 labN.grid(row=0,column=0)
 global enN
 enN=Entry(fr1,background="#FFFFFF")
 enN.grid(row=0,column=1)

 labT=Label(fr1,text="TELEPHONE",font='Times 10 bold')
 labT.grid(row=1,column=0,padx=10, pady=10)


 global enT
 enT=Entry(fr1,)
 enT.grid(row=1,column=1)

 labA=Label(fr1,text='ADDRESS',font='Times 10 bold')
 labA.grid(row=2,column=0)
 global enC
 enC=Entry(fr1,)
 enC.grid(row=2,column=1)
 
 fr2=Frame(ae,)
 fr2.pack()
 
 addB=Button(fr2,text='ADD CONTACT',command=add,font='Times 10 bold')
 addB.grid(row=0,column=0)

#SEARCH CONTACTS
#from tkinter import*

def searchhh_contacts():
 search=Tk()
 search.title('SEARCH CONTACTS')
 search.configure(background="#34495E")
 search.geometry('250x250')
 global fr3
 fr3=Frame(search)
 fr3.pack()

 labNN=Label(fr3,text='NAME')
 labNN.grid(row=1,column=1)
 global enNN 
 enNN=Entry(fr3)
 enNN.grid(row=1,column=2)


 fr4=Frame(search)
 fr4.pack()

 searchF=Button(fr4,text='SEARCH',command=search_contacts)
 searchF.grid(row=0,column=2)

 fr5=Frame(search)
 fr5.pack()
 global contacts
 contacts=Listbox(fr5,height=30,width=26)
 contacts.pack()

#DELETE CONTACTS
#from tkinter import*
def delete_contacts():
 delete=Tk()
 delete.title('DELETE CONTACTS')
 delete.configure(background="#34495E")
 delete.geometry('250x100')
 global fr6

 fr6=Frame(delete) 
 fr6.pack()
 
 
 labNNN=Label(fr6,text='NAME')
 labNNN.grid(row=1,column=1)
 global enNNN
 enNNN=Entry(fr6)
 enNNN.grid(row=1,column=2)


 fr7=Frame(delete)
 fr7.pack()

 deleteF=Button(fr7,text='DELETE',command=delete_contact)
 deleteF.grid(row=0,column=2)

 fr8=Frame(delete)
 fr8.pack()


#phonebook
#from tkinter import*
main=Tk()
main.title('PHONE BOOK')
main.configure(background="#34495E")
main.geometry('250x400')

fr9=Frame(main,background="#34495E",padx=15, pady=15)
fr9.pack()

adddB=Button(fr9,text="ADD CONTACTS",command=add_contacts,background='#BFC9CA')
adddB.grid(row=0,column=0,padx=25, pady=25)

ddelB=Button(fr9,text="DELETE CONTACTS",command=delete_contacts,background='#BFC9CA')
ddelB.grid(row=1,column=0,padx=25, pady=25)

ssearchB=Button(fr9,text="SEARCH CONTACT",command=searchhh_contacts,background='#BFC9CA')
ssearchB.grid(row=2,column=0,padx=25, pady=25)
