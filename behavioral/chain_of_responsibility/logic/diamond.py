from behavioral.chain_of_responsibility.logic import BaseHandler


class Diamond(BaseHandler):
    def _process_handle(self) -> None:
        self._human.defense += 1
