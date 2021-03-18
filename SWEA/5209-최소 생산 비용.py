import sys
sys.stdin = open("sample_input.txt")


class Charge:
    def __init__(self):
        self.N = int(input())
        self.minPrice = 999999
        self.map = []
        self.isUse = list([False] * self.N)

        for _ in range(self.N):
            self.map.append(list(map(int, input().split())))

        self.get_min_price(0, 0)

    def get_min_price(self, product, charge):
        if product == self.N:
            self.minPrice = min(self.minPrice, charge)
            return

        if charge >= self.minPrice:
            return

        for companyNum in range(self.N):
            if self.isUse[companyNum]:
                continue

            self.isUse[companyNum] = True
            self.get_min_price(product + 1, charge + self.map[product][companyNum])
            self.isUse[companyNum] = False


T = int(input())
for t in range(1, T+1):
    charge = Charge()

    print(f"#{t} {charge.minPrice}")