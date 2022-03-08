from behavioral.chain_of_responsibility.logic import BaseHandler


class Bravery(BaseHandler):
    def _process_handle(self) -> None:
        self._human.attack += 1
