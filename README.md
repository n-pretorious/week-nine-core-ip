# Instagram Clone

## Core Features

* An admin can upload new profiles, photos and comments through an admin panel
* An admin can update the said above model details
* A user can register and setup a profile
* A user can view their profile to see their information
* A user can search for other users
* A user can follow and unfollow other users
* A user can view images of people they have followed on their timeline
* A user can view a post's details

## Prerequisites

* Python3
* Django
* Postgres

## Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/{{ USERNAME }}/{{ project_name }}.git
    $ cd {{ project_name }}
    

## Usage

On your favorite editor...

### Activate the virtualenv for your project

    $ python3 -m venv --without-pip virtual
    $ source virtual/bin/activate

Download the latest version of pip in virtual our environment

    $ curl https://bootstrap.pypa.io/get-pip.py | python

Install project dependencies:

    $ pip install -r requirements.txt

## Environment variables

The `ENVIRONMENT` variable loads the correct settings.

``` 
CLOUD_NAME=''
API_KEY=''
API_SECRET=''
SECRET_KEY=''
DEBUG=bolean
DB_NAME='instclone'
DB_USER=''
DB_PASSWORD=''
DB_HOST=''
MODE=''
ALLOWED_HOSTS='*'
DISABLE_COLLECTSTATIC='' 
```

Then simply apply the migrations:

    $ python manage.py migrateÏ

You can now run the development server:

    $ python manage.py runserver

## BDD

| BEHAVIOUR    | INPUT   |  OUTPUT |
| :------------- | :------------- | :--------------- |
| Follow a user | Click follow button in profile | Follow button toggles to unfollow|
| Unfollow a user | Click unfollow button in profile | Unfollow button toggles to follow|
| Search a user |  Username | A modal view appears with a link as user's profile picture, username and name that leads to user's profile |
| Explore search result | Click on a particular search result  | Redirect to a user's profile |
| Explore a post in user's profile | Click on a particilar post | See the post on modal view |
| Like a post | Click on like button | Button turns blue and likes increase by 1 |
| Unlike a post | Click on like button | Button turns black and likes decreas by 1 |
| Comment on a post | Enter comment in comment section and click post button | Comment appears on the comment's section |

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Copyright (c) 2020 Pretorious Ndung'u
