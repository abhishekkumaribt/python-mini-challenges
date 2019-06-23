# --------------
#Code starts here
def palindrome(num):
    num+=1
    while str(num)!=str(num)[-1::-1]:
        num+=1
    return num


# --------------
#Code starts here
def each_char_count(str_1):
    count = {}
    for item in str_1.lower():
        if item in count.keys():
            count[item] += 1
        else:
            count[item] = 1
    return count

def a_scramble(str_1, str_2):
    res = False
    str_1 = each_char_count(str_1)
    str_2 = each_char_count(str_2)
    for key, value in str_2.items():
        if key in str_1.keys() and str_1[key]>=value:
            res = True
        else:
            res = False
            return res
    return res


# --------------
#Code starts here
def check_fib(num):
    res = -1
    s1 = 0
    s2 = 1
    while res<num:
        res = s1 + s2
        if res==num:
            return True
        elif res>num:
            return False
        s1 = s2
        s2 = res


# --------------
#Code starts here
def compress(word):
    word = word.lower()
    res = ""
    ch = word[0]
    num = 1
    index = 0
    while index<len(word)-1:
        if ch==word[index+1]:
            num += 1
            index += 1
        else:
            res += ch+str(num)
            index += 1
            ch = word[index]
            num = 1
    res += ch+str(num)
    return res


# --------------
#Code starts here
def k_distinct(string,k):
    return len(set(string.lower()))==k


