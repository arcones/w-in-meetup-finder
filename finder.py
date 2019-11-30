#!/usr/bin/env python3.8

import requests
import math
import gender_guesser.detector as gender
from argparse import ArgumentParser

parser = ArgumentParser(description='Get the names of the members of a meetup group')
parser.add_argument('group', help='Name of the group, as it appears in the URL of the platform')

args = parser.parse_args()

# Get the number of members that the group contains

urlGroup = f"https://api.meetup.com/{args.group}?&sign=true&photo-host=public&only=members"

res = requests.get(urlGroup)

members = res.json()['members']

print(f"The {args.group} meetup public group has {members} members")

# Compose the request to get member names with pagination

offsets = math.floor(members/200)
detector = gender.Detector(case_sensitive=False)
women = []

while offsets != -1:
    urlMembers = f"https://api.meetup.com/{args.group}/members?&sign=true&photo-host=public&page=200&offset={offsets}&only=name"
    res = requests.get(urlMembers)
    for json in res.json():
        fullname = json['name']
        name = fullname.split()[0]
        gender = detector.get_gender(name, u'spain')

        if gender not in ["male", "unknown", "andy", "mostly_male"]:
            women.append(fullname)
            print(fullname)

    offsets -= 1

print(f"In the meetup group {args.group}, of a total of {members} members might be {len(women)} women")
