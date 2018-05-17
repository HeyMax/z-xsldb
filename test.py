import xlrd
data = xlrd.open_workbook("C:\\Users\\Heymax\\Desktop\\DBTest.xlsx")
table = data.sheets()[0]

for row in range(0,table.nrows):
    temp=""
    for col in range(0,table.ncols):
        if table.cell(row,col).value != None:
            temp += str(table.cell(row,col).value)+"\t"
    print(temp)

