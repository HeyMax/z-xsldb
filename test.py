import xlrd
data = xlrd.open_workbook("C:\\Users\\80649\\Desktop\\QQ-QA-2018-5-3.xlsx")
#table = data.sheets()[0]
def print_sheet(sheet):
	for row in range(0,sheet.nrows):
		temp=""
		for col in range(0,sheet.ncols):
			if sheet.cell(row,col).value != None:
				temp += str(sheet.cell(row,col).value)+"\t"
		print(temp)
		
def main():
	for sheet in data.sheets():
		print_sheet(sheet)

if __name__ == "__main__":
	main()
