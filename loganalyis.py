#module to connect to the database
import psycopg2
#connect todatabase user=postgres password=1234
db = psycopg2.connect("dbname=logAnalysis")
cursor = db.cursor()

#function 1 to get the top 3 articles in view
def first_question():
    #first qusetion function to view the top 3 articles
    sqlstmt = '''SELECT title, views
                FROM articles, articlesv
                WHERE articles.slug = articlesv.id
                ORDER BY views DESC
                LIMIT 3;'''
    cursor.execute(sqlstmt)
    return cursor.fetchall()

def second_question():
    #function 2 to get the authors order by view articles
    sqlstmt = '''SELECT authors.name, SUM(views) AS views
                 FROM articlesv, authors
                 LEFT JOIN articles ON authors.id = articles.author
                 WHERE articles.slug = articlesv.id
                 GROUP BY author,authors.name
                 ORDER BY views DESC;'''
    cursor.execute(sqlstmt)
    return cursor.fetchall()

def third_question():
    #function 3 the logs more than 1%
    sqlstmt = '''SELECT to_char(DATE(time),'FMMonth DD, YYYY'),
                 ROUND(
                 (COUNT(CASE WHEN status LIKE'4%'THEN 1 ELSE NULL END)::NUMERIC /
                 count(*)::NUMERIC)*100,
                 2)AS percentage
                 FROM log
                 GROUP BY DATE(time)
                 HAVING percentage > 1;'''
    cursor.execute(sqlstmt)
    return cursor.fetchall()
def close_connection():
    #close the connection
    if cursor:
        cursor.close()
    if db:
        db.close()


#function 4 appera the queryresult table that take the finction as a parameter
def print_thetable(x):
    if x == first_question:
        count_type= 'views'
        print( "THE TOP THREE ARTICLES ARE : ")
    elif x == second_question:
        count_type= 'views'
        print ("THE TOP AUTHORS : ")
    else:
        count_type = '%errors'
        print("THE DAYS WHICH HAVE MORE THEN 1% PERCENTAGE ERRORS: ")
        rows = x()
        
    for row in rows:
            print("%s - %s%s" % (str(row[0]),str(row[1]),count_type))
    print ()
if __name__ == '__main__':
    # the first query in the database
    print_thetable(first_question)
    print_thetable(second_question)
    print_thetable(third_question)
    close_connection()
    
    

                




    
