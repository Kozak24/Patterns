from behavioral.chain_of_responsibility.logic import BaseHandler


class Starvation(BaseHandler):
    def _process_handle(self) -> None:
        if self._human.hp <= 4:
            self._human.hp = 0
        else:
            self._human.hp -= 4
