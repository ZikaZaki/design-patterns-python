from support.app import CustomerSupport, FILOOrderingStrategy, RadnomOrderingStrategy, random_strategy_creator
from support.ticket import SupportTicket


class BlackHoleStrategy:

  def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
    return []


def main():
  # create the application
  app = CustomerSupport()

  # register a few tickets
  app.add_ticket(SupportTicket("Zack Ali", "My computer makes strang sounds!"))
  app.add_ticket(
      SupportTicket("Linus Sebastian",
                    "I can't upload any videos, please help."))
  app.add_ticket(
      SupportTicket("John Smith",
                    "VSCode doesn't automatically solve my bugs."))

  # process the tickets
  app.process_tickets(random_strategy_creator(seed=1))


if __name__ == "__main__":
  main()
