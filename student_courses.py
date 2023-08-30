import re

def solution(queries):
    course_id_pattern='^[a-zA-Z]{3}[0-9]{3}'
    uniq_course_ids = set()
    uniq_course_names = set()
    course_id_credits = {}
    student_course_ids = {} 
    student_course_creds = {}
    student_pairs = {}
    query_res = []

    for q in queries:
        if q[0] == "CREATE_COURSE":
            if re.match(course_id_pattern, q[1]):
                if q[1] not in uniq_course_ids and q[2] not in uniq_course_names:
                    uniq_course_ids.add(q[1])
                    uniq_course_names.add(q[2])
                    course_id_credits[q[1]] = int(q[3])
                    query_res.append("true")
                else:
                    query_res.append("false")
            else:
                query_res.append("false")
        elif q[0] == "REGISTER_FOR_COURSE":
            if q[2] in uniq_course_ids:
                if q[1] in student_course_ids.keys():
                    if q[2] not in student_course_ids[q[1]]:
                        student_course_ids[q[1]].append(q[2])
                    else:
                       query_res.append("false") 
                else:
                    student_course_ids[q[1]] = [q[2]]
                
                if q[1] in student_course_creds.keys():
                    student_course_creds[q[1]] += course_id_credits[q[2]]
                else:
                    student_course_creds[q[1]] = course_id_credits[q[2]]

                if student_course_creds[q[1]] <= 24:
                    for k,v in student_course_ids.items():
                        if k != q[1]:
                            if q[2] in v:
                                student_pairs[k] = q[1]
                    query_res.append("true")
                else:
                    student_course_creds[q[1]] -= course_id_credits[q[2]]
                    if  student_course_creds[q[1]] < 0:
                          student_course_creds[q[1]] = 0
                    student_course_ids[q[1]].pop(len(student_course_ids[q[1]])-1)
                    query_res.append("false")
            else:
                query_res.append("false")
        elif q[0] == "GET_STUDENT_PAIRS":
            for k,v in student_pairs.items():
                query_res.append([k,v])
        else:
            query_res.append("false")
    
    return query_res

def main():
    queries = [
        ["CREATE_COURSE", "CSE100", "Computer Science Fundamentals", "6"],
        ["CREATE_COURSE", "CSE150", "Data Structures", "10"],
        ["CREATE_COURSE", "CSE200", "Artificial Intelligence", "12"],
        ["CREATE_COURSE", "CSE250", "Machine Learning Fundamentals", "10"],
        ["REGISTER_FOR_COURSE", "st001", "CSE100"],
        ["REGISTER_FOR_COURSE", "st002", "CSE150"],
        ["GET_STUDENT_PAIRS"],
        ["REGISTER_FOR_COURSE", "st003", "CSE150"],
        ["REGISTER_FOR_COURSE", "st001", "CSE200"],
        ["REGISTER_FOR_COURSE", "st001", "CSE250"],
        ["REGISTER_FOR_COURSE", "st002", "CSE200"],
        ["GET_STUDENT_PAIRS"],
        ["REGISTER_FOR_COURSE", "st004", "CSE250"],
    ]
    
    print(solution(queries))

if __name__ == "__main__":
    main()