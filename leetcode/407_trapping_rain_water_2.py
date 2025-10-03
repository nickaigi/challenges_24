class Solution:

    # class to store the height and coordinates of a cell in the grid
    class Cell:
        def __init__(self, height, row, col) -> None:
            self.height = height
            self.row = row
            self.col = col

        # comparison method for the priority queue (min-heap)
        def __lt__(self, other):
            return self.height < other.height
    def _is_valid_cell(self, row, col, num_of_rows, num_of_cols):
        return 0 <= row < num_of_rows and 0 <= col < num_of_cols

    def trapRainWater(self, height_map):
        pass
