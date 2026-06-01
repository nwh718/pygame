import pygame


def get_nearest_intersection(x, y, offset_x, offset_y, cell_size, tolerance=15):
    """
    将鼠标点击坐标转换为棋盘上最近的交叉点索引
    
    参数:
        x, y: 鼠标点击的屏幕坐标
        offset_x, offset_y: 棋盘左上角的偏移量
        cell_size: 每个格子的大小
        tolerance: 吸附容差（像素），默认 15px
    
    返回:
        (row, col): 交叉点的索引，如果点击超出容差范围则返回 None
    """
    relative_x = x - offset_x
    relative_y = y - offset_y
    
    col = round(relative_x / cell_size)
    row = round(relative_y / cell_size)
    
    nearest_x = col * cell_size
    nearest_y = row * cell_size
    
    distance = ((relative_x - nearest_x) ** 2 + (relative_y - nearest_y) ** 2) ** 0.5
    
    if distance <= tolerance:
        return (row, col)
    else:
        return None
