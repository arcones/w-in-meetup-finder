#!/usr/bin/env python3

import requests
import math
import gender_guesser.detector as gender
from argparse import ArgumentParser
from jsonpath_rw import jsonpath, parse

parser = ArgumentParser()
parser.add_argument('group', help='Name of the group, as it appears in the URL of meetup')
parser.add_argument('eventID', help='ID of the event, as it appears in the URL of meetup')

args = parser.parse_args()

# Get the name of the people attending the event

url_event = f"https://api.meetup.com/{args.group}/events/{args.eventID}/rsvps?&sign=true&photo-host=public"
res = requests.get(url_event).json()
attendees = []
for item in res:
    attendees.append(item['member']['name'])


# Iterate over the name of the attendees to get the females

detector = gender.Detector(case_sensitive=False)
women = []
for fullName in attendees:
    name = fullName.split()[0]
    gender = detector.get_gender(name, u'spain')

    if gender not in ["male", "unknown", "andy", "mostly_male"]: ## Just removed andy as results of this gender seem not to be very accurate
        women.append(fullName)

# Print the results

print(f"In the event {args.eventID} of the meetup group {args.group}, of a total of {len(attendees)} attendees might be {len(women)} women")
print(f"Women represent the {'%.1f'%((len(women)/len(attendees))*100)}% of the attendance")
