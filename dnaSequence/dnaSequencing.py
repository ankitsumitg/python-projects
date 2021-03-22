def fileToList(filename):
    try:
        mylist = []
        with open(filename, "r") as read:
            details = read.readlines()
            for line in details:
                if line == '\n':
                    mylist.append('')
                else:
                    mylist.extend(line.split())
        return mylist
    except Exception as e:
        return []
def returnFirstString(lst):
    return lst[0] if lst else ''

def strandsAreNotEmpty(s1,s2):
    return False if s1 =='' or s2 == '' else True

def strandsAreEqualLengths(s1,s2):
    return len(s1) == len(s2)

def candidateOverlapsTarget(t,c,overlap):
    k = overlap
    for i in range(overlap):
        if t[-k] !=  c[i]:
            return False
        k -= 1
    return True
def findLargestOverlap(t,c):
    if strandsAreEqualLengths(t,c) and strandsAreNotEmpty(t,c):
        l_overlap = 0
        for i in range(len(c)):
            if candidateOverlapsTarget(t,c,i+1):
                l_overlap = i + 1
        return l_overlap
    return -1
def findBestCandidate(t,clist):
    m = ''
    l = 0
    for i in clist:
        temp_overlap = findLargestOverlap(t,i)
        if temp_overlap >0 and temp_overlap > l:
            l = temp_overlap
            m = i
    return (m,l)
def joinTwoStrands(c,t,overlap):
    if overlap == 0:
        return c+t
    return c+t[overlap:]
def main():
    targetfilename = input('Target strand filename: ')
    candidatefilename = input('Candidate strands filename: ')
    print(findBestCandidate(fileToList(targetfilename)[0],fileToList(candidatefilename))[0])
if __name__ == '__main__':
    main()
