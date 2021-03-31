import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *


HOMEPAGE = 'https://www.majestylink.com'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = DOMAIN_NAME + '/queue.txt'
CRAWLED_FILE = DOMAIN_NAME + '/crawled.txt'
NUMBER_Of_THREADS = 20
queue = Queue()

Spider(DOMAIN_NAME, HOMEPAGE, DOMAIN_NAME)

# Each worker threads (will die when main exits)


def create_workers():
    for _ in range(NUMBER_Of_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# Do the next job in the queue


def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items in the queue, if so crawle them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


create_workers()
crawl()
