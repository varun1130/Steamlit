import streamlit as st
import mysql.connector
from PIL import Image
import time

# --------------------Sql Connect--------------------------------------------------------------->
con = mysql.connector.connect(host="localhost",user="root",password= "Admin@02.,")
commit = con.cursor()
commit.execute("use user_data")

#-----------------------SLIDEBAR---------------------------------------------------------------->
rad = st.sidebar.radio("Navigator",["Register","Login","Forget Password","about us"])


#------------------DEF_FUNCTIONS---------------------------------------------------------------->

#___REDISTER_______:
def Register(full_name,email_id,phone_num,user_name,user_password):
    p = st.progress(0)
    for i in range(1,100):
        time.sleep(0.01)
        p.progress(i+1)
    user_ata = (full_name,email_id,phone_num,user_name,user_password)
    store_qry = "insert into user(full_name,email_id,phone_num,user_name,user_password) values (%s,%s,%s,%s,%s)"
    commit.execute(store_qry,user_ata)
    con.commit()
    st.balloons()
#__LOGIN____:
def login(user_name):
    qry = "select user_password from user where user_name =%s "
    val = (user_name,)
    commit.execute(qry,val)
    data = commit.fetchall()
    return data
#____FORET PASSWORD___:
def forget(email_id):
    qry = 'select user_name from user where email_id =%s'
    val = (email_id,)
    commit.execute(qry,val)
    data = commit.fetchall()
    return data
#_____Password UPDATE_____:
def pass_update(user_password,email_id):
    qry ="update user set user_password=%s where email_id= %s"
    val =(user_password,email_id)
    commit.execute(qry,val)
    con.commit()  
    return True
#-------------------------------REGISTER---------------------------------------------------------------------->

if rad == "Register":
    st.title("Register")  
    f_name,= st.columns(1)
    full_name = f_name.text_input("Full Name")
    mail,P_num = st.columns(2)
    email_id = mail.text_input("MAIL ID")
    phone_num = P_num.text_input("Phone Number")
    us,pw = st.columns(2)
    user_name = us.text_input("User name")
    user_password = pw.text_input("Password",type="password")
    pw1, = st.columns(1)
    Re_password = pw1.text_input("Re-Enter the Password Again",type="password")
    check = st.checkbox("I agree")
    button = st.button("Submit")

    if (button==True) and (user_password == Re_password):
        Register(full_name,email_id,phone_num,user_name,user_password)
    else:
        if button==True:
            st.error("Password did not match")
            st.warning("Try again")
#----------------------------LOGIN-------------------------------------------------------------------------->
if rad == "Login":
    name, = st.columns(1)
    User_Name = name.text_input("User Name")
    pw, = st.columns(1)
    pass_word = pw.text_input("Password")
    button = st.button("Submit")
    if button == True:
        password = login(User_Name)
        if password[0][0] == pass_word:
            st.balloons()
            st.info("Login success")
        else:
            st.error("Incorrect password")

#----------------------------------------------------------------------------------------------------------
if rad =="Forget Password":
    pw, = st.columns(1)
    user_forget_email = pw.text_input("Enter the Email-id")
    button = st.button("Submit")
    val = forget(user_forget_email)
    print(val)
    if bool(val) == True:
        new_pass = pw.text_input("Enter the New Password")
        flag = 1
        if button == True:
            val = pass_update(new_pass,user_forget_email)
            if val ==True:
                st.warning("Update Sucess")
                st.warning("Go to LoginPage To Login")

    
#-----------------------------------------------------------------------------------------------------------
if rad == "about us":
    st.error("this error")
    st.exception(RuntimeError("this is runtime error"))
    st.info("congrats")
    st.warning("warning")
    