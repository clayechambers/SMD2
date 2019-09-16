import ReadSMD_eTree as smd
import time

start_time = time.time()

table = smd.xmlSMD2ListofDictionaries(r'data\smd.xml')

with open(r'data\data.txt','w') as file:

    for row in table:
    
        file.write('----------------------------------------------\n')
    
        for field in row:
    
            if not row[field] is None:
    
                file.write(field + ' = ' + row[field] + '\n')
    
            else:
    
                file.write(field + ' = NONE\n')
                
print("--- %s seconds ---" % (time.time() - start_time))