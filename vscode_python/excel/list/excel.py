import xlrd

#读取excel文件
#def test(line):
    #for i in range(0,len(line)):
        #if line[i]:
            #print(i)

def search(competeLine,nameLine):
    temp=[]
    for i in range(1,len(competeLine)):
        if competeLine[i]:
            temp.append(i)
    print(competeLine[0]+':')
    for i in range(0,len(temp)):
        print(nameLine[temp[i]]+' ')
    print('\n')

def search2(GradeLine,nameLine):
    temp=[]
    for i in range(1,len(GradeLine)):
        if GradeLine[i]==19:
            temp.append(i)
    print('19级有:')
    for i in range(0,len(temp)):
        print(nameLine[temp[i]]+'、',end='')
    print(len(temp))



def excel(line):
    wb = xlrd.open_workbook('D:\\test.xlsx')# 打开Excel文件
    sheet = wb.sheets()[4]#通过excel表格名称(rank)获取工作表
    dat = []  #创建空list
    for a in range(sheet.nrows):  #循环读取表格内容（每次读取一行数据）
                cells = sheet.row_values(a)  # 每行数据赋值给cells
                data=cells[line]#因为表内可能存在多列数据，0代表第一列数据，1代表第二列，以此类推
                dat.append(data) #把每次循环读取的数据插入到list
    return dat

line1 = excel(0) #返回第一行
name = excel(1) #返回第二行
line3 = excel(2) #返回第三行
competeLine1 = excel(3) #返回第四行

competeLine2 = excel(27) #返回第二十七行
#print(len(line1))
#print(len(line2))
#print(len(line3))
#print(len(line4))


#print(line1)
#print(line2)
#print(line3)
#print(line4)

#for i in range(3,27):
    #search(excel(i),name)

search2(line1,name)




#从line3开始是比赛数据
#每个比赛数据 需要记录其第一行 之后记录其之后不为空的行数 并打印出对应位置的名字


#for i in range(0,len(line4)):
