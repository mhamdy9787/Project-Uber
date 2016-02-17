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
        self.driverFleet = []#initializes a new list of drivers
        self.availableDriver = []#Initializes a new list of unoccupied drivers
        self.waitingList = []#List of waiting customers



    def __str__(self):
        """Return a string representation.

        @type self: Dispatcher
        @rtype: str
        >>>self.driverFleet = ["bob","john","jimmy"]
        >>>self.availableDriver = ["john"]
        >>>self.waitingList = ["darren","wayne"]
        >>>__str__()
        ""Amount of Drivers: 3\nAmount of Available Drivers: 1\nAmount of Waiting Customers:2"
        # TODO
        return ("Amount of Drivers: {0}\n" #The number of drivers
                "Amount of Available Drivers: {1}\n"#The number of available drivers
                "Amount of Waiting Customers:{2}", format(len(self.driverFleet),len(self.availableDriver),len(self.waitingList))
                #^The number of waiting customers
    def request_driver(self, rider):
        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: Driver | None
        >>>self.waitingList = ["jack"]
        >>>self.availableDriver = ["John"]
        >>>request_driver("jack")
        "John"
        >>>self.waitingList = ["jack"]
        >>>self.availableDriver = []
        >>>request_driver("jack")
        None
        """
        # TODO
        if self.availableDriver == []:#If there are no avialble drivers then add the rider to the waiting list and return None
            self.waitingList.append(rider)
            return None
        else:#Else assign the rider to a driver by returning a driver
            nearestDriver = self.availableDriver[0]
            #Checking for which driver is closest to the rider.
            for driver in self.availableDriver:
                print(nearestDriver , nearestDriver.get_travel_time(rider.location) )
                print(driver,driver.get_travel_time(rider.location))
                if driver.get_travel_time(rider.location) < nearestDriver.get_travel_time(rider.location):
                    nearestDriver = driver
        return nearestDriver


    def request_rider(self, driver):
        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        @type self: Dispatcher
        @type driver: Driver
        @rtype: Rider | None
        >>>self.waitingList = ["jack"]
        >>>self.availableDriver = ["John"]
        >>>request_rider("John")
        "jack"
        >>>self.waitingList = []
        >>>self.availableDriver = ["John"]
        >>>request_rider("John")
        None
        >>>self.waitingList = []
        >>>self.availableDriver = ["John"]
        >>>request_rider("John")
        None
        
        """
        # TODO
        if driver not in self.driverFleet:#If isnt already in the list append them to the genral list and the available list
            self.driverFleet.append(driver)
            self.availableDriver.append(driver)
        if self.waitingList == []:#If there are no riders return None
            return None
        else:
            return self.waitingList[0]#If there is a rider then use then assign the first person in the queue

    def activateDriver(self,driver):
        #TODO

        self.availableDriver.append(driver)
        print(self.availableDriver)
    def deActivateDriver(self,driver):
        #TODO

        self.availableDriver.remove(driver)

    def cancel_ride(self, rider):
        """Cancel the ride for rider.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: None
        """
        # TODO
        if rider in self.waitingList:
            self.waitingList.remove(rider)

