# domdom: a web app on AWS

domdom is a web application that randomly selects an entry from a database, shows it to the user, and allows the user to save their own content to the database, all from a single U.I.

domdom on AWS [http://randomwisdom.eu-west-2.elasticbeanstalk.com/]

This version runs on an AWS EC2 server.

App runs in Flask framework with only 3 dependencies - see requirements.txt

The front-end U.I is built with HTML / CSS and uses Jinja2 templates to display the content.

In the repo you will find:

Front-end:
Index.html
Returns the initially called information
Allows one-click reloading
Contains a form for users’ content

Form.html
An include in index.html with the form attributes

Submitted.html
Posts the form and returns the users’ addition

Large.css
CSS for a viewport above 1024px

Back-end
Appplicatin.py
Launches the HTML templates when instigated

Database
Interacts with the database using MySQL queries via SQL alchemy.

![MIT license](https://badgen.net/badge/license/MIT/blue)
