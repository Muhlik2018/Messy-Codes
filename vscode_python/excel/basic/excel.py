import xlrd

#读取excel文件
def excel(line):
    wb = xlrd.open_workbook('D:\\test.xlsx')# 打开Excel文件
    sheet = wb.sheets()[0]#通过excel表格名称(rank)获取工作表
    dat = []  #创建空list
    for a in range(sheet.nrows):  #循环读取表格内容（每次读取一行数据）
                cells = sheet.row_values(a)  # 每行数据赋值给cells
                data=cells[line]#因为表内可能存在多列数据，0代表第一列数据，1代表第二列，以此类推
                dat.append(data) #把每次循环读取的数据插入到list
    return dat
line1 = excel(0) #返回第一行
line2 = excel(1) #返回第二行
line3 = excel(2) #返回第三行
print(len(line1))
print(len(line2))
print(len(line3))
countA=0
countB=0
countC=0




for i in range(0,len(line1)):
    temp=max(line1[i],line2[i],line3[i])
    if temp==line1[i]:
        countA+=1
    elif temp==line2[i]:
        countB+=1
    elif temp==line3[i]:
        countC+=1
print(countA)
print(countB)
print(countC)
