#!/usr/bin/env python3

import requests
import json
import argparse
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
import sys
# Load environment variables from file
from dotenv import load_dotenv
import os


# Specify the path to your environment file
load_dotenv("/usr/local/bin/.env.leetcode")

# TOKEN AND IDS
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")
# URL
NOTION_BASE_URL = "https://api.notion.com/"
LEETCODE_INFO_URL = "https://lcid.cc/info/"
LEETCODE_URL = "https://leetcode.com/problems/"

urlDatabase = f"{NOTION_BASE_URL}v1/databases/{DATABASE_ID}"
urlQueryPages = f"{NOTION_BASE_URL}v1/databases/{DATABASE_ID}/query"

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


def get_leetcode_info_by_id(id):
    try:
        leetcode_url = f"{LEETCODE_INFO_URL}{id}"
        resInfo = requests.get(leetcode_url, timeout=3)
        resInfo = resInfo.json()
        if "code" in resInfo:
            if resInfo["code"] != 200:
                raise RequestException(resInfo["message"])
            resInfo.raise_for_status()
        return resInfo
    except HTTPError as errh:
        sys.exit(errh)
    except ConnectionError as errc:
        sys.exit(errc)
    except Timeout as errt:
        sys.exit(errt)
    except RequestException as err:
        sys.exit(err)


def is_question_exists(question_id, pages):

    for row in pages:
        props = row["properties"]
        Leetcode_ID = props["Leetcode_ID"]["number"]
        page_id = row["id"]
        if Leetcode_ID == question_id:
            return page_id

    return None


def get_database_data(url, headers):
    response = requests.get(url, headers=headers)
    # print(response.text)
    return response.json()


def update_page(page_id: str, data: dict):
    url = f"https://api.notion.com/v1/pages/{page_id}"

    payload = {"properties": data}

    res = requests.patch(url, json=payload, headers=headers)
    return res


def create_page(data: dict):
    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"type": "database_id",
                          "database_id": DATABASE_ID}, "properties": data}

    res = requests.post(create_url, headers=headers, json=payload)
    # print(res.status_code)
    return res


def present_in_database(leetcode_number):
    """
    If num_pages is None, get all pages, otherwise just the defined number.
    """
    filterProperties = {
        "filter": {
            "property": "Leetcode_ID",
            "number": {
                "equals": leetcode_number
            }
        }
    }
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    response = requests.post(url, json=filterProperties, headers=headers)

    data = response.json()

    # Comment this out to dump all data to a file
    # with open('db.json', 'w', encoding='utf8') as f:
    #     json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]

    if len(results) == 0:
        return None

    return results[0]["id"]


def get_pages(num_pages=None):
    """
    If num_pages is None, get all pages, otherwise just the defined number.
    """

    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    get_all = num_pages is None
    page_size = 100 if get_all else num_pages

    payload = {"page_size": page_size}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    # Comment this out to dump all data to a file
    # with open('db.json', 'w', encoding='utf8') as f:
    #     json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]
    while data["has_more"] and get_all:
        payload = {"page_size": page_size, "start_cursor": data["next_cursor"]}
        url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        results.extend(data["results"])

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Generate leetcode question to fill up Notion for tracking of questions")
    parser.add_argument("leetcode_number", type=int,
                        help="leetcode question number")
    parser.add_argument(
        "comment", nargs="?", default="", help="optional comment for the question"
    )
    args = parser.parse_args()

    leetcode_number_input_by_user = args.leetcode_number
    leetcode_comment_input_by_user = args.comment

    leet_code = get_leetcode_info_by_id(leetcode_number_input_by_user)

    difficulty = leet_code["difficulty"]
    name = leet_code["title"]
    nameForURL = leet_code["titleSlug"]

    page_id = present_in_database(leetcode_number_input_by_user)

    if page_id is not None:
        if leetcode_comment_input_by_user != "":

            updateData = {
                "Leetcode_ID": {
                    "number": leetcode_number_input_by_user
                },
                "Notes": {"rich_text": [{"text": {"content": leetcode_comment_input_by_user}}]},
            }
        else:
            updateData = {
                "Leetcode_ID": {
                    "number": leetcode_number_input_by_user
                },
            }
        update_page(page_id, updateData)
        print(
            f'Question {leetcode_number_input_by_user} updated (Last Done) in the Notion database.')
    else:
        data = {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": name,
                        },

                    }
                ]
            },

            "Difficulty": {
                "select": {
                    "name": difficulty,
                }
            },
            "Link": {
                "url": f"{LEETCODE_URL}{nameForURL}"
            },
            "Leetcode_ID": {
                "number": leetcode_number_input_by_user
            },
            "Notes": {"rich_text": [{"text": {"content": leetcode_comment_input_by_user}}]},
        }

        create_page(data)
        print(
            f'Question {leetcode_number_input_by_user} added to the Notion database.')


if __name__ == '__main__':
    main()
