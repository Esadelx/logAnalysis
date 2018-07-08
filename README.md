# logAnalysis
Udaicty project 3 logs Analysis
logsdata Analysis report of adatabase using logs report using postgresql and pgadmin and Python
install Envirnoment 
.install python 3.7 
.install postgresql 9.0 9.6 
.install pgAdmin 4 
.install python libs needed 

create view in postgreql 

CREATE OR REPLACE VIEW articlesv AS
       (SELECT slug as id, COUNT(path) AS views
       FROM articles
       LEFT JOIN log ON slug = substring(path from 10)
       GROUP BY slug);
       
              
 #How to run the project?

1- install postgres

2- create a database in pgAdmin4 by the name logsAnlaysis the 3 tables and the view which descriped above download this archieve
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
extract the sql file which contains the statements for creating the tables then execute the create view statement.

3-Create a Super User with granting all privileges 

4- run psql -d logAnalysis -f newsdata.sql

5-Type the command C:\Program Files\PostgreSQL\9.6\bin>psql -U postgres -d LogAnalysis -a -f newsdata.sql

6- run python loganalyiss.py
