"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
@type WAITING: str
    A constant used for the waiting rider status.
@type CANCELLED: str
    A constant used for the cancelled rider status.
@type SATISFIED: str
    A constant used for the satisfied rider status
"""

WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Rider:

    def __init__(self,identifier,status,destination,origin,patience):


        self.id = identifier
        self.status = status
        self.destination = destination #locationClass
        self.location = origin #locationClass
        self.patience = patience

    def updateStatus(self,newStatus):

        self.status = newStatus

    def __str__(self):
        return "{} {}".format(self.id,self.status)
