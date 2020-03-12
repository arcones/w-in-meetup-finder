# windo-finder

CLI to check the number & relative percentage of women in meetup public groups or in events of those groups.

## Background
As an organizer of Women in DevOps and HashiCorp Users Madrid meetup groups, I originally created this application to query for female members of similar groups so I can make my groups more diverse inviting them to join.

Later on, I used it also to check for female attendees of specific events I hosted, so we can measure the diversity of the attendance.

It uses gender-guesser library to guess if the member is female, so the guess is not perfect but close enough.

## Requirements: pip3 & python3

## Usage

Install the requirements with pip3:

`pip3 install --user -r requirements.txt`

### Meetup public group query

```
# The name of the meetup group should be taken directly from meetup URL
python3 finderInGroup.py <NameOfThePublicMeetupGroup>
```

Like in the following example:

`python3 finderInGroup.py Madrid-HashiCorp-User-Group`

That, as of 2020-03-12 gives these results:

> In the meetup group Madrid-HashiCorp-User-Group, of a total of 351 members might be 21 women
> Women represent the 6.0% of the participants of the Madrid-HashiCorp-User-Group
> See more info in Madrid-HashiCorp-User-Group.txt file

### Meetup public group's event query

```
# The name and the ID of the event should be taken directly from meetup URL
python3 finderInEvent.py <NameOfThePublicMeetupGroup> <IDOfTheEvent> 
```

Like in the following example:

`python3 finderInEvent.py Madrid-HashiCorp-User-Group 267246665`

That, gives these results:

> In the event 267246665 of the meetup group Madrid-HashiCorp-User-Group, of a total of 43 attendees might be 1 women
> Women represent the 2.3% of the attendance

## Roadmap
- In case gender guess fails with the name, the picture of the members/attendees is checked
- To plot the results in a Grafana pannel
