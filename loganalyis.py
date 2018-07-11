#!/usr/bin/env python3

# connect to the database

import psycopg2

conn = psycopg2.connect("dbname=logAnalysis user=Sully"
                        " password=1234 host=localhost")
cursor = conn.cursor()


def get_articles():
    # function the top three Authors
    cursor.execute('''select authors.name,
                      count(*) as num_view
                      from  authors
                      inner join articles
                      on authors.id=articles.author
                      inner join log on
                      log.path = concat('/article/', articles.slug)
                      where log.status ='200 OK'
                      group by authors.name
                      order by num_view desc
                      limit 3'''
                   )
    return cursor.fetchall()
    conn.commit()


def get_authors():
    # function the top three Authors
    cursor.execute('''select authors.name ,
                      count(*) as num_view
                      from  authors
                      inner join articles
                      on authors.id=articles.author
                      inner join log on
                      log.path = concat('/article/', articles.slug)
                      where log.status ='200 OK'
                      group by authors.name
                      order by num_view desc
                      limit 3'''
                   )
    return cursor.fetchall()
    conn.commit()


def get_days():

    cursor.execute('''create or replace view dataerror as
                      select substring(cast(log.time as text), 0, 11)
                      as date,
                      count(log.status) as error
                      from log
                      where log.status like '%404%'
                      group by date '''
                   )
    cursor.execute('''create or replace view  alldata as
                select substring(cast(log.time as text), 0, 11)
                as date ,
                count(log.status) as all from log
                group by date '''
                   )
    cursor.execute('''create or replace view final_query as
                select alldata.date,
                ((dataerror.error / alldata.all::float)*100) as
                all_error
                from alldata
                inner join dataerror on alldata.date=dataerror.date '''
                   )

    cursor.execute(''' select date,
                all_error
                from final_query
                where all_error>1'''
                   )
    return cursor.fetchall()
    conn.commit()


def close_conn():

    # Function to close the connection to the database

    if cursor:
        cursor.close()
    if conn:
        conn.close()


def print_table(x):

    # Function to format the query result table that takes the function

    # which do the query as a parameter

    if x == get_articles:
        count_type = ' views'
        print('THE TOP THREE ARTICLES ARE:')
    elif x == get_authors:
        count_type = ' views'
        print('THE TOP Three AUTHORS :')
    else:
        count_type = '% errors'
        print('THE DAYS WHICH HAVE MORE THEN 1% PERCENTAGE ERRORS:')
    rows = x()
    for row in rows:
        print("%s - %s%s" % (str(row[0]), str(row[1]), count_type))
    print()


if __name__ == '__main__':
    print_table(get_articles)
    print_table(get_authors)
    print_table(get_days)
    close_conn()
