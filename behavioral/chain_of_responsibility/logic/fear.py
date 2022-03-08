from behavioral.chain_of_responsibility.logic import BaseHandler


class Fear(BaseHandler):
    def _process_handle(self) -> None:
        if self._human.attack >= 1:
            self._human.attack -= 1
