#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import tkinter
import tkMessageBox

def ask1():
  tkMessageBox.showinfo( "Hello Python", "Hello Runoob")

def ask2():
  tkMessageBox.showinfo( "Hello Python", "Hello Runoob")

def ask3():
  tkMessageBox.showinfo( "Hello Python", "Hello Runoob")


def ask4():
  tkMessageBox.showinfo( "Hello Python", "Hello Runoob")

def ask5():
  tkMessageBox.showinfo( "Hello Python", "Hello Runoob")

def ask6():
  tkMessageBox.showinfo( "Hello Python", "Hello Runoob")

def ask7():
  tkMessageBox.showinfo( "Hello Python", "Hello Runoob")

def ask8():
  tkMessageBox.showinfo( "Hello Python", "Hello Runoob")

def ask9():
  tkMessageBox.showinfo( "Hello Python", "Hello Runoob")

def ask10():
  tkMessageBox.showinfo( "Hello Python", "Hello Runoob")

def ask():
  tkMessageBox.showinfo("查询功能","查询1:\n查询2:\n查询3:\n查询4:\n查询5:\n查询6:\n查询7:\n查询8:\n查询9:\n查询10")
  top=tkinter.Tk(className="查询")

  button1 = tkinter.Button(top, text = '查询1', command = ask1)
  button2 = tkinter.Button(top, text = '查询2', command = ask2)
  button3 = tkinter.Button(top, text = '查询3', command = ask3)
  button4 = tkinter.Button(top, text = '查询4', command = ask3)
  button5 = tkinter.Button(top, text = '查询5', command = ask5)
  button6 = tkinter.Button(top, text = '查询6', command = ask6)
  button7 = tkinter.Button(top, text = '查询7', command = ask7)
  button8 = tkinter.Button(top, text = '查询8', command = ask8)
  button9 = tkinter.Button(top, text = '查询9', command = ask9)
  button10 = tkinter.Button(top, text = '查询10', command = ask10)

  button1.pack()
  button2.pack()
  button3.pack()
  button4.pack()
  button5.pack()
  button6.pack()
  button7.pack()
  button8.pack()
  button9.pack()
  button10.pack()

  #进入消息循环体
  top.mainloop()


top = tkinter.Tk(className="database")

button = tkinter.Button(text = '查询', command = ask)
button.pack()

top.mainloop()