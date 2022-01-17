def VerifyBST(arr):
        if arr == []:
            return False
        if len(arr)==1:
            return True
        root = arr[-1]
        #串的最后一个数为根
        del arr[-1]
        #删除根
        pos =None
        #左右子树的分界点，即右子树的第一个结点

        for i in range(len(arr)):
            if pos == None and arr[i] > root  :
                #第一次找到大于根的结点，为右子树的第一个结点
                pos = i

            if pos != None and arr[i] < root  :
                #发现右子树有比根小的结点，返回false
                return 0

        if pos== None:
            #没找到大于根的结点，即该串只有左子树没有右子树
            return VerifyBST(arr)

        if arr[:pos] == []:
            left_ret = 1
        else:
            left_ret = VerifyBST(arr[:pos])
        if arr[pos:] == []:
            right_ret = 1
        else:
            right_ret = VerifyBST(arr[pos:])

        return left_ret*right_ret

a= list(map(int,input ().split()))
b=VerifyBST(a)
if b==0:
    print("false",end='')
if b==1:
    print("true",end='')