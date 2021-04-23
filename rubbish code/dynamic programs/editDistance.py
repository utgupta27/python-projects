def editDistance(targetStr,originalStr):
    if len(targetStr) == 0: return len(originalStr)
    if len(originalStr) == 0 : return  len(targetStr)
    if targetStr[0] == originalStr[0] : return editDistance(targetStr[1:],originalStr[1:])
    delete = editDistance(targetStr[1:],originalStr)
    insert = editDistance(targetStr,originalStr[1:])
    update = editDistance(targetStr[1:],originalStr[1:])
    return min(delete,update,insert) + 1

if __name__ == '__main__':
    print(editDistance('SUNDAY','SATURDAY'))