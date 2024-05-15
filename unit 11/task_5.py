class SuperStr(str):

    def is_repeatance(self, s):
        if not s:
            return False
        return self == s * (len(self) // len(s))

    def is_palindrom(self):
        s = self.lower()
        return s == s[::-1]



str1 = SuperStr("abcabcabcabc")
str2 = SuperStr("abc")
str3 = SuperStr("  ")

print(f"'{str1}' кратна '{str2}': {str1.is_repeatance(str2)}")
print(f"'{str1}' кратна '{str3}': {str1.is_repeatance(str3)}")
print(f"'{str2}' кратна '{str1}': {str2.is_repeatance(str1)}")

str1 = SuperStr("A man, a plan, a canal: Panama")
str2 = SuperStr("racecar")
str3 = SuperStr("apple")
str4 = SuperStr("")

print(f"'{str1}' палиндром: {str1.is_palindrom()}")
print(f"'{str2}' палиндром: {str2.is_palindrom()}")
print(f"'{str3}' палиндром: {str3.is_palindrom()}")
print(f"'{str4}' палиндром: {str4.is_palindrom()}")
