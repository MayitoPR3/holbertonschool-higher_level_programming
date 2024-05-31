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
            print("Title: ", post['title'])
        else:
            print("Error: ", response.status_code)


def fetch_and_save_posts():
    """defines fetch and save"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        keys = []
        keys = {
            'id': posts['id'],
            'title': posts['title'],
            'body': posts['body']
        }
        keys.append(keys)

        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for post in posts:
                writer.writerow(post)
            else:
                print("Error: ", response.status_code)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
