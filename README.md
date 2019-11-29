# WinDO-finder

Tool to query for female members of public meetup groups.
It uses gender-guesser library to guess if the member is female, so the guess is not perfect but close enough.

Install the requirements with pip3:

`pip3 install --user -r requirements.txt`

Run it with python3 providing the name of the public meetup group (as it appears in meetup URLs) as parameter, like in the following example:

`python3 finder <NameOfThePublicMeetupGroupHere>`

Like in the following example:

`python3 finder Madrid-HashiCorp-User-Group`
