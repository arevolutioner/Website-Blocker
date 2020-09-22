# MAC and LINUX: /etc/hosts
# WINDOWS: C:\Windows\System32\drivers\etc
import time
from datetime import datetime as dt


# host_temp = "hosts"
hosts_file = "/etc/hosts"
redirecting = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.instagram.com", "instagram.com", "www.dnevnik.bg",
                "www.sportal.bg"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Working hour")
        with open(hosts_file, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirecting + " " + website + "\n")

    else:
        with open(hosts_file, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours")

    time.sleep(5)

