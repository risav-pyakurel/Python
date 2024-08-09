# Given an array of strings strs, group the anagrams together.You can return the answer in any order.
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

given_strs = ["eat","tea","tan","ate","nat","bat"]
new_dict = {}

for i in given_strs:
    s= "".join(sorted(i))
    print(s)
    if s in new_dict:
        new_dict[s].append(i)

    else:
        new_dict[s] = [i]

#print(new_dict)

print(list(new_dict.values()))
















