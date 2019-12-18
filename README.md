# women-in-meetup-finder

Tool to query for female members of public meetup groups.
It uses gender-guesser library to guess if the member is female, so the guess is not perfect but close enough.

## Requirements: pip3 & python3

Install the requirements with pip3:

`pip3 install --user -r requirements.txt`

Run it with python3 providing the name of the public meetup group (as it appears in meetup URLs) as parameter, like in the following example:

`python3 finder.py <NameOfThePublicMeetupGroupHere>`

Like in the following example:

`python3 finder.py Madrid-HashiCorp-User-Group`

## Background

As an organizer of Women in DevOps Madrid meetup group, I have used this application to query for female members of similar groups so I can make them aware of the existence of my meetup group.
