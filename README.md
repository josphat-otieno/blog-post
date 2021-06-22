# BLOG POST
## This is a python-flask Blog Application where users can see various blogs posted by bloggers and are able to subscribe to recieve notifications on recent posts. The bloggers can sign up for blogging
 
 ## Author
## By **[JOSEPHAT OTIENO](https://github.com/josphat-otieno)**

## User Stories
These are the behaviours/features that the application implements for use by a user and writer.

* User opens the application
* The user sees various blogs posted by bloggers
* The user comments on the blog
* users can subscribe to recieve notifications about new posts
* Blogger/witer logs in into the application
* Sees the comments postes by other users
* The writer deletes comments found offensive
* The writer updates varoius posts
* The writer can delete various posts
* The writers can Upload their profile photos and update thier bio

## Behaviour Driven Development
## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| users loads the application | *On page load* | user sees various posts/blogs posted by bloggers |
| user clicks on comment button | *On  click* | comment page is loaded and user sees various comments and can add more comments |
| user clicks on subscribe button | *on lcick* | subscription page is loaded and user enters details for subscription |
| writer cllicks on sign up | *On page load* | sign up page is loaded and user can sign up to be a blogger |
| writer clicks on crete blog  | *on page load* | user is able to create blog on when the page loads |
| writes clicks on edit post| *edit page is loaded* | user is able to update the blog|
| writer clicks on delete post | *on page load* | the post is deleted |
| writer clicks on delete comment | *on page load* | the comment is deleted|
| writer clicks on profile | *on page load* | the writer add profile adds profile infoemation and uploads a profile photo|

## Prerequisites
* Python3.8

## Setup/Installation Requirements
* Clone [this repository]( https://github.com/josphat-otieno/blog-post.git)  using the following commamnd  in the terminal: `git clone  https://github.com/josphat-otieno/blog-post.git`. 
* Note:<em>You will need to git installed in your machine. You can install using the following comman: `$ sudo apt-get install git.`</em>
* After cloning, navigate to the folder where the repo was cloned and open it with your favorite code editor. 
* Create a vitual environment using the following command `python3 -m venv --without-pip virtual`
* Activate the virtual environment using the following command `source virtual/bin/activate`
* Run thefollowing command  to interact with the application `$python3.8 manage.py server`
* Run tests units using the following command `$python3.8 manage.py test`

## Known Bugs

No known bugs

## Technologies Used
- Python3.8
- Flask
- Heroku

## Contacts
# Tel: +254717878813
Email: josephat.otieno@student.moringaschool.com
