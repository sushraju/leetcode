

'''
start_time = 0
end_time = 10

test case 1
d_starts = [2, 3, 5, 7]
d_ends = [6, 5, 10, 11]
d_pays = [5, 2, 4, 3]

test case 2
d_starts = [2, 3, 5, 2]
d_ends = [6, 5, 10, 4]
d_pays = [5, 2, 4, 6]

Calculcate maximum moolah
'''

def calc_max_pay(start_time, end_time, d_starts, d_ends, d_pays):
    curr_max_pay = 0
    max_pay = 0
    for i in range(0, len(d_starts)):
        curr_max_pay += d_pays[i]
        for k in range(0, len(d_starts)):
            if i != k:
                if d_starts[k] > d_starts[i] and d_starts[k] >= d_ends[i] and d_ends[k] <= end_time and d_starts[k] >= start_time:
                    curr_max_pay += d_pays[k]

        if curr_max_pay > max_pay:
            max_pay = curr_max_pay
        
        curr_max_pay = 0
            
    return max_pay

def main():
    start_time = 0
    end_time = 10   
    d_starts = [2, 3, 5, 7]
    d_ends = [6, 5, 10, 11]
    d_pays = [5, 2, 4, 3]
    print(calc_max_pay(start_time, end_time, d_starts, d_ends, d_pays))

    start_time = 0
    end_time = 11   
    d_starts = [2, 3, 5, 2]
    d_ends = [6, 5, 10, 4]
    d_pays = [5, 2, 4, 3]
    print(calc_max_pay(start_time, end_time, d_starts, d_ends, d_pays))


if __name__ == "__main__":
    main()
