from game.action import Action

class DrawActorsAction:
    
    def __init__(self, output_service):
        
        self._output_service = output_service
    def execute(self, cast):
        self._output_service.clear_screen()
        for i in cast:
            self._output_service.draw_actors(cast[i])
        self._output_service.flush_buffer()
        
        
