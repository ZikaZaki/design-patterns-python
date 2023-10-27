from collections.abc import Callable
from dataclasses import dataclass
import random
# from abc import ABC, abstractmethod
from typing import Optional, Protocol

from support.ticket import SupportTicket

# we can also use the Callable to define the type of TicketOrderingStrategy
TicketOrderingStrategy = Callable[[list[SupportTicket]], list[SupportTicket]]

# class TicketOrderingStrategy(Protocol):

#   # def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
#   def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
#     """Returns an ordered list of tickets."""
#     ...


class FIFOOrderingStrategy:

  def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
    return tickets.copy()


class FILOOrderingStrategy:

  def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
    return list(reversed(tickets))


# a way to add extra parameters with functions is using closures
def random_strategy_creator(seed: Optional[int] = None) -> TicketOrderingStrategy:
  def random_strategy(tickets: list[SupportTicket]) -> list[SupportTicket]:
    random.seed(seed)
    return random.sample(tickets, len(tickets))

  return random_strategy


# to add extra parameters like settings/configs
@dataclass
class RadnomOrderingStrategy:
  seed: Optional[int] = None

  def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
    random.seed(self.seed)
    return random.sample(tickets, len(tickets))


class CustomerSupport:

  def __init__(self):
    self.tickets: list[SupportTicket] = []

  def add_ticket(self, ticket: SupportTicket):
    self.tickets.append(ticket)

  def process_tickets(self, processing_strategy: TicketOrderingStrategy):
    # create the ordered list of tickets
    ticket_list = processing_strategy(self.tickets)

    # if it's empty, don't do anything
    if len(ticket_list) == 0:
      print("There are no tickets to process. Well done!")
      return

    # go through the tickets list and process each ticket
    for ticket in ticket_list:
      print(f"Processing ticket {ticket.id}...")
      ticket.process()

    # clear the tickets list
    self.tickets = []
