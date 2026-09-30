def calculate_stats(score_list):
    total = sum(score_list)
    avg = total / len(score_list)
    return total, avg

total, avg = calculate_stats([75, 65, 90])
print(f"총점: {total}, 평균: {avg:.2f}")



