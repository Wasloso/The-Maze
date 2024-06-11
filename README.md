
# The maze

bla bla bla descripton

# TODO
- Settings
    - Settings manager
    - Settings screen
        - Volume controller
        - optional: Dark/Light mode 
        - ???
- Maze
    - Mazes manager (play_screen)
        - Load saved mazes
        - Add new
        - Delete existing
        - Modify
        - Maze creator
    - Fog of war
    - "AI"
    - should we change cell to be Sprite subclass, so we can use cells.draw() instead of for cell in cells...???
    - POWER UPS IF WE GET BORED
        - can go through a wall
        - teleport closer to the objective
        - extra speeeeeeeeeeed
        - go rainbow like mario
        - spawn an enemy that chases you for idk 10 seconds 
- Assets
    - Graphics
        - Backgrounds
        - Buttons
        - Player
            - optional: Different images for each direction (up, down etc.) 
        - Maze
            - wall
            - floors
            - optional: Different image depending on neighbors eg. when a floor cell has floor cell to the right the floor image is a right-way path etc
        - Objective
    - Sounds:
        - walking
        - background music
        - achieved objective

# TO BE FIXED
- Buttons
    - can't create a sprites.group() as the draw() method doesnt work properly



