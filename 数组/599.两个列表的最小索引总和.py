class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        min_index = len(list1) + len(list2)
        for i in range(len(list1)):
            restaurant = list1[i]
            if restaurant in list2:
                index = i + list2.index(restaurant)
                if index < min_index:
                    min_index = index
                    res = [restaurant]
                elif index == min_index:
                    res.append(restaurant)

        return res
