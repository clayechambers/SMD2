import ReadSMD_eTree as smd
import xlsxwriter
import time

start_time = time.time()

table = smd.xmlSMD2ListofDictionaries(r'data\smd.xml')

workbook = xlsxwriter.Workbook(r'data\SMD.xlsx')
worksheet = workbook.add_worksheet()
#for row in table:

xlrow = 0
xlcolumn = 0

for field in table[0]:
    #print(field)
    worksheet.write(xlrow, xlcolumn, field)
    xlcolumn += 1

for row in table:

    xlrow += 1
    xlcolumn = 0

    for field in row:

        if not row[field] is None:

            worksheet.write(xlrow, xlcolumn, row[field])

        else:

            worksheet.write(xlrow, xlcolumn, 'NONE')

        xlcolumn += 1

workbook.close()

print("--- %s seconds ---" % (time.time() - start_time))