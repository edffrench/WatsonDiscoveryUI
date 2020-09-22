# WatsonDiscoveryUI

To run the application just cd into the directory in the terminal, pip install requirmentas and use the command python3 run.py 

.

the package is structured as follows

static contains all the static files such as javascript and css. the only javascript file you may want to look at is MAIN.JS, 
you can avoid using the rest of it.

templates holds all the html files. Public are html files you would expect regualr users to view whilst, admin refers to the html
you would want only admins to view.

json contains the api credentials 

and the file that contains the flask server is in views.py, this shows you all the server side. This interacts with the Watson Services API.

the files i suggest altering are the templates, main.js, views.py. the rest are optional, would avoid altering app.js and particles.js
