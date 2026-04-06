class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr=[]
        for ob in strs:
            found = False
            for i in range(len(arr)):
                if sorted(ob) == sorted(arr[i][0]):
                    arr[i].append(ob)
                    found = True
                    break
            if not found:
                arr.append([ob])
        return arr
