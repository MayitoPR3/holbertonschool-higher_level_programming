#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    """defines fetch and print"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code: ", response.status_code)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(posts[int])


def fetch_and_save_posts():
    """defines fetch and save"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        keys = ['id', 'title', 'body']
        with open('posts.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            for post in posts:
                writer.writerow({key: post[key] for key in keys})
