user_count = "juho"
if user_count =="admin":

    print("관리자님 안녕하세요")

else:

    print("일반 사용자입니다")

user = "human"
if user == "human":

    print("맞습니다")

else:
    print("틀립니다")

user2 = "amelia"
if user2 == "amelia":
    print("amelia님 환영합니다")

else:
    print("amelia님이 맞지 않습니다")

students = [{"name":"지영","score":95},{"name":"주호","score":75}]
for s in students:
    if s["score"] >= 85:
        result = "승급"
    else:
        result = "강등"
print(f"{s['name']}: {result}")

def  calcuclate_stats(score_ list):




