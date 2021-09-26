from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import matplotlib.pyplot as plt
import requests
import bs4
import mysql.connector

def f1():
  add_window.deiconify()
  main_window.withdraw()

def f2():
  main_window.deiconify()
  add_window.withdraw()

def f3():
  view_window.deiconify()
  main_window.withdraw()
  vw_emp_data.delete(1.0, END)
  info = ""
  con = None
  try:
    con = mysql.connector.connect(host="localhost",user="root",password="abc456", database="emp_db")
    cursor = con.cursor()
    sql = "select * from emp"
    cursor.execute(sql)
    data = cursor.fetchall()
    for d in data:
      info = info + "id:" + str(d[0]) + " name:" + str(d[1]) + " salary:" + str(d[2]) +  "\n"
    vw_emp_data.insert(INSERT , info)
  except Exception as e:
    showerror("Failure ", e)
  finally:
    if con is not None:
      con.close() 

def f4():
  main_window.deiconify()
  view_window.withdraw()

def f5():
  update_window.deiconify()
  main_window.withdraw()
  if (uw_ent_id.get() == "" or uw_ent_name.get() == "" or uw_ent_salary.get() == ""):
    showerror("OOPS!", "Please fill all the details")
  elif (uw_ent_id.get().isdigit() == False):
    showerror("OOPS!", "Id can have integers only")
    uw_ent_id.delete(0, END)
    uw_ent_name.delete(0, END)
    uw_ent_salary.delete(0, END)
  elif int(uw_ent_id.get()) <= 0 :
    showerror("OOPS!", "Id can't be negative")
    uw_ent_id.delete(0, END)
    uw_ent_name.delete(0, END)
    uw_ent_salary.delete(0, END)
  elif (len(uw_ent_name.get()) < 2):
    showerror("OOPS!", "Name can't consist of only one alphabet")
    uw_ent_id.delete(0, END)
    uw_ent_name.delete(0, END)
    uw_ent_salary.delete(0, END)
  elif ((((uw_ent_name.get()).replace(" ","")).isalpha()) == False):
    showerror("OOPS!", "Name can't consist of digits or special characters ")
    uw_ent_id.delete(0, END)
    uw_ent_name.delete(0, END)
    uw_ent_salary.delete(0, END)
  elif (uw_ent_salary.get().isdigit() == False):
    showerror("OOPS!", "Salary can be integers only")
    uw_ent_id.delete(0, END)
    uw_ent_name.delete(0, END)
    uw_ent_salary.delete(0, END)
  elif int(uw_ent_salary.get()) < 0:
    showerror("OOPS!", "Salary can't be negative")
    uw_ent_id.delete(0, END)
    uw_ent_name.delete(0, END)
    uw_ent_salary.delete(0, END)
  elif int(uw_ent_salary.get()) < 8000:
    showerror("OOPS!", "Salary can't be less than 8000")
    uw_ent_id.delete(0, END)
    uw_ent_name.delete(0, END)
    uw_ent_salary.delete(0, END)
  else:
    con = None
    try:
      id = int(uw_ent_id.get())
      name = uw_ent_name.get()
      salary = int(uw_ent_salary.get())
      con = mysql.connector.connect(host="localhost",user="root",password="abc456",database="emp_db")
      cursor = con.cursor()
      sql = "update emp set name = '%s', salary = '%d' where id = '%d'"
      cursor.execute(sql % (name, salary, id))
      if cursor.rowcount > 0:
        con.commit()
        showinfo("Success ", "record updated")
        uw_ent_id.delete(0, END)
        uw_ent_name.delete(0, END)
        uw_ent_salary.delete(0, END)
      else:
        showerror("Failure ", "record does not exists ")
        uw_ent_id.delete(0, END)
        uw_ent_name.delete(0, END)
        uw_ent_salary.delete(0, END)
    except Exception as e:
      showerror("Issue", e)
      con.rollback()
    finally:
      if con is not None:
        con.close()

def f6():
  main_window.deiconify()
  update_window.withdraw()

