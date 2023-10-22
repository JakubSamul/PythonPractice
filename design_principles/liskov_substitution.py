class KitchenAppliance():
    def on():
        pass 

    def off():
        pass


class KitchenApplianceWithTemp(KitchenAppliance):
    def set_temperature():
        pass


class Toaster(KitchenApplianceWithTemp):
    def on():
        # turn on toaster
        pass

    def off():
        # turn off on toaster
        pass

    def set_temperature():
        # set temp on toaster
        pass


class Juice(KitchenAppliance):
    def on():
        # turn on juice
        pass

    def off():
        # turn off jiuce
        pass