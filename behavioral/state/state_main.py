from behavioral.state.logic import Ticket


def main() -> None:
    ticket = Ticket("Can't open second instance of program", "John Kendo", "Amanda Dandekar")

    ticket.open()
    ticket.close()
    ticket.in_progress()

    ticket.in_progress()
    ticket.close()
    ticket.resolve()

    ticket.resolve()
    ticket.in_progress()
    ticket.close()

    ticket.close()
    ticket.in_progress()
    ticket.resolve()
    ticket.open()


if __name__ == "__main__":
    main()
