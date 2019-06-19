#!/usr/bin/python3
"""
Date Updated: 2019-06-19
Author: James Campbell
What: Loads CNN.com using mechanize and saves all the links to assets/cnn.txt
"""
import mechanize

base_url = "http://www.cnn.com"
title = "cnn"


def crawl(site):
    seed_url = site
    br = mechanize.Browser()

    br.set_handle_robots(False)
    br.set_handle_equiv(False)

    br.open(seed_url)

    link_bank = []

    for link in br.links():
        if link.url[0:4] == "http":
            link_bank.append(link.url)
        if link.url[0] == "/":
            url = link.url
            if url.find(".com") == -1:
                if url.find(".org") == -1:
                    link_bank.append(base_url + link.url)
                else:
                    link_bank.append(link.url)
            else:
                link_bank.append(link.url)

        if link.url[0] == "#":
            link_bank.append(base_url + link.url)

    link_bank = list(set(link_bank))
    my_file = open(f"./assets/{title}.txt", "w")
    for link in link_bank:
        my_file.write(link + "\n")
    my_file.close()
    return link_bank


crawl(base_url)
