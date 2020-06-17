#!/usr/bin/env python3

import time
import requests
import threading
import queue

WORD = "trump"

NEWS_API_KEY = "bbf81cf8eaee407c884c612e26187a98"

base_url = 'https://newsapi.org/v1/'


def get_sources():
    """
    Get all the English language sources of news
    'https://newsapi.org/v1/sources?language=en'
    """
    url = base_url + "sources"
    params = {"language": "en"}
    resp = requests.get(url, params=params)
    data = resp.json()
    sources = [src['id'].strip() for src in data['sources']]
    print("all the sources:")
    print(sources)
    return sources


def get_articles(source):
    """
    https://newsapi.org/v1/articles?
    """
    url = base_url + "articles"
    params = {"source": source,
              "apiKey": NEWS_API_KEY,
              "sortBy": "top",
              }
    print("requesting:", source)
    resp = requests.get(url, params=params)
    if resp.status_code != 200:
        print("something went wrong with {}".format(source))
        print(resp)
        print(resp.text)
        return []
    data = resp.json()
    # the url to the article itself is in data['articles'][i]['url']
    titles = [str(art['title']) + str(art['description']) for art in data['articles']]
    return titles


def count_word(word, titles):
    word = word.lower()
    titles = [x.lower() for x in titles[0]]
    count = 0
    for title in titles:
        if word in title:
            count += 1
    return count


def create_buckets(lst, n):
    return [lst[i::n] for i in range(n)]


def get_articles_threads(sources, thread_count = 2):
    threads = []
    results = queue.Queue()
    jobs = create_buckets(sources, thread_count)
    #print(jobs)

    def thread_tender(*args):
        for j in job:
            print(threading.currentThread().getName())
            results.put(get_articles(j))

    for i in range(thread_count):
        job = jobs[i]
        thread = threading.Thread(target=thread_tender, args=(job))
        thread.start()
        threads.append(thread)
        print("Thread {} started.".format(thread.name))

    for i in range(thread_count):
        threads[i].join()
    print("Thread join complete.")

    return [results.get() for i in range(thread_count)]


if __name__ == '__main__':
    start = time.time()
    sources = get_sources()

    art_count = 0
    word_count = 0
    titles = get_articles_threads(sources)
    print(titles)
    art_count += len(titles)
    word_count += count_word(WORD, titles)

    print(WORD, "found {} times in {} articles".format(word_count, art_count))
    print("Process took {:.0f} seconds".format(time.time() - start))
