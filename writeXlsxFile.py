import ReadSMD_eTree as smd
import xlsxwriter
import time

workbook = xlsxwriter.Workbook(r'data\SMD.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Hello world')
workbook.close()

#Bunch of crap