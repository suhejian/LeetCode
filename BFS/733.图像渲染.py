class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        value = image[sr][sc]
        if image[sr][sc] == newColor:
            return image

        queue = [(sr, sc)]
        while queue:
            r, c = queue.pop(0)
            image[r][c] = newColor
            for mx, my in [(r-1, c), (r, c-1), (r, c+1), (r+1, c)]:
                # 索引合理，符合要求
                if 0 <= mx < len(image) and 0 <= my < len(image[0]) and image[mx][my] == value:
                    queue.append((mx, my))
        return image