import sqlite3 as lite
import ReadSMD_eTree as smd
import time

start_time = time.time()

table = smd.xmlSMD2ListofDictionaries(r'data\smd.xml')

conn = lite.connect(r'data\smdDB.db')

#conn.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='SMD_MAIN' ''')

conn.execute('''CREATE TABLE IF NOT EXISTS SMD_MAIN
     (ID INT PRIMARY KEY     NOT NULL,
     CATEGORY           TEXT    NOT NULL,
     FEATURE_NAME       TEXT    NOT NULL,
     FEATURE_DESC       TEXT    NOT NULL);''')

id = 1
for row in table:

    #print(id, row['Category'], row['FeatureName'], row['FeatureDescription'])
    print("INSERT INTO SMD_MAIN (ID,CATEGORY,FEATURE_NAME,FEATURE_DESC) VALUES (" + str(id) + ", '" + row['Category'] + "', '" + row['FeatureName'] + "', '" + row['FeatureDescription'].strip() + "')")
    
    conn.execute("INSERT INTO SMD_MAIN (ID,CATEGORY,FEATURE_NAME,FEATURE_DESC) VALUES (" + str(id) + ", '" + row['Category'] + "', '" + row['FeatureName'] + "', '" + row['FeatureDescription'].strip() + "')")
    
    id += 1

print("--- %s seconds ---" % (time.time() - start_time))