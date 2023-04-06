def solution(alp, cop, problems):
    answer = 0
    max_req_alp, max_req_cop = 0, 0

    for problem in problems:
        max_req_alp = max(max_req_alp, problem[0])
        max_req_cop = max(max_req_cop, problem[1])

    if alp >= max_req_alp and cop >= max_req_cop:
        return answer

    alp = min(alp, max_req_alp)
    cop = min(cop, max_req_cop)

    # DP
    DP = [[float('+inf')] * 151 for _ in range(151)]
    DP[alp][cop] = 0

    for algo in range(alp, max_req_alp + 1):
        for code in range(cop, max_req_cop + 1):
            if algo + 1 <= max_req_alp:
                DP[algo + 1][code] = min(DP[algo + 1][code], DP[algo][code] + 1)
            if code + 1 <= max_req_cop:
                DP[algo][code + 1] = min(DP[algo][code + 1], DP[algo][code] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                # 문제 풀기 가능
                if algo >= alp_req and code >= cop_req:
                    # 문제 푼것과 현재 min 값
                    new_algo = min(algo + alp_rwd, max_req_alp)
                    new_code = min(code + cop_rwd, max_req_cop)

                    DP[new_algo][new_code] = min(DP[new_algo][new_code], DP[algo][code] + cost)

    return DP[max_req_alp][max_req_cop]