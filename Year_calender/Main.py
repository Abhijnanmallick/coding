import Get_jan
year=int(input("Enter the year (YYYY)::"))
jan_1=Get_jan.jan_fst(year)
days=['SUN','MON','TUE','WED','THU','FRI','SAT']

#january
print("\n         JANUARY")
for i in days:
    print(i,end=" ")
print()
total=1
chk=0
chv=1
while(total<32):
    if chv<=jan_1:
        chv+=1
        chk+=1
        print("    ",end="")
        continue
    print(f" {total}",end=" ") if total>9 else print(f" 0{total}",end=" ")
    total+=1
    chk+=1
    if chk%7==0:
        print()
print("\n\n----------------------------")

#february
print("\n         FEBRUARY")
next_st=(31%7)+jan_1
while(next_st>6):
    next_st%=7
for i in days:
    print(i,end=" ")
print()
end=28
if(year%100)%4==0:
    end=29
total=1
chk=0
chv=1
while(total<=end):
    if chv<=next_st:
        chv+=1
        chk+=1
        print("    ",end="")
        continue
    print(f" {total}",end=" ") if total>9 else print(f" 0{total}",end=" ")
    total+=1
    chk+=1
    if chk%7==0:
        print()
print("\n\n----------------------------")

#march
print("\n         MARCH")
mar_st=(31+end)%7+jan_1
while(mar_st>6):
    mar_st%=7
for i in days:
    print(i,end=" ")
print()
total=1
chk=0
chv=1
while(total<=31):
    if chv<=mar_st:
        chv+=1
        chk+=1
        print("    ",end="")
        continue
    print(f" {total}",end=" ") if total>9 else print(f" 0{total}",end=" ")
    total+=1
    chk+=1
    if chk%7==0:
        print()
print("\n\n----------------------------")

#april
print("\n         APRIL")
st=(31+end+31)%7+jan_1
while(st>6):
    st%=7
for i in days:
    print(i,end=" ")
print()
total=1
chk=0
chv=1
while(total<=30):
    if chv<=st:
        chv+=1
        chk+=1
        print("    ",end="")
        continue
    print(f" {total}",end=" ") if total>9 else print(f" 0{total}",end=" ")
    total+=1
    chk+=1
    if chk%7==0:
        print()
print("\n\n----------------------------")

#may
print("\n         MAY")
st=(31+end+31+30)%7+jan_1
while(st>6):
    st%=7
for i in days:
    print(i,end=" ")
print()
total=1
chk=0
chv=1
while(total<=31):
    if chv<=st:
        chv+=1
        chk+=1
        print("    ",end="")
        continue
    print(f" {total}",end=" ") if total>9 else print(f" 0{total}",end=" ")
    total+=1
    chk+=1
    if chk%7==0:
        print()
print("\n\n----------------------------")

#june
print("\n         JUNE")
st=(31+end+31+30+31)%7+jan_1
while(st>6):
    st%=7
for i in days:
    print(i,end=" ")
print()
total=1
chk=0
chv=1
while(total<=30):
    if chv<=st:
        chv+=1
        chk+=1
        print("    ",end="")
        continue
    print(f" {total}",end=" ") if total>9 else print(f" 0{total}",end=" ")
    total+=1
    chk+=1
    if chk%7==0:
        print()
print("\n\n----------------------------")

#july
print("\n         JULY")
st=(31+end+31+30+31+30)%7+jan_1
while(st>6):
    st%=7
for i in days:
    print(i,end=" ")
print()
total=1
chk=0
chv=1
while(total<=31):
    if chv<=st:
        chv+=1
        chk+=1
        print("    ",end="")
        continue
    print(f" {total}",end=" ") if total>9 else print(f" 0{total}",end=" ")
    total+=1
    chk+=1
    if chk%7==0:
        print()
print("\n\n----------------------------")

#august
print("\n         AUGUST")
st=(31+end+31+30+31+30+31)%7+jan_1
while(st>6):
    st%=7
for i in days:
    print(i,end=" ")
print()
total=1
chk=0
chv=1
while(total<=31):
    if chv<=st:
        chv+=1
        chk+=1
        print("    ",end="")
        continue
    print(f" {total}",end=" ") if total>9 else print(f" 0{total}",end=" ")
    total+=1
    chk+=1
    if chk%7==0:
        print()
print("\n\n----------------------------")

#september
print("\n         SEPTEMBER")
st=(31+end+31+30+31+30+31+31)%7+jan_1
while(st>6):
    st%=7
for i in days:
    print(i,end=" ")
print()
total=1
chk=0
chv=1
while(total<=30):
    if chv<=st:
        chv+=1
        chk+=1
        print("    ",end="")
        continue
    print(f" {total}",end=" ") if total>9 else print(f" 0{total}",end=" ")
    total+=1
    chk+=1
    if chk%7==0:
        print()
print("\n\n----------------------------")

#october
print("\n         OCTOBER")
st=(31+end+31+30+31+30+31+31+30)%7+jan_1
while(st>6):
    st%=7
for i in days:
    print(i,end=" ")
print()
total=1
chk=0
chv=1
while(total<=31):
    if chv<=st:
        chv+=1
        chk+=1
        print("    ",end="")
        continue
    print(f" {total}",end=" ") if total>9 else print(f" 0{total}",end=" ")
    total+=1
    chk+=1
    if chk%7==0:
        print()
print("\n\n----------------------------")

#november
print("\n         NOVEMBER")
st=(31+end+31+30+31+30+31+31+30+31)%7+jan_1
while(st>6):
    st%=7
for i in days:
    print(i,end=" ")
print()
total=1
chk=0
chv=1
while(total<=30):
    if chv<=st:
        chv+=1
        chk+=1
        print("    ",end="")
        continue
    print(f" {total}",end=" ") if total>9 else print(f" 0{total}",end=" ")
    total+=1
    chk+=1
    if chk%7==0:
        print()
print("\n\n----------------------------")

#december
print("\n         DECEMBER")
st=(31+end+31+30+31+30+31+31+30+31+30)%7+jan_1
while(st>6):
    st%=7
for i in days:
    print(i,end=" ")
print()
total=1
chk=0
chv=1
while(total<=31):
    if chv<=st:
        chv+=1
        chk+=1
        print("    ",end="")
        continue
    print(f" {total}",end=" ") if total>9 else print(f" 0{total}",end=" ")
    total+=1
    chk+=1
    if chk%7==0:
        print()
print("\n\n----------------------------")