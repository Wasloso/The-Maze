from heapq import heappop, heappush

# Not modular import to avoid circular import
from .maze import Maze
from .player import Player


class Solver:
    def __init__(self, maze: Maze, player: Player):
        self.maze = maze
        self.player = player
        self.solution = self.a_star()
        self.last_dir = None
        print(self.solution[0])

    def a_star(self):
        def heuristic(start_pos, end_pos):
            return abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1])

        def reconstruct_path(came_from, current_pos):
            total_path = [current_pos]
            while current_pos in came_from:
                current_pos = came_from[current_pos]
                total_path.append(current_pos)
            total_path.reverse()
            return total_path

        player_pos, objective_pos = self.maze.player_start_pos, self.maze.objective_position_pos
        open_set = [(0, player_pos)]
        came_from = {}
        cost_so_far = {player_pos: 0}

        while open_set:
            cost, current_pos = heappop(open_set)
            if current_pos == objective_pos:
                return reconstruct_path(came_from, current_pos)

            # Find if cell is collidable in each direction [TOP, RIGHT, LEFT, BOTTOM]
            for next_pos in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                new_pos = tuple(map(sum, zip(current_pos, next_pos)))
                if 0 <= new_pos[1] < self.maze.rows and 0 <= new_pos[0] < self.maze.columns:
                    if self.maze.grid[new_pos[0]][new_pos[1]].collidable == 0:
                        new_cost = cost_so_far.get(current_pos) + 1
                        if new_pos not in cost_so_far or new_cost < cost_so_far[new_pos]:
                            cost_so_far[new_pos] = new_cost
                            priority = new_cost + heuristic(new_pos, objective_pos)
                            heappush(open_set, (priority, new_pos))
                            came_from[new_pos] = current_pos

        # Failure, goal was never reached
        return None

    def update(self):
        if self.solution:
            target_pos = self.solution[0]
            if self.player.rect.center != self.maze.get_rect_position(*target_pos):
                player_x, player_y = self.maze.get_cell_index(*self.player.rect.center)
                player_x = target_pos[1] - player_x
                player_y = target_pos[0] - player_y
                if (player_x, player_y) == (0, 0):
                    self.player.move(self.last_dir)
                else:
                    self.last_dir = (player_x, player_y)
                    self.player.move((player_x, player_y))
            else:
                self.solution.pop(0)
