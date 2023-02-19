def jan_fst(year):
    diff=year-1
    leaps=0
    x=1
    while(x<year):
        if((x%100)%4==0):
            leaps+=1
        x+=1
    return ((leaps*366)+((diff-leaps)*365))%7