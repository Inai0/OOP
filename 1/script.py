class Transport:
    def __init__(self, name, status, kind):
        self.name = name
        self.status = status
        self.kind = kind

    def display(self):
        print(f"{self.name}: {self.status} {self.kind}")

class TruckFactory:
    def create_transport(self, name, status, kind):
        return Transport(name, status, kind)

# Create a factory
factory = TruckFactory()

# Create transport (trucks) using the factory
trucks = []
for i in range(1, 11):
    if i <= 5:
        status = "Доступний"
    else:
        status = "Використовується"
    truck = factory.create_transport(f"Вантажівка {i}", status, "Вантажівка")
    trucks.append(truck)

# Display information about all trucks and their states
for truck in trucks:
    truck.display()