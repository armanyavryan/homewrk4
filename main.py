def to_unique(emailList):
    unique_emails = {}
    for string in emailList:
        at = string.find("@")
        plus = string.find("+", 0, at)
        if plus == -1:
            plus = at
        number_of_dots = string.count(".", 0, plus)
        string = string.replace(".", "", number_of_dots)
        formatted = string[0: plus - number_of_dots] + string[at - number_of_dots: ]
        if unique_emails.get(formatted):
            unique_emails[formatted] += 1
        else:
            unique_emails[formatted] = 1
    return unique_emails


emails = ["testemail+david@lee.tcode.com", "test.email+alex@leetcode.com", "test.e.mail+bob.catchy@leetcode.com"]
# print( len(to_unique(emails)))

def match_to_pattern(words, pattern):
    matches = list()
    for w in words:
        d = dict()
        is_matching = True
        for i  in range(len(w)):
            if d.get(w[i]) == None:
                if pattern[i] in d.values():
                    is_matching = False
                    break
                d[w[i]] = pattern[i]
            elif d[w[i]] != pattern[i]:
                is_matching = False
                break
        if is_matching:
            matches.append(w)
    return matches
#
# words = ["abc","deq","mee","aqq","dkd","ccc"]
# pattern = "abb"
# print(match_to_pattern(words, pattern))

#Input: logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5
#Output: [0,2,0,0,0]
def find_UAM(users_log, k):
    users_unique_log = dict()
    for user in users_log:
        if not users_unique_log.get(user[0]):
            users_unique_log[user[0]] = {user[1] }
        else:
            users_unique_log[user[0]].add(user[1])
    uniques = [0] * k
    for user_id in users_unique_log:
        uniques[len(users_unique_log[user_id]) - 1] += 1

    return uniques


logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5

# print(find_UAM(logs, k))


def find_jewels(jewels, stones):
    sum = 0
    jewels_set = set(jewels)
    for c in stones:
         if c in jewels_set:
           sum += 1
    return sum

# print(find_jewels("z", "aAAbbbbZ"))

def binary_to_beautiful(b):
    count = 0
    i = 0
    indexes = []
    while  i < len(b):
        print(i)
        while i < len(b) and b[i] != "0":
            i += 1
        while i < len(b) and b[i] == "0":
            i += 1

        i += 1
        if i < len(b):
            if b[i] == "0":
                indexes.append(i)
                i += 1
                count += 1
                continue
        i += 1
    print(indexes)
    return count

# print("count: ", binary_to_beautiful("0100101010"))


def str_pow(s, k):
    if k == 0:
        return ""
    elif k > 0:
        return s * k
    else:
        n = -len(s) // k
        s0 = s[:n]
        if s.count(s0) == -k:
            return s0
        else:
            return "undefined"

print(str_pow("absabsabs", -2))