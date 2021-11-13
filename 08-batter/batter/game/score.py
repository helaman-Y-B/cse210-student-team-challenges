
class Score:
    def __init__(self, points) -> None:
        self._point = points

    def decrease_score(self):
        self._point -= 1

    def _show_current_score(self):
        return self._point
