class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # % 10 to get digit, // 10 get carry
        if num1 == "0" or num2 == "0":
            return "0"
        n1, n2 = len(num1), len(num2)
        digits = [0] * (n1 + n2) # assign max digit 
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(n1):
            for i2 in range(n2):
                num_mul = int(num1[i1]) * int(num2[i2])
                digits[i1 + i2] += num_mul
                digits[i1 + i2 + 1] += digits[i1 + i2] // 10 # carry
                digits[i1 + i2] =  digits[i1 + i2] % 10 # finally get digit
        # remove the leading 0:
        for j in range(len(digits)-1, -1, -1):
            if digits[j] == 0:
                digits.pop()
            else:
                break
        # for result
        res = ""
        for j in range(len(digits)-1, -1, -1):
            res += str(digits[j])
        return res


        # can also use map: res = map(str, res[beg:])






        