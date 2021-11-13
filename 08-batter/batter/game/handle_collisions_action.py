import random
import sys
from game import constants
from game.action import Action
from game.director import Director
from game.output_service import OutputService
from game.score import Score


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.

    Stereotype:
        Controller
    """

    def __init__(self, cast, script, points, screen):
        self.director = Director(cast, script, screen, points)
        self.score = Score(points)
        self.output = OutputService(screen, points)
        self._screen = screen

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        try:
            ball = cast["ball"][0]  # there's only one
            paddle = cast["paddle"][0]  # there's only one
            bricks = cast["brick"]
            for brick in bricks:
                if ball.get_position().equals(
                        brick.get_position()) and brick.get_text() == "*":
                    brick.set_text("")
                    ball.set_velocity(ball.get_velocity().change_y_direction())

            paddle_x = paddle.get_position().get_x()
            paddle_pos_range = range(paddle_x,
                                     paddle_x + len(paddle.get_text()) + 1)
            ball_x = ball.get_position().get_x()

            if ball.get_position().get_y(
            ) == constants.MAX_Y - 1 and ball_x in paddle_pos_range:
                ball.set_velocity(ball.get_velocity().change_y_direction())

            if ball.get_position().get_y(
            ) == constants.MAX_Y - 1 and not ball_x in paddle_pos_range:
                ball.set_velocity(ball.get_velocity().change_y_direction1())

            if ball.get_position().get_y() == 1:
                ball.set_velocity(ball.get_velocity().change_y_direction())

            if ball_x == constants.MAX_X - 1 or ball_x == 1:
                ball.set_velocity(ball.get_velocity().change_x_direction())

        except AttributeError:
            print()
            print("You lost! good luck next time.")
            print()
            sys.exit()

        # paddle_x = paddle.get_position().get_x()
        # paddle_x_len = paddle_x + len(paddle.get_text())
        # if paddle_x <= ball.get_position().get_x() >= paddle_x_len and ball.get_position().get_y() == paddle.get_position().get_y():
        #     ball.set_velocity(ball.get_velocity().change_y_direction())
        # if ball.get_position().get_y()==paddle.get_position().get_y()+1:
        #     ball.set_velocity(ball.get_velocity().change_y_direction1())
