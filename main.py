from lib import multiply, power, subtract

def main():

    print("=== Демонстрація імпорту модулів ===\n") 
    
    res_mult = multiply(6, 7)
    print(f"Добуток чисел 6 та 7: {res_mult}")

    res_pow = power(2, 5)
    print(f"Число 2 у степені 5: {res_pow}")

    res_sub = subtract(20, 8)
    print(f"Різниця чисел 20 та 8: {res_sub}")

if __name__ == "__main__":
    main()