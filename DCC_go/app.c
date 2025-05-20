#include <stdio.h>

int main() {
    int pilihan;
    double a, b, hasil;

    printf("=== Kalkulator Matematika Dasar ===\n");
    printf("1. Penjumlahan\n");
    printf("2. Pengurangan\n");
    printf("3. Perkalian\n");
    printf("4. Pembagian\n");
    printf("Pilih operasi (1-4): ");
    scanf("%d", &pilihan);

    printf("Masukkan angka pertama: ");
    scanf("%lf", &a);
    printf("Masukkan angka kedua: ");
    scanf("%lf", &b);

    switch (pilihan) {
        case 1:
            hasil = a + b;
            printf("Hasil: %.2lf\n", hasil);
            break;
        case 2:
            hasil = a - b;
            printf("Hasil: %.2lf\n", hasil);
            break;
        case 3:
            hasil = a * b;
            printf("Hasil: %.2lf\n", hasil);
            break;
        case 4:
            if (b != 0) {
                hasil = a / b;
                printf("Hasil: %.2lf\n", hasil);
            } else {
                printf("Error: Pembagian dengan nol!\n");
            }
            break;
        default:
            printf("Pilihan tidak valid.\n");
    }

    return 0;
}