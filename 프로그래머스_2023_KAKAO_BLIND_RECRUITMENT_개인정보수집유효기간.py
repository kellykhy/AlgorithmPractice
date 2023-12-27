# 프로그래머스 2023 KAKAO BLIND RECRUITMENT 개인정보 수집 유효기간

def solution(today, terms, privacies):
    answer = []
    # today
    today = list(map(int, today.split('.')))
    # terms->terms_dict
    terms_dict = {}
    for term in terms:
        tmp = term.split()
        terms_dict[tmp[0]] = int(tmp[1]) * 28
    # privacies
    for i in range(len(privacies)):
        start_date, type = privacies[i].split(' ')
        start_date_lst = list(map(int, start_date.split('.')))
        start_date_day = start_date_lst[0] * 336 + start_date_lst[1] * 28 + start_date_lst[2]
        today_day = today[0] * 336 + today[1] * 28 + today[2]
        if (start_date_day + terms_dict[type] <= today_day):
            answer.append(i+1)
    return answer

today_ex = "2020.01.01"	
terms_ex = ["Z 3", "D 5"]	
privacies_ex = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
print(solution(today_ex, terms_ex, privacies_ex))