def generate_checkerboard(width, height, color1, color2):
    """
    Generate a checkerboard pattern of given width and height using two colors.
    The pattern alternates colors across both rows and columns.

    Returns:
        A 2D list (height x width) where each element is color1 or color2.
    """
    cA = color1
    cB = color2
    board = []
    for y in range(height):
        row = []
        for x in range(width):
            if (x + y) % 2 == 0:
                row.append(cA)
            else:
                row.append(cB)
        board.append(row)
    return board