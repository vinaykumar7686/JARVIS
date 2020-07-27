def isPartialFloat(s):
    try:
        float(s)
        return True
    except Exception:
        return False

def convert(exp):
    exp.append('$')
    point = 0
    res = []
    for i,sym in enumerate(exp):
        if sym == ' ':
            continue
        if sym.isdigit():
            if exp[i-1].isdigit():
                res[point-1] = res[point-1]+sym
            elif res and isPartialFloat(res[point-1]):
                res[point-1] = res[point-1]+sym
            else:
                res.append(sym)
                point+=1
        elif sym=='.':
            if exp[i-1].isdigit():
                res[point-1] = res[point-1]+sym
        elif sym.isalpha():
            if exp[i-1].isalpha():
                res[point-1] = res[point-1]+sym
            else:
                res.append(sym)
                point+=1
        else:
            point+=1
            res.append(sym)
    return res[:point-1]
        
print(convert(list(input("Enter expression: "))))

