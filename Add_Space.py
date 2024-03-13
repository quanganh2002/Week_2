def add_space (left, path):
    if left == len(s): 
        result.append(" ".join(path))
        return
    for i in range(left+1, len(s)+1):
        word = s[left:i]
        if word in wordDict:
            add_space(i,path + [word])


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
result = []
add_space(0,[])
print(result)