class Gold:
    """
    A Gold Class.
    """
    def __init__(self, name):
        self.name = name
    
    def form(self):
        return f"{self._name} is phisical"


class Crypto:
    """
    A Crypto Class.
    """
    def __init__(self, name):
        self.name = name
    
    def form(self):
        return f"{self._name} is virtual:


def get_asset_class(asset="gold"):
    """
    Factory fuction.
    """
    assets = dict(gold=Gold("Gold"), crypto=Crypto("Bitcoin"))
    return assets[asset]

if __name__ == "__main__":
    g = get_asset_class("gold")
    print(g.form())

    c = get_asset_class("gold")
    print(c.form())