#
# A few examples using recursion
#

# 3이 n에 몇 번 등장하는지 카운트하는 함수입니다
# string 관련 함수를 사용하면 안됩니다
# 0 contains 0 threes
# 7 contains 0 threes
# 3 contains 1 threes
# 13 contains 1 threes
# 33333 contains 5 threes
# 123454321 contains 2 threes
# 12333983393893 contains 7 threes
def number_of_threes(n):
    raise NotImplementedError

# palindrome은 뒤집어읽어도 같은 string을 말합니다
# 주어진 s가 palindrome인지 True, False로 리턴하세요
# 'abba' is a palindrome? True
# 'omma' is a palindrome? False
# 'a' is a palindrome? True
# '' is a palindrome? True
# 'ere' is a palindrome? True
# 'era' is a palindrome? False
# 'amanaplanacanalpanama' is a palindrome? True
def palindrome(s):
    raise NotImplementedError

# 주어진 수 n을 log2를 취한 integer를 반환하는 함수입니다.
# 소숫점 아랫값은 내림합니다.
# binLog(7) = 2
# binLog(8) = 3
# binLog(17) = 4
# binLog(1000) = 9
# binLog(1024) = 10
# binLog(2500) = 11
# binLog(1000000) = 19
# binLog(1000000000) = 29
def bin_log(n):
    raise NotImplementedError

if __name__ == "__main__":
    for n in [ 0, 7, 3, 13, 33333, 123454321, 12333983393893 ]:
        print("%d contains %d threes" % (n, number_of_threes(n)))
    print()
    for s in ["abba", "omma", "a", "", "ere", "era", 
              "amanaplanacanalpanama" ]:
        print("'%s' is a palindrome? %s" % (s, palindrome(s)))
    print()
    for n in [7, 8, 17, 1000, 1024, 2500, 1000000, 1000000000]:
        print("binLog(%d) = %d" % (n, bin_log(n)))