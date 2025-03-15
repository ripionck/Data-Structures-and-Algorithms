def groupAnagrams(strs):
    hashmap = {}
    for s in strs:
        key = tuple(sorted(s))
        if key not in hashmap:
            hashmap[key] = []
        hashmap[key].append(s)
    return list(hashmap.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))