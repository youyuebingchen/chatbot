# 先建立一个基于目标行业的database
graph = {"上海":["苏州","常州"],
         "苏州":["常州","镇江"],
         "常州":["镇江"],
         "镇江":["常州"],
         "盐城":["南通"],
         "南通":["常州"]}
# 明确如何从A 到 B
def findpath(start,end,path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return "没有路径"
    for node in graph[start]:
        if node not in path:
            newpath = findpath(node,end,path)
            if newpath:
                return newpath
    return "没有路径"
print(findpath("上海","广州"))