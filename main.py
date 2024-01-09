from tkinter import *
import os

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("Website Blocker")
root.configure(bg='#DCE0AC')

Label(root, text='Website Blocker', font='Helvetic 20 bold').pack()
host_path = r'C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

Label(root, text='Enter Website :', font='Helvetic 13 bold').place(x=5, y=60)
Websites = Text(root, font='Helvetica 10', height='2', width='40', bg='#EEEAE6')  # Set background color
Websites.place(x=140, y=60)

def block_website():
    website_lists = Websites.get(1.0, END)
    websites = list(website_lists.split(","))
    with open(host_path, 'r+') as host_file:
        file_content = host_file.read()
        for web in websites:
            if web.strip() in file_content:
                Label(root, text='Already Blocked', font='Helvetica 12 bold').place(x=200, y=200)
            else:
                host_file.write(ip_address + " " + web.strip() + '\n')
                Label(root, text="Blocked", font='Helvetica 12 bold').place(x=230, y=200)

def unblock_website():
    website_lists = Websites.get(1.0, END)
    websites = list(website_lists.split(","))
    with open(host_path, 'r') as host_file:
        lines = host_file.readlines()
    with open(host_path, 'w') as host_file:
        for line in lines:
            if not any(website.strip() in line for website in websites):
                host_file.write(line)
        Label(root, text="Unblocked", font='Helvetica 12 bold').place(x=230, y=200)

block = Button(root, text='Block', font='Helvetica 12 bold', pady=5, command=block_website, width=6, bg='#AE8B6F',
               activebackground='#2D2E49')
block.place(x=230, y=150)

unblock = Button(root, text='Unblock', font='Helvetica 12 bold', pady=5, command=unblock_website, width=6,
                 bg='#FFD4AC', activebackground='#A5664B')
unblock.place(x=300, y=150)

root.mainloop()
