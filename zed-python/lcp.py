def longestCommonPrefix(strs):
    """
           :type strs: List[str]
           :rtype: str
    """
    #res = ''
    if len(strs) == 0:
        return ''
    res = ''
    strs = sorted(strs)
    print("sorted array >>>",strs)
    for i in strs[0]:
        print('i in strs[0]',i)
        print('>>>>before>>',res,i)
        if strs[-1].startswith(res+i):
            res += i
            print('>>>after>>>',res,i)
        else:
            break
    return res
y = ['ankit','ram','visnu','kol']
#x = ['leetcode','leeds','lomano','leemo','leajeans']
print(longestCommonPrefix(y))
