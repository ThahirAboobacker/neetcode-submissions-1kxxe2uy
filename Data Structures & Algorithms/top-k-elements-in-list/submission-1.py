class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ele={}
        for number in nums:
            if number in ele:
                ele[number]+=1
            else:
                ele[number]=1


        sorted_by_value = dict(sorted(ele.items(), key=lambda item: item[1], reverse=True))
        res = []
        for i in list(sorted_by_value.keys())[:k]:
            res.append(i)
        return res
