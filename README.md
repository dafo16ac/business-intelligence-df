<h1 align="center"> Web Application </h1>
<h2 align="center"> Market Segmentation Dashboard </h2>

# OBS: work in progress
This is the source code of the [web application](https://business-intelligence-davide.herokuapp.com/) I developed to ***showcase*** my dexterity with data science and data engineering practices, such as clustering, production deployment of web appliations, and friendly GUIs.

The structure of the present repository follows best practices as much as the libraries used allow bug-free code (e.g. dash). It is as follows:


```{r test-python, engine='python'}
📁 business-intelligence-df-2.2
 |_ 📃 app.py
 |_ 📃 settings.py
 |_ 📃 requirements.txt
 |_ 📁 assets
     |_	📃 app_layout.css
     |_	📃 favicon.ico
     |_	📃 graph_layouts.py
 |_ 📁 data
     |_	📃 XXXX
```

### 📁 assets 

The preceding clustering technique has been further explained in a separate notebook (TBD).

For an overview of projects in my *Portfolio*, please follow this [link](https://github.com/dafo16ac/df_portfolio).

Some details on each script

App.py: it is instead of main.py. this is the main dash application running on Flask. Written in python, it also includes callbakcs for the dynamic aspects of the web application.
Settings: settings of the app, useful to easily switch whether you are working locally or deploying in production. It also includes the code for the PostgreSQL engine, if preferred as alternative. Worth to be noted, the debug variable is important to be set to false once in production, due to security concerns.

Data. This is quite large. Since every characteristic is demanding in terms of code in order to present different aspects of the XXXX
Generation of the variables needed in order to be presented in the application. Those could also be improved in terms of code efficiency by refactoring how variables are generated, through loops.
I decided to split XXXX
Graphs are also generated here
These will be fetched by the main app.py. similar structure is then used in the callbacks. Moreover, there is the processed dataset with all the customer records.

Classes for tables: OOP for simplifying the generation of the tables, recurrent themes in the app. Similar technique could be implemented for other charts, allowing further shrinkage of the code length. 

Assets: favicon and CSS style of the webapp.
