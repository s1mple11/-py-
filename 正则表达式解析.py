class node:  # 结点类
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def setorder(regular):  # 遍历输入，按照优先级添加括号
    m = 0 #表达式长度
    while m < len(regular):
        if regular[m] == '*':
            if regular[m - 1] != ')':
                regular.insert(m - 1, '(')
                regular.insert(m + 2, ')')
                m = m + 2
        m = m + 1
    return regular

def createtree(regular, m):  # 构建二叉语法树
    root = node('')
    while m < len(regular):
        if root.value == '':  # 遍历开始时初始化根结点
            if regular[m] == '(':
                root, m = createtree(regular, m + 1)
                continue
            elif 'a' <= regular[m] <= 'z':
                root = node(regular[m])
                m = m + 1
                continue
        if 'a' <= regular[m] <= 'z':  # 分类读取正则表达式
            root.left = copy(root)
            root.value = '+'
            root.right = node(regular[m])
            m = m + 1
        elif regular[m] == '*':
            root.left = copy(root)
            root.value = '*'
            root.right = None
            m = m + 1
        elif regular[m] == '|':
            root.left = copy(root)
            root.value = '|'
            root.right, m = createtree(regular, m + 1)
        elif regular[m] == ')':
            return root, m + 1
        elif regular[m] == '(':
            root.left = copy(root)
            root.value = '+'
            root.right, m = createtree(regular, m + 1)
    return root, m

def gettreedeep(root):  # 求二叉树深度
    deeplist = [root]
    depth = 0  # 二叉树深度
    while deeplist != []:
        for j in range(len(deeplist)):
            if deeplist[0].left != None and deeplist[0].right == None:
                deeplist.append(deeplist[0].left)
            elif deeplist[0].right != None:
                deeplist.append(deeplist[0].left)
                deeplist.append(deeplist[0].right)
            del deeplist[0]
        depth += 1
    return depth

def copy(Node):  # 深拷贝函数
    newnode = node('')
    newnode.value = Node.value
    newnode.right = Node.right
    newnode.left = Node.left
    return newnode


def printtree(root):  # 打印二叉树
    depth = gettreedeep(root)
    a = 0  # 根节点前空格数
    if depth <= 5:
        for j in range(1, depth):
            a +=   5 * j - 4
    else:
        for j in range(1, depth):
            a +=   3 * j - 2
    nodelist = [root]  # 节点列表
    blanklist = [-1, a]  # 节点空格列表
    blankchangelist = [0]  # 空格变化列表
    if depth <= 5:  # 初始打印连接符次数
        b = 5 * (depth - 1) - 4
    else:
        b = 3 * (depth - 1) - 2
    while nodelist != []:
        for j in range(len(nodelist)):  # 打印结点值
            print(' ' * (blanklist[j + 1] - blanklist[j] - 1), end='')
            print(nodelist[j].value, end='')
        print('')
        for j in range(len(nodelist)):  # 遍历节点列表，迭代节点列表，节点空格列表，空格变化列表
            if nodelist[0].left != None and nodelist[0].right == None:
                nodelist.append(nodelist[0].left)
                blankchangelist.append(0)
                blanklist.append(blanklist[1])
            elif nodelist[0].right != None:
                nodelist.append(nodelist[0].left)
                nodelist.append(nodelist[0].right)
                blankchangelist.append(-1)
                blankchangelist.append(1)
                blanklist.append(blanklist[1])
                blanklist.append(blanklist[1])
            del nodelist[0]
            del blankchangelist[0]
            del blanklist[1]
        for j in range(b):  # 打印连接符
            for j in range(len(nodelist)):  # 遍历空格变化列表，迭代节点空格列表
                blanklist[j + 1] += blankchangelist[j]
            for j in range(len(nodelist)):
                print(' ' * (blanklist[j + 1] - blanklist[j] - 1), end='')
                if blankchangelist[j] == 1:
                    print('\\', end='')
                elif blankchangelist[j] == -1:
                    print('/', end='')
                elif blankchangelist[j] == 0:
                    print('|', end='')
            print('')
        if depth <= 5:  # 缩减打印连接符个数
            b -=  5
        else:
            b -=  3

regular = list(input()) 
regular = setorder(regular)
root, m = createtree(regular, 0)
printtree(root)