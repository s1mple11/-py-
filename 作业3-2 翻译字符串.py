def decodeString(s: str) -> str:
    stack = []   
    res = ''  
    count = 0  
    for c in s:   
        if c == '[':  
            stack.append([count, res])
            count, res = 0, ''   
        elif c == ']':  
            cur_count, last_res = stack.pop()  # 弹出保存的临时变量
            res = last_res + cur_count * res  # 更新res临时变量
        elif '0' <= c <= '9':   # 判断是否为数字字符，保存
            count = count * 10 + int(c)
        else:   # 如果为字符，简单相加存储临时变量
            res += c
    return res
res=input()
print(decodeString(res))