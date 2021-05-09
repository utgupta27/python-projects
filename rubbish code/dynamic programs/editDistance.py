def editDistance(targetStr,originalStr):
    if targetStr == None or targetStr == '': return len(originalStr)
    if originalStr == None or originalStr == '': return len(targetStr)
    if originalStr == targetStr : return editDistance(targetStr[1:],originalStr[1:])
    delete = editDistance(targetStr[1:],originalStr)
    update = editDistance(targetStr[1:],originalStr[1:])
    insert = editDistance(targetStr,originalStr[1:])
    return max(delete,update,insert) + 1

if __name__ == '__main__':
    print(editDistance('SUNDAY','SUNDAY'))