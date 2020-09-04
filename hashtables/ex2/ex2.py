#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    ticket_dict = {}

    for ticket in tickets:  # create dict, for each source:destination
        if ticket not in ticket_dict:
            ticket_dict[ticket.source] = ticket.destination

    # starting point should have no source. since its the start
    starting_point = ticket_dict['NONE']
    # create the route, starting with starting_point
    route = [starting_point]
    # link the route together. each stop is based off the source. which is the destination of the previous stop
    for x in range(length-1):
        route.append(ticket_dict[route[x]])

    return route
