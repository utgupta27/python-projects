def isInterleave(str1,str2,str3):
    if (len(str1) == 0 or str1 == '') and (len(str2) == 0 or str2 == '') and (len(str3) == 0 or str3 == ''):
        return True
    if len(str3) == 0 or str3 == '':
        return False
    if (len(str1) == 0 or str1 == '') and (len(str2) == 0 or str2 == ''):
        return False
    temp1,temp2 = False,False
    if str1[0] == str3[0]:
        temp1 = isInterleave(str1[1:],str2,str3[1:])
    if str2[0] == str3[0]:
        temp2 = isInterleave(str1,str2[1:],str3[1:])

    return temp1 or temp2

if __name__ == '__main__':
    print(isInterleave('abc','xyz','axybzc'))