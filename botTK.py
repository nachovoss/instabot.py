#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from instabot_py import InstaBot
from tkinter import *
from PIL import ImageTk, Image


window = Tk()
window.title('Instabot3000 by interface by Nachovoss')
window['bg'] = 'pink'
                                           #adjust path as needed
filename=PhotoImage(file = "C:\\Users\\User\\Desktop\\instabot.py-master\\instalogo.png")

background_label = Label(window, image=filename)
background_label.place(x=80, y=130, width=420, height=420)

window.geometry("1000x800")
window.bg = 'pink'
window.maxsize(width=700, height=600)
window.minsize(width=700, height=600)


#adjust path as needed
window.iconbitmap(r'C:\\Users\\User\\Desktop\\instabot.py-master\\instalogo.ico')

img = ImageTk.PhotoImage(Image.open("instabot3000.png"))
header = Label(window, image = img, height=130, width=600,bg='pink')



def start_bot():

    bot = InstaBot(
        login=entry_1.get(),  # Enter username (lowercase). Do not enter email!
        password=entry_2.get(),
        like_per_day=int(entry_3.get()),
        comments_per_day=int(entry_4.get()),
        tag_list=[entry_5.get(), entry_6.get(), entry_7.get(), entry_8.get()],
        tag_blacklist=["rain", "thunderstorm"],
        user_blacklist={},
        max_like_for_one_tag=50,
        follow_per_day=int(entry_9.get()),
        follow_time=1 * 60 * 60,
        unfollow_per_day=int(entry_x.get()),
        unlike_per_day=0,
        unfollow_recent_feed=True,
        # If True, the bot will also unfollow people who dont follow you using the recent feed. Default: True
        time_till_unlike=3 * 24 * 60 * 60,  # 3 days
        unfollow_break_min=15,
        unfollow_break_max=30,
        user_max_follow=0,
        # session_file=False, # Set to False to disable persistent session, or specify custom session_file (ie ='myusername.session')
        user_min_follow=0,
        log_mod=0,
        proxy="",
        # List of list of words, each of which will be used to generate comment
        # For example: "This shot feels wow!"
        comment_list=[
            ["this", "the", "your"],
            ["photo", "picture", "pic", "shot"],
            ["is", "looks", "is 👉", "is really"],
            [
                "great",
                "super",
                "good",
                "very good",
                "good",
                "wow",
                "WOW",
                "cool",
                "GREAT",
                "magnificent",
                "magical",
                "very cool",
                "stylish",
                "beautiful",
                "so beautiful",
                "so stylish",
                "so professional",
                "lovely",
                "so lovely",
                "very lovely",
                "glorious",
                "so glorious",
                "very glorious",
                "adorable",
                "excellent",
                "amazing",
            ],
            [".", "🙌", "... 👏", "!", "! 😍", "😎"],
        ],
        # Use unwanted_username_list to block usernames containing a string
        # Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
        # 'free_followers' will be blocked because it contains 'free'
        unwanted_username_list=[
            "second",
            "stuff",
            "art",
            "project",
            "love",
            "life",
            "food",
            "blog",
            "free",
            "keren",
            "photo",
            "graphy",
            "indo",
            "travel",
            "art",
            "shop",
            "store",
            "sex",
            "toko",
            "jual",
            "online",
            "murah",
            "jam",
            "kaos",
            "case",
            "baju",
            "fashion",
            "corp",
            "tas",
            "butik",
            "grosir",
            "karpet",
            "sosis",
            "salon",
            "skin",
            "care",
            "cloth",
            "tech",
            "rental",
            "kamera",
            "beauty",
            "express",
            "kredit",
            "collection",
            "impor",
            "preloved",
            "follow",
            "follower",
            "gain",
            ".id",
            "_id",
            "bags",
        ],
        unfollow_whitelist=["example_user_1", "example_user_2"],
        # Enable the following to schedule the bot. Uses 24H
        # end_at_h = 23, # Hour you want the bot to stop
        # end_at_m = 30, # Minute you want the bot stop, in this example 23:30
        # start_at_h = 9, # Hour you want the bot to start
        # start_at_m = 10, # Minute you want the bot to start, in this example 9:10 (am).
    )

    bot.mainloop()


label_1=Label(window,text='Username:',fg='blue')
label_2=Label(window,text='Password:',fg='blue')
label_3=Label(window,text='Nº of likes a day:(max1000)',fg='blue')
label_4=Label(window,text='Nº of comments(max100):',fg='blue')
label_5=Label(window,text='Hashtag Nº1',fg='blue')
label_6=Label(window,text='Hashtag Nº2:',fg='blue')
label_7=Label(window,text='Hashtag Nº3:',fg='blue')
label_8=Label(window,text='Hashtag Nº4:' ,fg='blue')
label_9=Label(window,text='Nº of Follows/day:(max600)',fg='blue')
label_x=Label(window,text='Nº of Unfollows/day:(max600)',fg='blue')


entry_1 = Entry(window)
entry_2 = Entry(window, show='*')
entry_3 = Entry(window)
entry_4 = Entry(window)
entry_5 = Entry(window)
entry_6 = Entry(window)
entry_7 = Entry(window)
entry_8 = Entry(window)
entry_9 = Entry(window)
entry_x = Entry(window)


button_1=Button(window,text='Start bot',command=start_bot, height = 3, width = 15,bg='pink', fg='blue')

label_1.place(x=555, y=140)
label_2.place(x=555, y=180)
label_3.place(x=525, y=220)
label_4.place(x=525, y=260)
label_5.place(x=555, y=300)
label_6.place(x=555, y=340)
label_7.place(x=555, y=380)
label_8.place(x=555, y=420)
label_9.place(x=520, y=460)
label_x.place(x=520, y=500)

header.place(x=1, y=1)

entry_1.place(x=555, y=160, width=100)
entry_2.place(x=555, y=200, width=100)
entry_3.place(x=555, y=240, width=100)
entry_4.place(x=555, y=280, width=100)
entry_5.place(x=555, y=320, width=100)
entry_6.place(x=555, y=360, width=100)
entry_7.place(x=555, y=400, width=100)
entry_8.place(x=555, y=440, width=100)
entry_9.place(x=555, y=480, width=100)
entry_x.place(x=555, y=520, width=100)

button_1.place(x=555, y=540)



window.mainloop()

