class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    
    def print_peceipt(self):
        print(f"distance{self.distance} km")
        print(f"rate{self.rate_per_km}")
        print(f"fare{self.fare}")


def main():
    ride1 = TaxiRide(rate_per_km=2)
    ride2 = TaxiRide(rate_per_km=2.5)
    ride1.calculate_fare(distance=15)
    ride2.calculate_fare(distance=25)

    # Print receipts
    print("Receipt for Ride 1:")
    ride1.print_peceipt()
    print("Receipt for Ride 2:")
    ride2.print_peceipt()

    

if __name__ == "__main__":
    main()
