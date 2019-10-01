import cv2
# - - - - - - - - - - -
from window import Window
from snake import Snake
# - - - - - - - - - - -

# calculate and return center position in window
def center_position(pos):
    return (pos[0] // 2, pos[1] // 2)


# - initilize Window
bg_color = 12
window_size = (800, 600)
# page for drawing objects ( array )
window = Window(window_size, bg_color)

# - center position of window
center_pos = center_position(window.size_window)
# - limit move items inside window
window_limit = [(0, 0), window.size_window]

snake = Snake(window_limit, center_pos, window.bg_color)

while True:
    # check move key
    if snake.direction in snake.directions:
        # clear snake  by default [color clear is bg_color]
        snake.draw(window.window, True)

        # increase length each move and decrease start length
        if snake.start_length > 0:
            snake.start_length -= 1
            snake.add_length()

        # move with snake.direction variable
        snake.move()
        snake.draw(window.window)
    # read key entered and sleep for control (speed snake)
    key = (cv2.waitKey(snake.speed) & 0xFF)

    # action is allowed
    if chr(key) in snake.directions:
        snake.direction = chr(key)
    # increase speed snake
    elif (key == ord('+')):
        if(snake.speed > 10):
            snake.speed -= 5
    # decrease speed snake
    elif (key == ord('-')):
        snake.speed += 5
    # pause game
    elif (key == ord('p')):
        snake.direction = 'p'
    # quit from game
    elif (key == ord('q')):
        break

cv2.destroyAllWindows()
