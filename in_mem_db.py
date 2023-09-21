from collections import defaultdict
import re

def solution(queries):
    in_mem_db = defaultdict(dict)    
    query_resp = []
    quot = "\""

    for q in queries:
        if q[0] == "SET":
            if q[1] and q[2] and q[3]:
                if q[1] in in_mem_db.keys():
                    in_mem_db[q[1]].update({q[2]: q[3]})
                else:
                    in_mem_db[q[1]] = {q[2]: q[3]}
                query_resp.append("")
        elif q[0] == "GET":
            if q[1] and q[2]:
                if q[1] in in_mem_db.keys():
                    if q[2] in in_mem_db[q[1]].keys():
                        query_resp.append(in_mem_db[q[1]][q[2]])
                    else:
                        query_resp.append("")
                else:
                    query_resp.append("")
        elif q[0] == "DELETE":
            if q[1] and q[2]:
                if q[1] in in_mem_db.keys():
                    if q[2] in in_mem_db[q[1]].keys():
                        del in_mem_db[q[1]][q[2]]
                        query_resp.append("true")
                    else:
                        query_resp.append("false")
                else:
                    query_resp.append("false")
        elif q[0] == "SCAN":
            if q[1]:
                if q[1] in in_mem_db.keys():
                    temp_query_resp = ''
                    for k,v in in_mem_db[q[1]].items():
                        if temp_query_resp:
                            temp_query_resp += ', ' + k +"(" + v + ')'
                        else:
                            temp_query_resp += k +"(" + v + ')'

                    query_resp.append(quot + temp_query_resp + quot)
                else:
                    query_resp.append("")
        elif q[0] == "SCAN_BY_PREFIX":
            if q[1] and q[2]:
                if q[1] in in_mem_db.keys():
                    scan_pattern = re.search('^(.*)', q[2]).group(1)
                    temp_query_resp = ''
                    for k,v in in_mem_db[q[1]].items():
                        if re.match(scan_pattern, k):
                            if temp_query_resp:
                                temp_query_resp += ', ' + k +"(" + v + ')'
                            else:
                                temp_query_resp += k +"(" + v + ')'
    
                    query_resp.append(quot + temp_query_resp + quot)
                else:
                    query_resp.append("")
        else:
            continue
            
    return query_resp

def main():
    queries = [
            ["SCAN_BY_PREFIX","dept4","fi"], 
            ["SET","dept4","first","1"], 
            ["SET","dept4","second","2"], 
            ["SET","dept4","fifth","5"], 
            ["SCAN_BY_PREFIX","dept4","fi"], 
            ["GET","dept4","first"], 
            ["SCAN_BY_PREFIX","dept4","sec"],
            ["SCAN","dept4"],
            ["SCAN","dept3"],
        ]
    
    print(solution(queries))

if __name__ == "__main__":
    main()
