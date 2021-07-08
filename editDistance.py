# THE KEY INTUITION FOR EDIT DISTANCE IS TO UNDERSTAND THAT THE SOURCE STRING IS CONVERTED TO DESTINATION STRING, SO ALWAYS KEEP THE LOGIC CENTERED AROUND THE SOURCE STRING INDEX
def match(a, b):
    if a == b:
        return 0
    else:
        return 1

# def subseqn(src, dst, matchIndices):
#     max_seqn_len=0
#     max_seq = ''
#     seqns = {}
#     for i in range(len(matchIndices)):
#         if i==0:
#             max_seqn_len=1
#             max_seq=src[matchIndices[0][0]]
#             continue
#         if matchIndices[i][0] == matchIndices[i-1][0] + 1 and matchIndices[i][1] == matchIndices[i-1][1] + 1:
#             max_seqn_len+=1
#             max_seq+=src[matchIndices[i][0]]
#         else:
#             seqns[max_seqn_len] = max_seq
#             max_seqn_len=1
#             max_seq=src[matchIndices[0][0]]

#     return seqns[sorted(seqns.keys())[-1]]


def editDistance(src, dst):
    table = {}
    srcLen = len(src)
    dstLen = len(dst)

    subString = ''
    matches = {}
    iPrev = None
    for i in range(0, srcLen):
        for j in range(0, dstLen):
            if i == 0:
                table[(0, j)] = j
            if j == 0:
                table[(i, 0)] = i
            if i != 0 and j != 0:
                table[(i, j)] = min(table[i-1, j]+1, table[i, j-1]+1,
                                    table[i-1, j-1]+match(src[i], dst[j]))
            
            if not match(src[i],dst[j]) and iPrev!=i:
                subString+=src[i]
                iPrev=i
            elif not match(src[i],dst[j]) and iPrev==None:
                subString=src[i]
                

                
            # if src[i]==dst[j] and src[i-1]==dst[j-1] and prevSrcInd==i:
            #     subString += src[i]
            #     prevSrcInd=i
            # elif not (src[i]==dst[j] and src[i-1]==dst[j-1]) and prevSrcInd!=i:
            #     matches[len(subString)] = subString
            #     subString = ''
    return table[(srcLen-1, dstLen-1)], subString


if __name__ == "__main__":
    src = 'petition'
    dst = 'competition'
    
    # src = 'abcdgh'
    # dst = 'abdfhr'
    print(editDistance(src, dst))
