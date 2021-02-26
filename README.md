# TestTaskJooble

<h3>Test task for Python Developer vacancy in Jooble</h3>

For launching this project on your device you should follow next commands:
  
  - Create a directory for this project: $ mkdir project
  - go to this folder: $ cd project
  - initialize git: $ git init
  - connect the remote repository: $ git remote add origin https://github.com/AlexUv2/TestTaskJooble.git 
  - download it using pull command: $ git pull https://github.com/AlexUv2/TestTaskJooble.git master
  
  After successful downloading it from git you should initialize virtual environment and install Flask.

  - check if you have python using: $ python3 --version; if not: $sudo apt install python3.8
  - then install pipenv: $sudo apt install pipenv
  - activate virtual enviroment: $ pipenv shell
  - install Flask: $ pipenv install flask
  - install Flask-SQLAlchemy: $ pipenv install flask-sqlalchemy
  - install Flask-RESTfulI:  $ pipenv install flask_restful
  
  <h4>For starting App without API</h4> 
    - $python3 links.py
  <h4>For starting App with API</h4> 
    - $python3 linksApi.py
    
    
   <h4> Follow http://127.0.0.1:5000/ </h4>
    
    
<h3>App Description</h3>

  This app shorts the links. You should enter the link and its lifetime, after submitting you will be redirected to the list of links where the last is at the top.
  Links are available only while app is running.
  Links has 5 symbols, this is enough for about 15 million unique links.
  Created using Python and Flask.

  
<h3>API Description</h3>

<table>
 <tr>
     <th>Method HTTP</th><th>Action</th><th>Example</th>
 </tr>
 
 <tr><td>[GET]</td><td>Get information about definie object</td><td>http://127.0.0.1:5000/links/api/1 </td></tr>
 <tr><td>[GET]</td><td>Get information about all objects</td><td>http://127.0.0.1:5000/links/api </td></tr>
 <tr><td>[POST]</td><td> Create new object</td><td>http://127.0.0.1:5000/links/api</td></tr>
 <tr><td>[PUT]</td><td>Change definite object</td><td>http://127.0.0.1:5000/links/api/1 </td></tr>
 <tr><td>[PATCH]</td><td> Change certain fields of definite object</td><td>http://127.0.0.1:5000/links/api/1 </td></tr>
 <tr><td>[DELETE]</td><td>Delete definite object</td><td>http://127.0.0.1:5000/links/api/1 </td></tr>

</table>

  For using app with API, run linksApi.py.
  
  


  
