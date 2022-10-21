list=[{"name":"xiaoming","学号":"123","语文":"80"},{"name":"xiaow","学号":"1234","语文":"90"}]

res=[item[key] for item in list for key in item]
print(res)
for item in list:
    for key in item:
        print(item[key])