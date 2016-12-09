Elastic search with Django and React
************************************

Steps to have the setup working:
#. Download and extract elastic search tar file. 
#. Install all necessary npm packages
#. Create virtualenv and install requirements


*. Go to : https://www.elastic.co/downloads/elasticsearch and download the correct version. 
*. Extract the .tar file to a folder named elasticsearch.
*. Run `./elasticsearch/bin/elasticsearch` and the elasticsearch server will be running. 
*. Run `npm install` in order to install all necessary packages
*. Run `./node_modules/.bin/webpack -d --watch` if you want to compile any changes in file *index.js*. 
*. `pip install -r requirements.txt` for the python environment packages to be installed. 
*. Run Django Server and bob is your uncle