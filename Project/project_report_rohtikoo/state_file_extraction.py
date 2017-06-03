import sqlite3 as sqlite
import pandas as pd

# Python Script used to extract the records of Michigan from the StateNames table .The records saved in MichiganStateNames_all.csv and used as data set two.

def main():

    with sqlite.connect(r'database.sqlite') as con:
        cur = con.cursor()
        #cur.execute("SELECT * from StateNames")
        #for row in cur.execute('SELECT * FROM StateNames'):
         #print row
        state=[]
        mi_name=[]
        out=[]

        #cur.execute("SELECT Name from StateNames where  State='MI'and Year >2003 order by Count desc")#sorted list of female names in Michigan as per count
        #state = cur.fetchall()

        f = open('MichiganStateNames_all.csv','wb')  # https://www.experts-exchange.com/questions/28134882/Python-SQL-Query-Results-to-CSV-file.html
        cur.execute("SELECT * from StateNames where  State='MI'order by Count desc")
        while True:
            #      # Read the data
            df = pd.DataFrame(cur.fetchmany())
            # We are done if there are no data
            if len(df) == 0:
                break
                #      # Let's write to the file
            else:
                df.to_csv(f, header=False)


if __name__ == '__main__':
    main()