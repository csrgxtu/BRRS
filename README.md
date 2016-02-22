# BRRS
Recommendation system for beautifulreading's books and users

# Usage
first, install all python dependencies
```bash
sudo pip install unicodecsv jieba whoosh flask pymongo
```
second, get book data and index it
```bash
cd tool
./RetrieveBookData.py 0 1000 ../data/1k.csv
mkdir ../data/1kindexdir
./Indexer.py ../data/1k.csv ../data/1kindexdir
```
third, start the python http server
```bash
cd ../src
./FlaskServer.py
```
finally, in the browser, go to http://ip:5000
