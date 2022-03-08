from behavioral.chain_of_responsibility.logic import BaseHandler


class DefenseTeardown(BaseHandler):
    def _process_handle(self) -> None:
        if self._human.defense >= 1:
            self._human.defense -= 1