def f7():
  delete_window.deiconify()
  main_window.withdraw()
  if (dw_ent_id.get() == ""):
    showerror("OOPS!", "Please enter valid Id")
  elif ((dw_ent_id.get()).isdigit() == False):
    showerror("OOPS!", "Id should consist of integers only")
    dw_ent_id.delete(0, END)
  elif (int(dw_ent_id.get()) <= 0):
    showerror("OOPS!", "Id can't be negative")
    dw_ent_id.delete(0, END)
  else:
    con = None
    try:
      id = int(dw_ent_id.get())
      con = mysql.connector.connect(host="localhost",user="root",password="abc456",database="emp_db")
      cursor = con.cursor()
      sql = "delete from emp where id = '%d'"
      cursor.execute(sql % (id))
      if cursor.rowcount > 0:
        con.commit()
        showinfo("Success ", "record deleted ")
        dw_ent_id.delete(0, END)
      else:
        showerror("Failure ", "record does not exists ")
        dw_ent_id.delete(0, END)
    except Exception as e:
      showerror("Issue ", e)
      con.rollback()
    finally:
      if con is not None:
        con.close()

def f8():
  main_window.deiconify()
  delete_window.withdraw()

def f9():
  if (ent_name.get() == "" or ent_name.get() == "" or ent_salary.get() == ""):
    showerror("OOPS!", "Please fill all the details")
  elif (ent_id.get().isdigit() == False):
    showerror("OOPS!", "Id can have integers only")
    ent_id.delete(0, END)
    ent_name.delete(0, END)
    ent_salary.delete(0, END)
  elif (int(ent_id.get()) <= 0) :
    showerror("OOPS!", "ID can't be negative")
    ent_id.delete(0, END)
    ent_name.delete(0, END)
    ent_salary.delete(0, END)
  elif (len(ent_name.get()) < 2):
    showerror("OOPS!", "Name can't consist of only one alphabet")
    ent_id.delete(0, END)
    ent_name.delete(0, END)
    ent_salary.delete(0, END)
  elif ((((ent_name.get()).replace(" ","")).isalpha()) == False):
    showerror("OOPS!", "Name can't consist of digits or special characters")
    ent_id.delete(0, END)
    ent_name.delete(0, END)
    ent_salary.delete(0, END)
  elif (ent_salary.get().isdigit() == False):
    showerror("OOPS!", "Salary can be integers only")
    ent_id.delete(0, END)
    ent_name.delete(0, END)
    ent_salary.delete(0, END)
  elif int(ent_salary.get()) < 0:
    showerror("OOPS!", "Salary can't be negative")
    ent_id.delete(0, END)
    ent_name.delete(0, END)
    ent_salary.delete(0, END)
  elif int(ent_salary.get()) < 8000:
    showerror("OOPS!", "Salary can't be less than 8000 ")
    ent_id.delete(0, END)
    ent_name.delete(0, END)
    ent_salary.delete(0, END)
  else:
    con = None
    try:
      id = int(ent_id.get())
      name = ent_name.get()
      salary = int(ent_salary.get())
      con = mysql.connector.connect(host="localhost",user="root",password="abc456",database="emp_db")
      cursor = con.cursor()
      sql = "insert into emp values('%d', '%s', '%d')"
      cursor.execute(sql%(id, name, salary))
      con.commit()
      showinfo("Success ", "record added")
      ent_id.delete(0, END)
      ent_name.delete(0, END)
      ent_salary.delete(0, END)
    except Exception as e:
      showerror("Failure ", "Duplicate entry for id is not allowed")
      con.rollback()
    finally:
      if con is not None:
        con.close()
 
main_window = Tk()
main_window.title("E.M.S")
main_window.geometry("2000x1000+100+50")
f = ("Courier", 20, "bold")

mw_btn_add = Button(main_window, text="Add", width=10, font=f, command = f1 )
mw_btn_add.pack(pady=4)

add_window = Toplevel(main_window)
add_window.geometry("500x500")
add_window.title("Add Employee Details")
add_window.withdraw()

lbl_id = Label(add_window, text="enter id ", font=f)
lbl_id.pack(pady=4)
ent_id = Entry(add_window, bd=4 , font=f)
ent_id.pack(pady=4)

lbl_name = Label(add_window, text="enter name ", font=f)
lbl_name.pack(pady=4)
ent_name = Entry(add_window, bd=4 , font=f)
ent_name.pack(pady=4)

