class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # 判断车是否阻挡象的路径
        def is_rook_blocking_bishop(rook, bishop, queen):
            # 车不在象和皇后的对角线上
            if abs(bishop[0] - rook[0]) != abs(bishop[1] - rook[1]):
                return False
            else:
                # 车在象和皇后的对角线上且在象和皇后之间
                return min(bishop[0], queen[0]) < rook[0] < max(bishop[0], queen[0]) and min(bishop[1], queen[1]) < \
                    rook[1] < max(bishop[1], queen[1])

        def is_bishop_blocking_rook(rook, bishop, queen):
            # 象不在车和皇后的同一条直线上
            if bishop[0] != rook[0] and bishop[1] != rook[1]:
                return False
            else:
                # 象在车和皇后的同一条直线上且在车和皇后之间
                if bishop[0] == rook[0] == queen[0] or bishop[1] == rook[1] == queen[1]:
                    if rook[0] > bishop[0] > queen[0] or rook[0] < bishop[0] < queen[0] or rook[1] > bishop[1] > queen[
                        1] or rook[1] < bishop[1] < queen[1]:
                        return True
                return False

        car = (a, b)
        elephant = (c, d)
        queen = (e, f)

        if (abs(queen[0] - elephant[0]) == abs(queen[1] - elephant[1]) and
                not is_rook_blocking_bishop(car, elephant, queen)):
            return 1
        if (queen[0] == car[0] or queen[1] == car[1]) and not is_bishop_blocking_rook(car, elephant, queen):
            return 1
        return 2


# 测试
print(Solution().minMovesToCaptureTheQueen(1, 1, 1, 4, 1, 8))  # 应输出 2
