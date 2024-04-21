#include <iostream>
#include <string>

// Using namespace directive
using namespace std;

// Base class: Vehicle
class Vehicle {
protected:
    string brand;

public:
    // Constructor
    Vehicle(string b) : brand(b) {
        cout << "Vehicle constructor called for brand: " << brand << endl;
    }

    // Virtual method to display information
    virtual void displayInfo() {
        cout << "Brand: " << brand << endl;
    }

    // Destructor
    virtual ~Vehicle() {
        cout << "Vehicle destructor called for brand: " << brand << endl;
    }

    // Static member to keep track of the total number of vehicles
    static int totalVehicles;

    // Friend function to access private members
    friend void friendFunction(Vehicle&);
};

// Initializing static member outside the class
int Vehicle::totalVehicles = 0;

// Derived class: Car (inherits from Vehicle)
class Car : public Vehicle {
private:
    int year;

public:
    // Constructor
    Car(string b, int y) : Vehicle(b), year(y) {
        cout << "Car constructor called for brand: " << brand << ", year: " << year << endl;
        totalVehicles++;  // Increment totalVehicles when a new vehicle is created
    }

    // Overridden method to display information
    void displayInfo() override {
        cout << "Car Information - Brand: " << brand << ", Year: " << year << endl;
    }

    // Destructor
    ~Car() override {
        cout << "Car destructor called for brand: " << brand << ", year: " << year << endl;
        totalVehicles--;  // Decrement totalVehicles when a car is destroyed
    }
};

// Friend function definition
void friendFunction(Vehicle& vehicle) {
    // Accessing the protected member brand from the friend function
    cout << "Friend Function: Brand of the vehicle is " << vehicle.brand << endl;
}

int main() {
    // Creating a Car object using the constructor
    Car myCar("Toyota", 2022);

    // Displaying information about the car
    cout << "Car Information: ";
    myCar.displayInfo();

    // Displaying total number of vehicles
    cout << "Total number of vehicles: " << Vehicle::totalVehicles << endl;

    // Using friend function to access private members
    myCar.~Car();
    friendFunction(myCar);
    return 0;
}