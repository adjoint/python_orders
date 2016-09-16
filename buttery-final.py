menutext = open('menusample.txt', 'r')
menu = []
menushort = []
#multiple, list for q, number for q
for i in range (500):
    a = menutext.readline()
    if a == '':
        break
    a = a.replace('\r', '')
    b = menutext.readline()
    c = b.split('.')
    d = int(c[0])+float(c[1])/100
    if a[-2:-1].isdigit() == True:
        e = a.split(' ')
        menu.append([e[0],d,0,[],0,int(e[1])])
        menushort.append([e[0],d,int(e[1])])
    else:
        menu.append([a[0:-1],d,0,[],0,1000])
        menushort.append([a[0:-1],d, 1000])
print menushort

f = open('total_sales.txt','w')
s = 0
    
while True:
    name = raw_input("Name: ")
    if name == 'end':
        print 'great work!'
        break
    if name == 'menu':
        print menushort
        continue
    if name[:1] == '-':
        for i in range(len(menu)):
            if name[1:4]==menu[i][0][0:3]:
                if menu[i][3] == []:
                    print 'no queue'
                    break
                else:
                    print menu[i][3][0], menu[i][4], menu[i][3]
                    del menu[i][3][0]
                    menu[i][4] -= 1
                    break
        continue
    if name[:1] == '#':
        for i in range(len(menu)):
            if name[1:4]==menu[i][0][0:3]:
                if menu[i][3] == []:
                    print 'no queue'
                    break
                else:
                    print menu[i][3][0], menu[i][4], menu[i][3]
                    break
        continue
    totalsum = 0
    while True:
        order = raw_input("Order: ")
        num = 1
        if order[-1:] == '+':
            if order[-2:-1].isdigit() == True:
                num = int(order[-2:-1])
            else:
                num = 1
            print num
            for i in range(len(menu)): 
                if order[0:3]==menu[i][0][0:3]:
                    if menu[i][5] == 0:
                        print 'Out of stock'
                        break
                    menu[i][5] -= num
                    menushort[i][2] -= num
                    for k in range(num):
                        menu[i][3].append(name)
                    menu[i][4] += num
                    a = 'Sum: ' + str(num*menu[i][1]) + '     Item: ' + menu[i][0] + ' Quantity: ' + str(num) + ' Price: ' + str(menu[i][1]) + ' Customer: ' + name
                    menu[i][2] += num
                    print a
                    f.write(a+'\n')
                    s = s + num*menu[i][1]
                    totalsum += num*menu[i][1]
                    break
            continue
        if order[-1:].isdigit() == True:
            num = int(order[-1:])
        else:
            num = 1
        for i in range(len(menu)):
            if order[0:3]==menu[i][0][0:3]:
                if menu[i][5] == 0:
                    print 'Out of stock'
                    break
                menu[i][5] -= num
                menushort[i][2] -= num
                for k in range(num):
                        menu[i][3].append(name)
                a = 'Sum: ' + str(num*menu[i][1]) + '     Item: ' + menu[i][0] + ' Quantity: ' + str(num) + ' Price: ' + str(menu[i][1]) + ' Customer: ' + name
                menu[i][2] += num
                menu[i][4] += num
                print a
                f.write(a+'\n')
                s = s + num*menu[i][1]
                totalsum += num*menu[i][1]
                print totalsum
                break
        break
f.write('\n')
for i in range (len(menu)):
    f.write('Item: ' + menu[i][0] + ' Price: ' + str(menu[i][1]) + ' Quantity: ' + str(menu[i][2]) + ' Sum: ' + str(menu[i][1]*menu[i][2]) + '\n')
f.write('\nTotal ' + str(s))     
f.close()


    
