import tkinter as tk
import time
import random
from tkinter import messagebox as mbox
import sqlite3

#色の宣言
color = "white"

#終了を押された時の処理
def shutdown():
    shut_msg = mbox.showinfo('通知','アプリケーションを終了します。')
    exit()

#送信を押された時の処理
def send():
    #送信のために、取得
    Eun_get = Eun.get()
    Epw_get = Epw.get()
    
    #ターミナルでの表示


#ヘルプページ
def help_page():

    help_root = tk.Tk()
    help_root.title('ヘルプページ')
    help_root.geometry("500x200+750+350")
    help_root.option_add('*font',['MS ゴシック',10])
    hese = "1.ダウンロードしたいYouTubeのURLを入れてください。\n"\
        "\n"\
        "2.どこのフォルダに保存するかを指定してください。\n"\
        "\n"\
        "3.mp3かmp4かのどちらかファイル形式を選択してください。\n"\
        "（初期設定はmp3が選択されています。）\n"\
        "\n"\
        "4.「変換する」をクリック。"
    help_sentens = tk.Label(help_root,text=hese,font=('','12'),bg='white')
    help_sentens.pack(padx=40,pady=30)

#アップデート情報ページ
def details_page():
    details_root = tk.Tk()
    details_root.title('アップデート情報')
    details_root.geometry("440x200+750+300")
    details_root.option_add('*font',['MS ゴシック',10])

    dese = '～アップデート情報～\n'\
        '1.0verにて...\n'\
        '・メモ機能\n'\

    details_sentens = tk.Label(details_root,text=dese,font=('','12'),bg='white')
    details_sentens.pack(padx=20,pady=30)

#アカウント新規作成（データベース使用）
def newaccount():
    newaccount_root = tk.Tk()
    newaccount_root.title('アカウント新規作成')
    newaccount_root.geometry('440x200+750+400')
    newaccount_root.option_add('*font',['メイリオ',10])

    #ラベルの作成
    word_new = tk.Label(newaccount_root, text = "ユーザー名とパスワードを決めて入力してください", bg = color)
    username_new = tk.Label(newaccount_root, text = "ユーザー名:", bg = color)
    password_new = tk.Label(newaccount_root, text = "パスワード:", bg = color)

    word_new.place(x = 20, y = 20)
    username_new.place(x = 30, y = 65)
    password_new.place(x = 30, y = 100)

    #エントリーの作成
    Eun_new = tk.Entry(newaccount_root, bg = color, width = 25, bd = 5)
    Epw_new = tk.Entry(newaccount_root, bg = color, width = 25, bd = 5, show = "●")

    Eun_new.place(x = 110, y = 65)
    Epw_new.place(x = 110, y = 100)

    #取り消しボタン(username)作成
    delete_button1 = tk.Button(newaccount_root, bg = color, text = "取り消し")
    delete_button1.place(x = 350, y = 60)

    delete_button1 ["command"] = delete1


    #取り消しボタン(password)作成
    delete_button2 = tk.Button(newaccount_root, bg = color, text = "取り消し")
    delete_button2.place(x = 350, y = 100)

    delete_button2 ["command"] = delete2

    #送信ボタン作成
    send_button = tk.Button(newaccount_root, bg = color, text = "送信" )
    send_button.pack(fill = "x", padx = 10, pady = 10, side = 'bottom')

    send_button ["command"] = send

    #sqlite3のデータベース（ユーザーデータ）
    #database = "user.db"
    #connect = sqlite3.connect(database)
    #uscu = connect.cursor()
    #username = input("username:")
    #password = input("password:")

    #uscu.execute('insert into userdata (username,password) values(?,?)', (username,password))
    #connect.commit()
    #connect.close()

#忘れた（データベース使用）
def forget():
    forget_root = tk.Tk()
    forget_root.title('アカウント復旧')
    forget_root.geometry("440x200+750+300")
    forget_root.option_add('*font',['MS ゴシック',10])

#usernameの入力取り消し
def delete1():
    Eun.delete(0, tk.END)

#passwordの入力取り消し
def delete2():
    Epw.delete(0, tk.END)


#ウィンドウの作成
root = tk.Tk()
root.title("ユーザー認証  ~var1.3~ (解像度：440*200)")
root.geometry('440x200+750+400')
root.option_add("*font", ["メイリオ",10])

#メニューバーの作成
men = tk.Menu(root)
root.config(menu = men)
menu_file = tk.Menu(root, tearoff = False)
men.add_cascade(label = "メニュー", menu = menu_file)
menu_file.add_command(label = "アカウント新規作成", command = newaccount)
menu_file.add_command(label = "パスワードまたはユーザー名を忘れた方はこちら",command=forget)
menu_file.add_command(label = "終了", command = shutdown)
men.add_cascade(label='ヘルプ',command=help_page)
men.add_cascade(label='アップデート情報',command=details_page)

#ラベルの作成
word = tk.Label(root, text = "ユーザー名とパスワードを入力してください", bg = color)
username = tk.Label(root, text = "ユーザー名:", bg = color)
password = tk.Label(root, text = "パスワード:", bg = color)

word.place(x = 20, y = 20)
username.place(x = 30, y = 65)
password.place(x = 30, y = 100)

#エントリーの作成
Eun = tk.Entry(root, bg = color, width = 25, bd = 5)
Epw = tk.Entry(root, bg = color, width = 25, bd = 5, show = "●")

Eun.place(x = 110, y = 65)
Epw.place(x = 110, y = 100)

#取り消しボタン(username)作成
delete_button1 = tk.Button(root, bg = color, text = "取り消し")
delete_button1.place(x = 350, y = 60)

delete_button1 ["command"] = delete1


#取り消しボタン(password)作成
delete_button2 = tk.Button(root, bg = color, text = "取り消し")
delete_button2.place(x = 350, y = 100)

delete_button2 ["command"] = delete2

#送信ボタン作成
send_button = tk.Button(root, bg = color, text = "送信" )
send_button.pack(fill = "x", padx = 10, pady = 10, side = 'bottom')

send_button ["command"] = send

root.mainloop()