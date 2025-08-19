#include <iostream>
#include <vector>
void menu()
{
    std::cout << "Welcome to the Numerical Exercises Program!\n";
    std::cout << "Please select an exercise to run:\n";
    std::cout << "1) Sum of Even / Product of Odd.\n";
    std::cout << "2) Organize array.\n";
    std::cout << "3) Calculator.\n";
    std::cout << "4) Exit.\n--> ";
}
void exercise_sum_even_product_odd()
{
    // Sum of Even / Product of Odd.
    int n, n1, sum_even = 0, product_odd = 1;
    std::vector<int> numbers;
    while (n1 == 0)
    {
        std::cout << "Type the number of elements: ";
        std::cin >> n;
        if (n > 0)
        {
            n1 = 1;
        }
        else
        {
            std::cout << "Please enter a positive number.\n";
        }
    }
    std::cout << "Type the elements:\n";
    for (int i = 0; i < n; ++i)
    {
        int num;
        std::cin >> num;
        numbers.push_back(num);
        if (num % 2 == 0)
        {
            sum_even += num;
        }
        else
        {
            product_odd *= num;
        }
    }
    std::cout << "Sum of even numbers: " << sum_even << "\n";
    std::cout << "Product of odd numbers: " << product_odd << "\n";
}
void organize_array()
{
    std::vector<int> numbers(10);
    std::cout << "Write an array of 10 numbers:\n";
    for (int i = 0; i < 10; i++)
    {
        std::cin >> numbers[i];
    }
    // Ordenar el array usando el algoritmo de burbuja
    for (int i = 0; i < 10 - 1; i++)
    {
        for (int j = 0; j < 10 - i - 1; j++)
        {
            if (numbers[j] > numbers[j + 1])
            {
                // Intercambiar los elementos
                int temp = numbers[j];
                numbers[j] = numbers[j + 1];
                numbers[j + 1] = temp;
            }
        }
    }
    std::cout << "Array organized\n";
    for (int i = 0; i < 10; i++)
    {
        std::cout << numbers[i] << " ";
    }
}

void calculator(){
    double num1, num2;
    char op;
    std::cout << "Enter first number: ";
    std::cin >> num1;
    std::cout << "Enter second number: ";
    std::cin >> num2;
    std::cout << "Enter operator (+, -, *, /): ";
    std::cin >> op;

    switch (op)
    {
        case '+':
            std::cout << "Result: " << num1 + num2 << "\n";
            break;
        case '-':
            std::cout << "Result: " << num1 - num2 << "\n";
            break;
        case '*':
            std::cout << "Result: " << num1 * num2 << "\n";
            break;
        case '/':
            if (num2 != 0)
                std::cout << "Result: " << num1 / num2 << "\n";
            else
                std::cout << "Error: Division by zero.\n";
            break;
        default:
            std::cout << "Invalid operator.\n";
    }
}

int main()
{
    menu(); // Show the menu
    int choice;
    std::cin >> choice;
    switch (choice)
    {
    case 1:
        std::cout << "Running Sum of Even / Product of Odd exercise.\n";
        exercise_sum_even_product_odd();
        break;
    case 2:
        std::cout << "Running Organize array exercise.\n";
        organize_array();
        break;
    case 3:
        std::cout << "Running Calculator exercise.\n";
        calculator();
    case 4:
        std::cout << "Exiting the program. Goodbye!\n";
        break;
    default:
        std::cout << "Invalid choice, please try again.\n";
        main(); // Restart the menu
    }
}
