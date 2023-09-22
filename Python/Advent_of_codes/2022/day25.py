with open('day25.txt') as f:
    read_data = f.read().strip().split('\n')


class SnafuConverter:
    def __init__(self, nums):
        self.nums = nums[::]

    def main(self):
        sum_fuels = 0
        for n in self.nums:
            sum_fuels += self.snafu_to_decimal(n)
        print(sum_fuels)
        print(self.decimal_to_snafu(sum_fuels))

    def snafu_to_decimal(self, num: str) -> int:
        dec = []
        for i, j in enumerate(num[::-1]):
            if j == '-':
                dec.append(5**i * -1)
            elif j == '=':
                dec.append(5**i * -2)
            else:
                dec.append(5**i * int(j))
        return sum(dec)

    def decimal_to_snafu(self, num: int) -> str:
        snafu = []
        quotient = num
        while quotient:
            remainder = quotient % 5
            quotient = quotient // 5
            snafu.append(remainder)
        for i, j in enumerate(snafu):
            if j in [3, 4, 5]:
                if j == 3:
                    snafu[i] = '='
                elif j == 4:
                    snafu[i] = '-'
                elif j == 5:
                    snafu[i] = '0'
                if i < len(snafu) - 1:
                    snafu[i + 1] += 1
                else:
                    snafu.append('1')
            else:
                snafu[i] = str(snafu[i])
            # print(snafu)
        return ''.join(snafu[::-1])


if __name__ == '__main__':
    c = SnafuConverter(read_data)
    c.main()
