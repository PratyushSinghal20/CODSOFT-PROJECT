#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    int number, guess, attempts;
    char playAgain;

    
    srand(time(0));

    do {
        number = rand() % 100 + 1; // random number between 1 and 100
        attempts = 0;

        cout << "Welcome to the Number Guessing Game!" << endl;
        cout << "I have selected a number between 1 and 100." << endl;

        do {
            cout << "Enter your guess: ";
            cin >> guess;
            attempts++;

            if (guess > number) {
                cout << "Too high! Try again." << endl;
            } else if (guess < number) {
                cout << "Too low! Try again." << endl;
            } else {
                cout << "Congratulations! You guessed the number in " << attempts << " attempts." << endl;
            }
        } while (guess != number);

        cout << "Do you want to play again? (y/n): ";
        cin >> playAgain;

    } while (playAgain == 'y' || playAgain == 'Y');

    cout << "Thank you for playing!" << endl;

    return 0;
}

