import string
import random
from typing import List
from abc import ABC, abstractmethod

def generate_id(length=8):
  # helper function for generating an id.
  return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

class SupportTicket:
  id: str
  customer: str
  issue: str

  def __init__(self, customer, issue):
    self.id = generate_id()
    self.customer = customer
    self.issue = issue

class TicketOrderingStrategy(ABC):
  @abstractmethod
  def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
    pass

class FIFOOrderingStrategy(TicketOrderingStrategy):
  def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
    return list.copy()

class FILOOrderingStrategy(TicketOrderingStrategy):
  def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
    list_copy = list.copy()
    list_copy.reverse()
    return list_copy

class RandomOrderingStrategy(TicketOrderingStrategy):
  def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
    list_copy = list.copy()
    random.shuffle(list_copy)
    return list_copy


class CustomerSupport:

  tickets: List[SupportTicket] = []

  def create_ticket(self, customer, issue):
    self.tickets.append(SupportTicket(customer, issue))

  def process_tickets(self, processing_strategy: TicketOrderingStrategy):
    # create the ordered list
    ticket_list = processing_strategy.create_ordering(self.tickets)
    
    # if it's empty don't do anything.
    if len(ticket_list) == 0:
      print("There are no tickets to process, Well done!")
      return


    for ticket in ticket_list:
      self.process_ticket(ticket)

  def process_ticket(self, ticket: SupportTicket):
    print("=====================================")
    print(f"Processing ticket id: {ticket.id}.")
    print(f"Customer: {ticket.customer}.")
    print(f"Issue: {ticket.issue}.")
    print("=====================================")



# create the application
app = CustomerSupport()

# register a few tickets
app.create_ticket("Zack Ali", "I need help with my laptop.")
app.create_ticket("Jane Doe", "I need help with my phone.")
app.create_ticket("Bob Smith", "I need help with my TV.")

# process the tickets
app.process_tickets(RandomOrderingStrategy())
