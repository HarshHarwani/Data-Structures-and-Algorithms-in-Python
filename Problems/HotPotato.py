from DataStructures.Queue import Queue_a

def hotPotato(namelist,num):
    q=Queue_a()
    for name in namelist:
        q.insert(name)
    while q.get_size()>1:
        for i in range(num):
            q.insert(q.remove())
        q.remove()
    return q.remove()


print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],1))
