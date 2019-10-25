def check_put_comp_r(a,b,c):
    i=0
    if a[i]=='o' and a[i+1]=='o' and a[i+2]!='x' and a[i+2]!='o':
        return i+2
    elif a[i]=='o' and a[i+2]=='o' and a[i+1]!='x' and a[i+1]!='o':
        return i+1
    elif a[i+1]=='o'and a[i+2]=='o' and a[i]!='x' and a[i]!='o':
        return i
    elif b[i]=='o' and b[i+1]=='o' and b[i+2]!='x' and b[i+2]!='o':
        return 3+i+2
    elif b[i]=='o' and b[i+2]=='o' and b[i+1]!='x' and b[i+1]!='o':
        return 3+i+1
    elif b[i+1]=='o' and b[i+2]=='o' and b[i]!='x' and b[i]!='o':
        return 3+i
    elif c[i]=='o' and c[i+1]=='o' and c[i+2]!='x' and c[i+2]!='o':
        return 6+i+2
    elif c[i]=='o' and c[i+2]=='o' and c[i+1]!='x' and c[i+1]!='o':
        return 6+i+1
    elif c[i+1]=='o' and c[i+2]=='o' and c[i]!='x' and c[i]!='o':
        return 6+i
    else:
        return -1
     
def check_put_comp_c(a,b,c):
    for i in range(3):
        if a[i]=='o' and b[i]=='o' and c[i]!='x' and c[i]!='o':
            return 6+i
        elif a[i]=='o' and c[i]=='o' and b[i]!='x' and b[i]!='o':
            return 3+i
        elif b[i]=='o' and c[i]=='o' and a[i]!='x' and a[i]!='o':
            return i
    return -1
def check_put_comp_d(a,b,c):
    i=0
    if a[i]=='o' and b[i+1]=='o' and c[i+2]!='x' and c[i+2]!='o':
        return 8
    elif ((a[i]=='o' and c[i+2]=='o') or (a[i+2]=='o' and c[i]=='o')) and b[i+1]!='x' and b[i+1]!='o':
        return 4
    elif b[i+1]=='o' and c[i+2]=='o' and a[i]!='x' and a[i]!='o':
        return 0
    elif a[i+2]=='o' and b[i+1]=='o' and c[i]!='x' and c[i]!='o':
        return 6
    elif b[i+2]=='o' and c[i+1]=='o' and a[i+2]!='x' and a[i+2]!='o':
        return 2
    else:
        return -1
def check_put_user_r(a,b,c):
    i=0
    if a[i]=='x' and a[i+1]=='x' and a[i+2]!='x' and a[i+2]!='o':
        return i+2
    elif a[i]=='x' and a[i+2]=='x' and a[i+1]!='x' and a[i+1]!='o':
        return i+1
    elif a[i+1]=='x' and a[i+2]=='x' and a[i]!='x' and a[i]!='o':
        return i
    elif b[i]=='x' and b[i+1]=='x' and b[i+2]!='x' and b[i+2]!='o':
        return 3+i+2
    elif b[i]=='x' and b[i+2]=='x' and b[i+1]!='x' and b[i+1]!='o':
        return 3+i+1
    elif b[i+1]=='x' and b[i+2]=='x' and b[i]!='x' and b[i]!='o':
        return 3+i
    elif c[i]=='x' and c[i+1]=='x' and c[i+2]!='x' and c[i+2]!='o':
        return 6+i+2
    elif c[i]=='x' and c[i+2]=='x' and c[i+1]!='x' and c[i+1]!='o':
        return 6+i+1
    elif c[i+1]=='x' and c[i+2]=='x' and c[i]!='x' and c[i]!='o':
        return 6+i
    else:
        return -1
     
def check_put_user_c(a,b,c):
    for i in range(3):
        if a[i]=='x' and b[i]=='x' and c[i]!='x' and c[i]!='o':
            return 6+i
        elif a[i]=='x' and c[i]=='x' and b[i]!='x' and b[i]!='o':
            return 3+i
        elif b[i]=='x' and c[i]=='x' and a[i]!='x' and a[i]!='o':
            return i
    return -1
def check_put_user_d(a,b,c):
    i=0
    if a[i]=='x' and b[i+1]=='x' and c[i+2]!='x' and c[i+2]!='o':
        return 8
    elif ((a[i]=='x' and c[i+2]=='x') or (a[i+2]=='x' and c[i]=='x')) and b[i+1]!='x' and b[i+1]!='o':
        return 4
    elif b[i+1]=='x' and c[i+2]=='x' and a[i]!='x' and a[i]!='o':
        return 0
    elif a[i+2]=='x' and b[i+1]=='x' and c[i]!='x' and c[i]!='o':
        return 6
    elif b[i+2]=='x' and c[i+1]=='x' and a[i+2]!='x' and a[i+2]!='o':
        return 2
    else:
        return -1
def check_opposite_corner(a,b,c):
    if a[0]==c[2] or a[2]==c[0]:
        if a[1]!='x' and a[1]!='o':
            return 1
        elif b[0]!='x' and b[0]!='o':
            return 3
        elif b[2]!='x' and b[2]!='0':
            return 5
        elif c[1]!='x' and c[1]!='o':
            return 7
    return -1
    
def check_put_priority(a,b,c,priority):
    for i in priority:
        if i<3:
            if a[i]!='x' and a[i]!='o':
                a[i]='o'
                break
            else:
                continue
        elif i<6:
            i-=3
            if b[i]!='x' and b[i]!='o':
                b[i]='o'
                break
            else:
                continue
        else:
            i-=6
            if c[i]!='x' and c[i]!='o':
                c[i]='o'
                break
            else:
                continue
