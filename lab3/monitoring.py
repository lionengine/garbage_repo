import requests
import json
import logging
import time
import threading

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def run():
    main("http://localhost:8000/health")

def main(url):
    try:
        r = requests.get(url)
        data = json.loads(r.content)
        logging.info("Сервер доступний. Час на сервері: %s", data['date'])
        logging.info("Запитувана сторінка: : %s", data['current_page'])
        logging.info("Відповідь сервера місти наступні поля:")
        for key in data.keys():
            logging.info("Ключ: %s, Значення: %s", key, data[key])
        print("Everything works fine. Getting ready to the next take-off...")
    except:
        print("SORRY. But we've got an error. Try to launch server and try again. I don't care...")
        logging.error("Can't connect to the server")
        logging.warning("Can't connect to the server")

    
    while True:
        time.sleep(60)
        run();

if __name__ == '__main__':
    run()
