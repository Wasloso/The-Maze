from heapq import heappop, heappush

from maze import Maze


def heuristic(start_pos, end_pos):
    return abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1])


def reconstruct_path(came_from, current_pos):
    total_path = [current_pos]
    while current_pos in came_from:
        current_pos = came_from[current_pos]
        total_path.append(current_pos)
    return total_path


def a_star(maze: Maze):
    player_pos, objective_pos = maze.player_start_pos, maze.objective_position_pos
    print(player_pos, objective_pos)
    open_set = [(0, player_pos)]
    came_from = {}
    cost_so_far = {player_pos: 0}

    while open_set:
        cost, current_pos = heappop(open_set)
        print(current_pos)
        if current_pos == objective_pos:
            return reconstruct_path(came_from, current_pos)

        # Find if cell is collidable in each direction [TOP, RIGHT, LEFT, BOTTOM]
        for next_pos in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
            new_pos = tuple(map(sum, zip(current_pos, next_pos)))
            if 0 <= new_pos[0] < maze.rows and 0 <= new_pos[1] < maze.columns:
                if maze.grid[new_pos[0]][new_pos[1]].collidable == 0:
                    new_cost = cost_so_far.get(current_pos) + 1
                    if new_pos not in cost_so_far or new_cost < cost_so_far[new_pos]:
                        cost_so_far[new_pos] = new_cost
                        priority = new_cost + heuristic(new_pos, objective_pos)
                        heappush(open_set, (priority, new_pos))
                        came_from[new_pos] = current_pos

    # Failure, goal was never reached
    return None
