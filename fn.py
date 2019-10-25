''' These Functions will use in main program file of Game. These functions will search for winners in column,row and digonals. '''


def check_c(a,b,c):                             #check in columns
    for i in range(3):
        if a[i]==b[i]==c[i]:
            print a[i]," is winner"
            return 1
            break

def check_r(a,b,c):                             #check in row
    for i in range(1):
        if a[i]==a[i+1]==a[i+2]:                #check in first row
            print a[i]," is winner"
            return 1
            break
        elif b[i]==b[i+1]==b[i+2]:              #check in second row
            print b[i]," is winner"
            return 1
            break
        elif c[i]==c[i+1]==c[i+2]:              #check in third row
            print c[i]," is winner"
            return 1
            break

def check_d(a,b,c):                             #check in digonal
    for i in range(1):
        if a[i]==b[i+1]==c[i+2]:                #check in first digonal
            print a[i]," is winner"
            return 1
            break
        elif c[i]==b[i+1]==a[i+2]:              #check in second digonal
            print c[i]," is winner"
            return 1
            break            
