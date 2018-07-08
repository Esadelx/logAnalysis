# logAnalysis
<h2>Udaicty project 3 logs Analysis</h2>

logs data Analysis report of adatabase using logs report using postgresql, pgadmin and Python
 

<h2>The project consist of 3 main functions as following:</h2>

  1-The get_top_articles to get the top 3 articles in number of views.

  2-The get_top_authors to get the authors ordered by the number of the views of their articles.

  3-The get_requests_fail_days to get the days on which the requests lead to more than 1% errors.

<strong>.install Envirnoment </strong>

1-install python 3.7 

2-install postgresql 9.0 9.6 

3-install pgAdmin 4 

The views used in this project:

       "create or replace view error as "
            "select substring(cast(log.time as text), 0, 11) as date, "
            "count(log.status) as error "
            "from log "
            "where log.status like '%404%' "
            "group by date "
            
    "create or replace view  data as "
            "select substring(cast(log.time as text), 0, 11) as date , count(log.status) as all from log "
            "group by date "
            
    "create or replace view query as "
            "select alldata.date, "
            "((dataerror.error / alldata.all::float)*100) as all_error "
            "from alldata "
            "inner join dataerror on alldata.date=dataerror.date "
       
              
. how to run?

1- install postgresql 9.6

2- create a database in pgAdmin4 by the name logsAnlaysis the 3 tables and the view which descriped above download this archieve
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
extract the sql file which contains the statements for creating the tables then execute the create view statement.

3-Create a Super User with granting all privileges 

4- run psql -d logAnalysis -f newsdata.sql

5-Type the command C:\Program Files\PostgreSQL\9.6\bin>psql -U Sully -d LogAnalysis -a -f newsdata.sql

6- run python loganalyis.py
