def alternateChar(str):
    count = 0
    for i in range(len(str) - 1):
        c = str[i]
        c1 = str[i + 1]
        if c == c1:
            count += 1
    return count


def CommGemEle(list):
    fw = list[0]
    count = 0
    for i in range(len(fw)):
        c = fw[i]
        flag = True
        for j in range(1, len(list)):
            word = list[j]
            if c not in word:
                flag = False
                break
        if flag:
            count += 1
    return count

def palAna(str):
    d={}
    result=0
    found=False
    for i in range(len(str)):
        if str[i] in d:
            d[str[i]]=d.get(str[i])+1
        else:
            d[str[i]]=1
    print d
    for key in d:
        count=d.get(key)
        if count%2!=0:
            result+=1
    if result>1:
        found=False
    else:
        found=True
    return found
palAna("cdcdcdcdeeeef")