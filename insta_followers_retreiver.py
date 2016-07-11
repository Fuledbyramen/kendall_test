import requests
import re
import schedule
import time
import datetime
import sqlite3

conn = sqlite3.connect('daily_follower.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS Follower_Reporter(username TEXT, followers REAL, datestamp TEXT, unix REAL)')

def get_followers():
    accounts = ["ventura_vixens", "kendall_morris", "zach.chao"]
    follower_count = []
    for account in accounts:
        account_url = requests.get("http://instagram.com/{}".format(account))
        followed_by = int(re.search(r"\"followed\_by\"\: \{\"count\"\: ([0-9]+)", account_url.text).group(1))
        now = datetime.datetime.now()
        date = ("%s/%s/%s" % (now.day, now.month, now.year))
        follower_count.append((account, followed_by, date))
        print(account + " tracked and added. Waiting 2 seconds.")
        time.sleep(2)
        c.execute("INSERT INTO Follower_Reporter (username, followers, datestamp, unix) VALUES (?, ?, ?, ?)", (account, followed_by, date, time.time()))
    print(follower_count)
    conn.commit()



schedule.every().day.at("12:00").do(get_followers)
while True:
    schedule.run_pending()
    time.sleep(50)

#get_followers()
