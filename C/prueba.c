// programa_ejemplo.c
// Ejemplo en C: lee n números, los ordena, calcula promedio y muestra primos.

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Prototipos
void leer_numeros(int *arr, int n);
void bubble_sort(int *arr, int n);
double promedio(int *arr, int n);
bool es_primo(int x);
void mostrar_array(int *arr, int n);

int main(void) {
    int n;

    printf("Cuantos numeros vas a ingresar? ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Entrada invalida. Saliendo.\n");
        return 1;
    }

    int *arr = malloc(sizeof(int) * n);
    if (!arr) {
        perror("malloc");
        return 1;
    }

    leer_numeros(arr, n);

    printf("\nNumeros ingresados:\n");
    mostrar_array(arr, n);

    bubble_sort(arr, n);
    printf("\nNumeros ordenados (ascendente):\n");
    mostrar_array(arr, n);

    double avg = promedio(arr, n);
    printf("\nPromedio: %.2f\n", avg);

    printf("\nNumeros primos en la lista:\n");
    bool found = false;
    for (int i = 0; i < n; ++i) {
        if (es_primo(arr[i])) {
            printf("%d ", arr[i]);
            found = true;
        }
    }
    if (!found) printf("Ninguno");
    printf("\n");

    free(arr);
    return 0;
}

void leer_numeros(int *arr, int n) {
    for (int i = 0; i < n; ++i) {
        printf("Numero %d: ", i + 1);
        while (scanf("%d", &arr[i]) != 1) {
            // limpiar entrada incorrecta
            int c;
            while ((c = getchar()) != EOF && c != '\n');
            printf("Entrada no valida. Ingresa un entero para el numero %d: ", i + 1);
        }
    }
}

void bubble_sort(int *arr, int n) {
    for (int i = 0; i < n - 1; ++i) {
        for (int j = 0; j < n - 1 - i; ++j) {
            if (arr[j] > arr[j + 1]) {
                int tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;
            }
        }
    }
}

double promedio(int *arr, int n) {
    long long suma = 0;
    for (int i = 0; i < n; ++i) suma += arr[i];
    return (double)suma / n;
}

bool es_primo(int x) {
    if (x <= 1) return false;
    if (x <= 3) return true;
    if (x % 2 == 0) return false;
    for (int i = 3; i * i <= x; i += 2)
        if (x % i == 0) return false;
    return true;
}

void mostrar_array(int *arr, int n) {
    for (int i = 0; i < n; ++i) printf("%d ", arr[i]);
    printf("\n");
}
