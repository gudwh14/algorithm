def solution(today, terms, privacies):
    answer = []
    terms_info = {}

    today = change(today)

    for term in terms:
        types, period = term.split(' ')
        terms_info[types] = period

    for idx, privacy in enumerate(privacies):
        date, types = privacy.split(' ')
        period = terms_info[types]
        value = change(date)

        valid = value + int(period) * 28
        if valid <= today:
            answer.apend(idx + 1)

    return answer


def change(date):
    year, month, day = map(int, date.split('.'))

    return year * 12 * 28 + month * 28 + day