"""
CP1404 - Practical
SilverServiceTaxi test
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi"""
    taxi = SilverServiceTaxi("Two", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()

