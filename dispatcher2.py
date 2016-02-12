from driver import Driver
from rider import Rider


class Dispatcher:
    """A dispatcher fulfills requests from riders and drivers for a
    ride-sharing service.

    When a rider requests a driver, the dispatcher assigns a driver to the
    rider. If no driver is available, the rider is placed on a waiting
    list for the next available driver. A rider that has not yet been
    picked up by a driver may cancel their request.

    When a driver requests a rider, the dispatcher assigns a rider from
    the waiting list to the driver. If there is no rider on the waiting list
    the dispatcher does nothing. Once a driver requests a rider, the driver
    is registered with the dispatcher, and will be used to fulfill future
    rider requests.
    """

    def __init__(self):
        """Initialize a Dispatcher.

        @type self: Dispatcher
        @rtype: None
        """
        # TODO
        self.driverFleet = []
        self.waitingList = []



    def __str__(self):
        """Return a string representation.

        @type self: Dispatcher
        @rtype: str
        """
        # TODO
        pass

    def request_driver(self, rider):
        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: Driver | None
        """
        # TODO
        if self.driverFleet == []:
            self.waitingList.append(rider)
            return None
        else:
            nearestDriver = self.driverFleet[0]
            #Checking for which driver is closest to the rider.
            for driver in self.driverFleet:
                if driver.get_travel_time(rider.destination) < nearestDriver.get_travel_time(rider.destination):
                    nearestDriver = driver
        return nearestDriver


    def request_rider(self, driver):
        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        @type self: Dispatcher
        @type driver: Driver
        @rtype: Rider | None
        """
        # TODO
        if driver not in self.driverFleet:
            self.driverFleet.append(driver)
        if self.waitingList == []:
            return None
        else:
            longestWaitingRider = self.waitingList[0]
            for rider in self.waitingList:
                if longestWaitingRider.patience < rider.patience:
                    #NOT FINNISHED





    def cancel_ride(self, rider):
        """Cancel the ride for rider.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: None
        """
        # TODO
        pass
