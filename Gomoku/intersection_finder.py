import pygame


def get_nearest_intersection(x, y, offset_x, offset_y, cell_size, tolerance=15, line_points=None):
    """
    将鼠标点击坐标转换为棋盘上最近的交叉点索引

    参数:
        x, y: 鼠标点击的屏幕坐标
        offset_x, offset_y: 棋盘左上角的偏移量
        cell_size: 每个格子的大小
        tolerance: 吸附容差（像素），默认 15px
        line_points: 棋盘每行/每列的点数，用于边界校验（可选）

    返回:
        (row, col): 交叉点的索引，如果点击超出容差范围或越界则返回 None
    """
    relative_x = x - offset_x
    relative_y = y - offset_y

    col = int((relative_x + cell_size / 2) // cell_size)
    row = int((relative_y + cell_size / 2) // cell_size)

    nearest_x = col * cell_size
    nearest_y = row * cell_size

    distance = ((relative_x - nearest_x) ** 2 + (relative_y - nearest_y) ** 2) ** 0.5

    if distance > tolerance:
        return None

    if line_points is not None:
        if col < 0 or col >= line_points or row < 0 or row >= line_points:
            return None

    return (row, col)
