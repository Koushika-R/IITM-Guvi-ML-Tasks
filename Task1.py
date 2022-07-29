# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 10:16:22 2022

@author: krith
"""

#Registration and Login system using Python, file handling:
import re
def name(user_id,password):
    expression_mail= "^[A-Za-z]+@[A-Za-z]+\.[A-Za-z]{1,}$"
    expression_password = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{5,16}$'
    return all((re.match(expression_mail,user_id),re.match(expression_password,password)))
        
def get_users():
    with open("User data.txt","r") as file:
        for info in file:
            user_id,user_credentials = info.split(',')
            user_credentials=user_credentials.rstrip("\n") #removing the new line at the end
            yield (user_id,user_credentials)

def user_exist(user_id):
    return any(user_id==file_users for file_users, user_credentials in get_users())

def acc_creation(email, password):
    if not user_exist(email):
       with open("User data.txt","a") as file:
           file.write(email)
           file.write(",")
           file.write(password)
           file.write("\n")
           print("Congratulations! Account created successfully.")
    else:
        print("User name already exists!")

def login_credentials(email,password):
    return any((email,password) == credentials for credentials in get_users())

def login(email,password):
    if login_credentials(email,password):
        print("Valid Credentials")
    else:
        print("Invalid Credentials")
        
def update_password(user_id, new_password):
    if user_exist(user_id):
        with open("User data.txt","r") as file:
            file_lines = file.readlines()
        with open("User data.txt", "w") as updated_userdata:
            for i in file_lines:
                mail_id,updated_password =i.split(",")
                if mail_id == user_id:
                    updated_userdata.write(mail_id)
                    updated_userdata.write(",")
                    updated_userdata.write(new_password)
                    updated_userdata.write("\n")
                else:
                    updated_userdata.write(mail_id)
                    updated_userdata.write(",")
                    updated_userdata.write(updated_password)
    else:
        print("Invalid User ID")


if __name__ == "__main__":
    
    
    while True:
        choice = ""
        
        print("1 : Login")
        print("2 : Create New Account")
        print("3 : Change Password")
        
        choice = input("Your Choice: ")
        
        
        if choice == "1":
            print("Enter Account Info: ")
            email = input("UserName: ")
            password = input("Password: ")
            login(email, password)
            
        elif choice == "2":
            
            print("Enter Account Details: ")
            user_id = input("UserName: ")
            password = input("Password: ")
            name(user_id, password)                  

        elif choice == "3":
            print("Enter Account Details: ")
            user_id= input("UserName: ")
            new_password = input("New Password: ")
            
            if update_password(user_id, new_password):
                
                
                if len(new_password) > 5 and len(new_password) < 16:
                        update_password(user_id, new_password)
                else:
                    print("Please Enter a Password with minimum 5 character and Maximum of 16 Character")
                    
            else:
                print("Username Dosent't Exists")
                break
        
        print("\n\n")