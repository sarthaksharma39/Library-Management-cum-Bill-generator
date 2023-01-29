import mysql.connector
conn=mysql.connector.connect(user='root',password='root',host='localhost',database='library')
myc=conn.cursor()
#details given by manager
o="y"
while(o=="y" or o=="Y"):
   m="""      BOOKS SHOPPING 
             *SARTHAK  Mart*
       shop no. 3 basant bagh enclave 
          PIN CODE:  151001
    mobile number-8421468850"""   
   print(m)
   print('''press N for BUYING NOVELS
press T for BUYING TEXTBOOKS
press G for BUYING GUIDE''')
   print("type X if you DON'T want to buy anything")
   c=str(input("enter your choice(N\T\G\X):"))
   #press N for BUYING NOVELS
   #press T for BUYING TEXTBOOKS
   #press G for BUYING GUIDE
   #press X to exit from program
   if(c=="N" or c=="n"):
      print("~~NOVEL'S~~")
      impt=int(input("no. of item purchase:"))
      for a in range(1,impt+1):
         print(a)
      date=input("invoice date:")
      print("details of customer")
      customer=str(input("customer's name:"))
      address=str(input("customer's address:"))
      city=str(input("customer's city:"))
      state=str(input("customer's state:"))
      mobilenumber=int(input("customer's mobile number:"))
      sql1="insert into customer (name,address,city,state,mob_number) values('{}','{}','{}','{}',{})".format(customer,address,city,state,mobilenumber)
      myc.execute(sql1)
      conn.commit()
      
      total=0
      maxitem=50 # maximum  number of items can be purchased at a time 
      if(impt<=maxitem):
         for a in range(1,impt+1):
            print("serial no:",a)
            i=str(input("item name:"))
            rate=float(input("price of item in rupees:"))
            qty=int(input("quantity of item purchased:"))
            value=qty*rate # total  price of product with no. of quantity 
            print("Total price:",value)  # total  amount of particular product
            total=total+value # total  amount of all products
            sql2="insert into item (serial_no,item_name,price,quantity) values({},'{}',{},{})".format(a,i,rate,qty)
            myc.execute(sql2)
            conn.commit()
         print("Items Purchased Till Now:")
         myc.execute('select * from item')
         data=myc.fetchall()
         for row in data:
            print(row)
         print("Total Amount:",total)
         gst=28/100
         gtax=total*gst #gst taxed amount
         price=total+gtax # total amount of all products after adding gst 
         if(total<100):
            print("Final price:",price)
         elif(total>=100 and total<=800):
            discount=5/100
            dprice=total*discount # discount amount
            print("Final price:",price-dprice)
         elif(total>800 and total<=5000):
            discount=15/100
            dprice=total*discount
            print("Final price:",price-dprice)
         elif(total>5000 and total<=14000):
            discount=20/100
            dprice=total*discount
            print("Final price:",price-dprice)
         elif(total>14000):
            discount=25/100
            dprice=total*discount
            print("Final price:",price-dprice)
      else:
         print(" Sorry You Can Only Buy 41 Items At A Time")
      print("NOVEL'S BILL")
   elif(c=="T" or c=="t"):
      print("~~TEXTBOOK'S~~")
      date=input("invoice date:")
      impt=int(input("no. of item purchase:"))
      print("details of customer")
      customer=str(input("customer's name:Mr./Miss:"))
      adress=str(input("customer's adress:"))
      city=str(input("customer's city:"))
      state=str(input("customer's state:"))
      mobilenumber=int(input("customer's mobile number:"))
      sql1="insert into customer (name,address,city,state,mob_number) values('{}','{}','{}','{}',{})".format(customer,address,city,state,mobilenumber)
      myc.execute(sql1)
      conn.commit()
      
      total=0 
      maxitem=41 # maximum  number of items can be purchased at a time 
      if(impt<=maxitem):
         for a in range(1,impt+1):
            print("serial no:",a)
            i=str(input("item name:"))
            rate=float(input("price of item in rupees:"))
            qty=int(input("quantity of item purchased:"))
            value=qty*rate # total  price of product with no. of quantity 
            print("Total price:",value)  # total  amount of particular product
            total=total+value # total  amount of all products
            sql="insert into item (serial_no,item_name,price,quantity) values({},'{}',{},{})".format(a,i,rate,qty)
            myc.execute(sql)
            conn.commit()
         print("Items Purchased Till Now:")
         myc.execute('select * from item')
         data=myc.fetchall()
         for row in data:
            print(row)
         print("Total Amount:",total)
         gst=8/100
         gtax=total*gst #gst taxed amount
         price=total+gtax # total amount of all products after adding gst 
         if(total<800):
            print("Final price:",price)
         elif(total>=800 and total<=6000):
            discount=5/100
            dprice=total*discount # discount amount
            print("Final price:",price-dprice)
         elif(total>6000 and total<=11000):
            discount=15/100
            dprice=total*discount
            print("Final price:",price-dprice)
         elif(total>11000 and total<=15000):
            discount=20/100
            dprice=total*discount
            print("Final price:",price-dprice)
         elif(total>15000):
            discount=25/100
            dprice=total*discount
            print("Final price:",price-dprice)
      else:
         print(" Sorry You Can Only Buy 41 Items At A Time")
      print("TEXTBOOK'S BILL")
   
   elif(c=="G" or c=="g"):
      print("~~GUIDES~~")
      date=input("invoice date:")
      impt=int(input("no. of item purchase:"))
      print("details of customer")
      customer=str(input("customer's name:Mr./Miss:"))
      address=str(input("customer's adress:"))
      city=str(input("customer's city:"))
      state=str(input("customer's state:"))
      mobilenumber=int(input("customer's mobile number:"))
      sql1="insert into customer (name,address,city,state,mob_number) values('{}','{}','{}','{}',{})".format(customer,address,city,state,mobilenumber)
      myc.execute(sql1)
      conn.commit()
      
      total=0 
      maxitem=41 # maximum  number of items can be purchased at a time 
      if(impt<=maxitem):
         for a in range(1,impt+1):
            print("serial no:",a)
            i=str(input("item name:"))
            rate=float(input("price of item in rupees:"))
            qty=int(input("quantity of item purchased:"))
            value=qty*rate # total  price of product with no. of quantity 
            print("Total price:",value)  # total  amount of particular product
            total=total+value # total  amount of all products
            sql="insert into item (serial_no,item_name,price,quantity) values({},'{}',{},{})".format(a,i,rate,qty)
            myc.execute(sql)
            conn.commit()
         print("Items Purchased Till Now:")
         myc.execute('select * from item')
         data=myc.fetchall()
         for row in data:
            print(row)
         print("Total Amount:",total)
         gst=4/100
         gtax=total*gst #gst taxed amount
         price=total+gtax # total amount of all products after adding gst 
         if(total<200):
            print("Final price",price)
         elif(total>=200 and total<=500):
            discount=5/100
            dprice=total*discount # discount amount
            print("Final price:",price-dprice)
         elif(total>500 and total<=900):
            discount=15/100
            dprice=total*discount
            print("Final price:",price-dprice)
         elif(total>900 and total<=15000):
            discount=20/100
            dprice=total*discount
            print("Final price:",price-dprice)
         elif(total>15000):
            discount=25/100
            dprice=total*discount
            print("Final price:",price-dprice)#final price is calculated after adding gst
      else:
         print(" Sorry You Can Only Buy 41 Items At A Time")
      print("~~GUIDES~~")
   elif(c=="x" or c=="X"):
      exit()
   else:
      print("PLEASE ENTER A VALID PRODUCT CATEGORY")
      print("  N for NOVEL'S")
      print("  T for TEXTBOOKS ")
      print("  G for GUIDE'S")
   t="""     ******THANK YOU*******
              ***VISIT US AGAIN***
           **ARMart@modernworld.in**"""
   print(t)
   o=input("want to run again y/n or Y/N")
