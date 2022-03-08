from behavioral.chain_of_responsibility.logic import BaseHandler


class Satiety(BaseHandler):
    def _process_handle(self) -> None:
        self._human.hp += 5
