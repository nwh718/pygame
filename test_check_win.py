#!/usr/bin/env python3
"""
测试增强版五子棋胜负判断函数
"""

from collections import namedtuple

Point = namedtuple('Point', 'X Y')


class Checkerboard:
    def __init__(self, line_points=15):
        self._line_points = line_points
        self._checkerboard = [[0] * line_points for _ in range(line_points)]
    
    def drop(self, point, value):
        self._checkerboard[point.Y][point.X] = value
    
    def check_win(self, point, value):
        if self._check_direction(point, value, 1, 0):
            return True
        if self._check_direction(point, value, 0, 1):
            return True
        if self._check_direction(point, value, 1, 1):
            return True
        if self._check_direction(point, value, 1, -1):
            return True
        return False
    
    def _check_direction(self, point, value, x_offset, y_offset):
        count = 1
        for step in range(1, 5):
            x = point.X + step * x_offset
            y = point.Y + step * y_offset
            if 0 <= x < self._line_points and 0 <= y < self._line_points:
                if self._checkerboard[y][x] == value:
                    count += 1
                else:
                    break
            else:
                break
        for step in range(1, 5):
            x = point.X - step * x_offset
            y = point.Y - step * y_offset
            if 0 <= x < self._line_points and 0 <= y < self._line_points:
                if self._checkerboard[y][x] == value:
                    count += 1
                else:
                    break
            else:
                break
        return count >= 5
    
    def print_board(self):
        print("  " + " ".join([f"{i:2}" for i in range(self._line_points)]))
        for y in range(self._line_points):
            print(f"{y:2}", end=" ")
            for x in range(self._line_points):
                val = self._checkerboard[y][x]
                if val == 0:
                    print(".", end="  ")
                elif val == 1:
                    print("X", end="  ")
                else:
                    print("O", end="  ")
            print()


def test_horizontal():
    print("\n=== 测试水平方向五子连珠 ===")
    board = Checkerboard()
    for x in range(5, 10):
        board.drop(Point(x, 5), 1)
    board.print_board()
    result = board.check_win(Point(7, 5), 1)
    print(f"结果: {'获胜 ✓' if result else '未获胜 ✗'}")
    return result


def test_vertical():
    print("\n=== 测试垂直方向五子连珠 ===")
    board = Checkerboard()
    for y in range(5, 10):
        board.drop(Point(7, y), 2)
    board.print_board()
    result = board.check_win(Point(7, 7), 2)
    print(f"结果: {'获胜 ✓' if result else '未获胜 ✗'}")
    return result


def test_diagonal1():
    print("\n=== 测试左上到右下对角线五子连珠 ===")
    board = Checkerboard()
    for i in range(5, 10):
        board.drop(Point(i, i), 1)
    board.print_board()
    result = board.check_win(Point(7, 7), 1)
    print(f"结果: {'获胜 ✓' if result else '未获胜 ✗'}")
    return result


def test_diagonal2():
    print("\n=== 测试右上到左下对角线五子连珠 ===")
    board = Checkerboard()
    for i in range(5, 10):
        board.drop(Point(12 - i, i), 2)
    board.print_board()
    result = board.check_win(Point(7, 7), 2)
    print(f"结果: {'获胜 ✓' if result else '未获胜 ✗'}")
    return result


def test_edge_case():
    print("\n=== 测试边界情况 (棋盘角落) ===")
    board = Checkerboard()
    for i in range(0, 5):
        board.drop(Point(i, i), 1)
    board.print_board()
    result = board.check_win(Point(2, 2), 1)
    print(f"结果: {'获胜 ✓' if result else '未获胜 ✗'}")
    return result


def main():
    print("增强版五子棋胜负判断函数测试")
    print("=" * 50)
    
    tests = [
        test_horizontal,
        test_vertical,
        test_diagonal1,
        test_diagonal2,
        test_edge_case
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"测试完成: {passed}/{len(tests)} 个测试通过")


if __name__ == '__main__':
    main()