lbl_salary = Label(add_window, text="enter salary", font=f)
lbl_salary.pack(pady=4)
ent_salary = Entry(add_window, bd=4 , font=f)
ent_salary.pack(pady=4)

btn_save = Button(add_window, text="Save", width=10, font=f ,command=f9)
btn_save.pack(pady=4)

btn_back = Button(add_window, text="Back", width=10, font=f,command = f2 )
btn_back.pack(pady=4)

mw_btn_view = Button(main_window, text="View", width=10, font=f, command= f3 )
mw_btn_view.pack(pady=4)

view_window = Toplevel(main_window)
view_window.geometry("700x500")
view_window.title("View Employee Details ")

vw_emp_data = ScrolledText(view_window, width = 40, height = 10, font = f)
vw_btn_back = Button(view_window, text = "Back", width = 10, font = f, command = f4)
vw_emp_data.pack(pady = 5)
vw_btn_back.pack(pady = 5)
view_window.withdraw()


mw_btn_update = Button(main_window, text="Update", width=10, font=f, command=f5)
mw_btn_update.pack(pady=4)

update_window = Toplevel(main_window)
update_window.geometry("500x500")
update_window.title("Update Employee Details")
update_window.withdraw()

uw_lbl_id = Label(update_window, text="enter id ", font=f)
uw_lbl_id.pack(pady=4)
uw_ent_id = Entry(update_window, bd=4 , font=f)
uw_ent_id.pack(pady=4)

uw_lbl_name = Label(update_window, text="enter name ", font=f)
uw_lbl_name.pack(pady=4)
uw_ent_name = Entry(update_window, bd=4 , font=f)
uw_ent_name.pack(pady=4)

uw_lbl_salary = Label(update_window, text="enter salary", font=f)
uw_lbl_salary.pack(pady=4)
uw_ent_salary = Entry(update_window, bd=4 , font=f)
uw_ent_salary.pack(pady=4)

uw_btn_save = Button(update_window, text="Save", width=10, font=f , command = f5)
uw_btn_save.pack(pady=4)

uw_btn_back = Button(update_window, text="Back", width=10, font=f , command = f6)
uw_btn_back.pack(pady=4)

mw_btn_delete = Button(main_window, text="Delete", width=10, font=f ,command = f7)
mw_btn_delete.pack(pady=4)

delete_window = Toplevel(main_window)
delete_window.geometry("500x500")
delete_window.title("Delete Employee Details")
delete_window.withdraw()

dw_lbl_id = Label(delete_window, text="enter id ", font=f)
dw_lbl_id.pack(pady=4)
dw_ent_id = Entry(delete_window, bd=4 , font=f)
dw_ent_id.pack(pady=4)

dw_btn_save = Button(delete_window, text="Save", width=10, font=f , command = f7 )
dw_btn_save.pack(pady=4)
dw_btn_back = Button(delete_window, text="Back", width=10, font=f ,command = f8 )
dw_btn_back.pack(pady=4)

def bar_chart():
  con = mysql.connector.connect(host="localhost",user="root",password="abc456", database="emp_db")
  cursor = con.cursor()
  sql = "select * from emp"
  cursor.execute(sql)
  data = cursor.fetchall()
  na, sa = [], []
  for d in data:
    na.append(d[1])
    sa.append(d[2])      
  plt.bar(na, sa, width=0.25, color="blue")
  plt.xlabel("Employee's Names")
  plt.ylabel("Salary")
  plt.title("top 5 highest salaries paid ")
  plt.grid()
  plt.savefig("barchart.jpg" )
  plt.show()

mw_btn_charts = Button(main_window, text="Charts", width=10, font=f, command = bar_chart )
mw_btn_charts.pack(pady=4)

QOTD = Label(main_window, text="QOTD" , width = 3000,  font=("Courier", 15, "bold"))
QOTD.pack(pady=4)

try:
  wa = "https://www.brainyquote.com/quote_of_the_day"
  res = requests.get(wa)
  data = bs4.BeautifulSoup(res.content, "html.parser")             
  info = data.find("img", {"class":"p-qotd"})
  quote = info['alt']
  QOTD.config(text=quote)
except Exception as e:
  print("issue",e)

main_window.mainloop()
  