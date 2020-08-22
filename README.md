<h1 align="center"> Web Application </h1>
<h2 align="center"> Market Segmentation Dashboard </h2>

This is the source code I developed to ***showcase*** my dexterity with Data Science and Data Engineering practices, such as clustering, production deployment of web applications, and friendly GUIs. In fact, I deployed it as [web application](https://business-intelligence-davide.herokuapp.com/) on Heroku.

The structure of the present repository follows best practices as long as the libraries used allow bug-free code (e.g. dash).

### 📃 app.py
This is the main dash application running on Flask. It also includes callbakcs for the dynamic features of the web application.

### 📃 settings.py
settings of the app, useful to easily switch whether you are working locally or deploying in production. It also includes the code for the PostgreSQL engine, if preferred as alternative. Worth to be noted, the debug variable is important to be set to false once in production, due to security concerns.

### 📁 data
Generation of the variables needed in order to visualize different characteristics of the cusotmers in the application. Those could also be improved in terms of code efficiency by refactoring how variables are generated, through loops.
Each script collects all the graphs that pertain to the same characteristic. Static graphs that appear once the webapp is launched are generated in these scripts.
These will be fetched by the main app.py. A similar structure is then used in the callbacks. Moreover, there is the processed dataset with all the customer records.

### 📁 assets
Favicon and CSS style of the webapp.
Classes for tables: OOP for simplifying the generation of the tables, recurrent themes in the app. Similar technique could be implemented for other charts, allowing further shrinkage of the code length. 


### 📃 requirements.txt

### Last notes
The preceding clustering technique has been further explained in a separate notebook (TBD).

For an overview of projects in my *Portfolio*, please follow this [link](https://github.com/dafo16ac/df_portfolio).
