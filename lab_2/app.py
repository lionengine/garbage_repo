# This program is edited by @altersights

import requests
import time

def main(url=''):
    if not url:
        print("No URL passed to function\n")
        return False

    r = requests.get(url=url)
    d = r.json()
    
    if "time" in d.keys():
        print("Time is: ", d['time'])
    try:
        print("Date is: ", d['date'], "\n")
    except KeyError:
        print("No date in response!!!")
        raise KeyError
    
    home_work(d['time'])
    return True


def home_work(t):
    "DateTime Function"
    
    if "AM" in t:
        print("*" * 26)
        print("*\t Доброго дня!\t *")
        print("*" * 26)
        return "am"
    elif "PM" in t:
        print("*" * 35)
        print("*\t Доброго вечора/ночі\t *")
        print("*" * 35)
        return "pm"
    else:
        print("Нимагу візначіть время суток")
        return 0

if __name__ == "__main__":
    a = "="*40
    print(a + "\nРезультат без параметрів: \n" + a + "\n")
    main()
    print(a + "\nРезультат з правильною URL: \n" + a + "\n")
    main('http://date.jsontest.com/')
