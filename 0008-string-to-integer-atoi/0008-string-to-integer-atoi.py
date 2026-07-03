class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # Check sign
        sign = 1
        if i < n:
            if s[i] == "-":
                sign = -1
                i += 1
            elif s[i] == "+":
                i += 1

        # Build the number
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        # Apply sign
        num = num * sign

        # Clamp to 32-bit integer range
        if num < -2147483648:
            return -2147483648
        if num > 2147483647:
            return 2147483647

        return num