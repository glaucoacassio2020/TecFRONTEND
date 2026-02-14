def solve():
    greater_heigth = float('-inf')
    lower_heigth = float('inf')
    cnt_female = cnt_male = 0
    sum = 0.0

    for _ in range(15):
        heigth = float(input())
        gen = input()
        if gen.strip().lower() == 'm':
            sum += heigth
            cnt_male += 1
        else:
            cnt_female += 1

        if heigth > greater_heigth:
            greater_heigth = heigth
        if heigth < lower_heigth:
            lower_heigth = heigth

    average = sum / cnt_male if cnt_male > 0 else 0

    print(f"{greater_heigth}, {lower_heigth}")
    print(f"{average:.2f}")
    print(cnt_female)


if __name__ == '__main__':
    solve()
