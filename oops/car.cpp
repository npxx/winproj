#include <iostream>
#include <string>
using namespace std;

// Class declaration
class Car {
public:
    // Attributes
    string model;
    int year;
    float speed;  // New attribute for speed

    // // Static member to keep track of the total number of cars
    static int totalCars;

    // Constructor to initialize attributes
    Car(string modelName, int modelYear) {
        model = modelName;
        year = modelYear;
        speed = 0.0;  // Initialize speed to 0
        totalCars++;  // Increment totalCars when a new car is created
    }

    void displayInfo() {
        cout << "Model: " << model << ", Year: " << year << ", Speed: " << speed << " km/h" << endl;
    }

    void accelerate(float acceleration) {
        speed += acceleration;
        cout << "The car is accelerating. Current speed: " << speed << " km/h" << endl;
    }
};

// Initializing static member outside the class
int Car::totalCars = 0;

int main() {
    // Creating two objects of the Car class using the constructor
    Car car1("Toyota", 2022);
    Car car2("Honda", 2020);

    // Calling the displayInfo method for each car
    cout << "Car 1 Information: ";
    car1.displayInfo();

    cout << "Car 2 Information: ";
    car2.displayInfo();

    // Accelerating the first car
    car1.accelerate(20.5);

    // Displaying total number of cars
    cout << "Total number of cars: " << Car::totalCars << endl;

    return 0;
}
