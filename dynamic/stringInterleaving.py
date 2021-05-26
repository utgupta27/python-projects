def isInterleave(str1,str2,str3):
    if str1 == '' and str2 == '' and str3 == '':
        return True
    if str1 == '' and str2 == '' and str3 != '':
        return False
    if str3 == '' and (str1 == '' or str2 == ''):
        return False

    if str1 != '' and str3 != '':
        if str1[0] == str3[0]:
            return isInterleave(str1[1:],str2,str3[1:])
    if str2 != '' and str3 != '':
        if str2[0] == str3[0]:
            return isInterleave(str1,str2[1:],str3[1:])

if __name__ == '__main__':
    print(isInterleave('abc','xyz','xyabcz'))