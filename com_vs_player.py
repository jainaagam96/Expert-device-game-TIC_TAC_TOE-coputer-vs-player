from fn import *
from fn2 import *
a=['1','2','3']         #Row 1
b=['4','5','6']         #Row 2
c=['7','8','9']         #Row 3

i=0
print a,'\n',b,'\n',c,'\n'
chance=input("enter 0 for first chance else press anything ")                            
if chance!=0:
    i=1
chance=0
priority=[4,0,2,6,8,1,3,5,7]
while True:
    if i%2==0:
        print "player's turn"
        x=input("enter positon ")
        
        if x not in range(1,10):
            print "invalid input"
            continue
        if x<=3:
            if a[x-1]=='x' or a[x-1]=='o':
                print "invalid input"
                continue
            a[x-1]='x'
        elif x<=6:
            if b[x-4]=='x' or b[x-4]=='o':
                print "invalid input"
                continue
            b[x-4]='x'
        elif x<=9:
            if c[x-7]=='x' or c[x-7]=='o':
                print "invalid input"
                continue
            c[x-7]='x'
        print a,'\n',b,'\n',c,'\n'
        i+=1
        chance+=1
        if check_c(a,b,c) or check_r(a,b,c) or check_d(a,b,c):          #checking  for  winner
            break
    else:
        print "cumputer's turn\n"
        
        p=check_put_comp_r(a,b,c)                                        
        q=check_put_comp_c(a,b,c)
        r=check_put_comp_d(a,b,c)
        t=check_put_user_r(a,b,c)
        u=check_put_user_c(a,b,c)
        v=check_put_user_d(a,b,c)
        s=check_opposite_corner(a,b,c)
        if p!=-1:
            if p<3:
                a[p]='o'
            elif p<6:
                p-=3
                b[p]='o'
            else:
                p-=6
                c[p]='o'
        elif q!=-1:
            if q<3:
                a[q]='o'
            elif q<6:
                q-=3
                b[q]='o'
            else:
                q-=6
                c[q]='o'
        elif r!=-1:
            if r<3:
                a[r]='o'
            elif r<6:
                r-=3
                b[r]='o'
            else:
                r-=6
                c[r]='o'
        elif t!=-1:
            if t<3:
                a[t]='o'
            elif t<6:
                t-=3
                b[t]='o'
            else:
                t-=6
                c[t]='o'
        elif u!=-1:
            if u<3:
                a[u]='o'
            elif u<6:
                u-=3
                b[u]='o'
            else:
                u-=6
                c[u]='o'
        elif v!=-1:
            if v<3:
                a[v]='o'
            elif v<6:
                v-=3
                b[v]='o'
            else:
                v-=6
                c[v]='o'
        elif s!=-1:
            if s<3:
                a[s]='o'
            elif s<6:
                s-=3
                b[s]='o'
            else:
                s-=6
                c[s]='o'
        else:
            check_put_priority(a,b,c,priority)
        print a,'\n',b,'\n',c,'\n'
        i+=1
        chance+=1
        if check_c(a,b,c) or check_r(a,b,c) or check_d(a,b,c):          #checking  for  winner
            break
    if chance==9:                                                       #checking for draw
        print "match is draw"
        break
