

import sqlite3 as sqlite
import csv
import pandas as pd


def main():

# read state level names from Sqlite3 db
# read the national level names from csv file
# find the frequency of each name
# 1.at state level for boys - Michigan : found to be "Emma"
# 2.at state level for girls - Michigan :found to be "Jacob"
# 3.at national level for boys -found to be Jacob
# 4. at national level for girls - found to be Emily
#Arrange each of the above in descending order of frequency  to find the most  in frequent (most popular name)
#print those names.
# Plot graph of the most frequent boy name in the recent ten years at the national level i.e from 2004 to 2014

    with sqlite.connect(r'database.sqlite') as con:
        cur = con.cursor()
        #cur.execute("SELECT * from StateNames")
        #for row in cur.execute('SELECT * FROM StateNames'):
         #print row
        state=[]
        mi_name=[]
        out=[]

        #generate full file of national names popular females in descending order of count
        cur.execute("SELECT Name from NationalNames where Gender='F'and Year >2003 order by Count desc")
        nat_ppl = cur.fetchall()
        print nat_ppl[0]



        f = open('NationalNames_popular.csv','w')  # https://www.experts-exchange.com/questions/28134882/Python-SQL-Query-Results-to-CSV-file.html
        cur.execute("SELECT Count ,Name,Gender,Year from NationalNames where Name=? AND Gender='F'and Year >2003 order by Year asc",nat_ppl[0])
        while True:
              # Read the data
              df = pd.DataFrame(cur.fetchmany())
              # We are done if there are no data
              if len(df) == 0:
                  break
              # Let's write to the file
              else:
                  df.to_csv(f, header=False)

        cur.execute("SELECT Name from NationalNames where Gender='M'and Year >2003 order by Count desc")
        nat_boy = cur.fetchall()
        print nat_boy[0]

         #https://www.experts-exchange.com/questions/28134882/Python-SQL-Query-Results-to-CSV-file.html
        cur.execute("SELECT Count ,Name,Gender,Year from NationalNames where Name=? AND Gender='M'and Year >2003 order by Year asc",nat_boy[0])
        while True:
            #      # Read the data
            df = pd.DataFrame(cur.fetchmany())
            # We are done if there are no data
            if len(df) == 0:
                break
                #      # Let's write to the file
            else:
                df.to_csv(f, header=False)



    filename = 'MichiganStateNames_all.csv'
    column1 ='Count'
    column2 ='Name'
    column3 ='Year'
    column4 ='Gender'
    #
    answer=0
    data = []  # This will contain our data
    #
    # # Create a csv reader object to iterate through the file
    reader = csv.reader(open(filename, 'rU'), delimiter=',', dialect='excel')
    #
    hrow = reader.next()  # Get the top row
    idx = hrow.index(column1)  # Find the column of the data you're looking for
    nam = hrow.index(column2)
    yr = hrow.index(column3)
    gen=hrow.index(column4)
    #
    #answer = max(reader, key=lambda column: int(column[5].replace(',','')))
    #print answer
    for row in reader:  # Iterate the remaining rows
          data.append((int(row[idx]),row[nam],row[gen],int(row[yr])))
    #
    #print data

    #sort the data list as per count
    # extract max count for gender = F and then gender = M to find most popular names at Michigan State level

    data = sorted(data, key=lambda x:(x[0]),reverse=True)

    newdata_male=[]
    newdata_female=[]

    #if x[3]>2003 then  extract data and store in another list
    for i,e in enumerate(data):
        if e[3] > 2003 and e[2]=='M':
            newdata_male.append(e)
        elif e[3]>2003 and e[2]=='F':
            newdata_female.append(e)
    print "pop Male in MI", newdata_male
    print "pop Female in MI",newdata_female

    pop_male_mi=[]
    pop_female_mi=[]

    for j,k in enumerate(newdata_male):#from the above resulting list we find that popular boy name is Jacob and popular girl name is Emma
        if k[1]=='Jacob':
            pop_male_mi.append(k)


    print "max count jacob", pop_male_mi

    for d,f in enumerate(newdata_female):
            if f[1]=='Emma':
                pop_female_mi.append(f)

    print "max count emma",pop_female_mi


    with open('test.csv', 'wb') as f: #http://stackoverflow.com/questions/36421146/writing-list-of-tuples-as-a-csv-file
       writer = csv.writer(f, delimiter=',')
       writer.writerows(pop_male_mi)
       writer.writerows(pop_female_mi)

    #Merging the data from the two different data sources.
    a = pd.read_csv("NationalNames_popular.csv")
    b = pd.read_csv("test.csv")
    b = b.dropna(axis=1)
    c = pd.concat([a,b],axis=1)
    #merged = a.merge(b, on='Count')
    c.to_csv("Nat_state_popularnames.csv", index=False) #contains the merged data of most popular names at National Level and most popular names at the State Level



if __name__ == '__main__':
    main()



