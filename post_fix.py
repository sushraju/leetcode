#!/usr/bin/env python

def solve_post(values):
    op_list = []
    ans = 0
    for value in values:
        if value == '+' or value == '*' or value == '-' or value == '/':

            # pop two operands and calculate.
            op_1 = int(op_list.pop())
            op_2 = int(op_list.pop())
            # print(op_2, op_1, value)
            if value == '+':
                ans = op_2 + op_1
            elif value == '*':
                ans = op_2 * op_1
            elif value == '-':
                ans = op_2 * op_1
            else:
                ans = op_2 // op_1

            # push the interim value back to the operands list.
            op_list.append(ans)
        else:

            # push the operands to the list until you encounter an operator.
            op_list.append(value)

    return ans


def main():

    # Driver code.
    assert (solve_post(['2', '3', '+', '3', '*']) == 15)
    assert (solve_post(['13', '-1', '2', '/', '5', '+', '+']) == 17)
    assert (solve_post(['1', '2', '+', '3', '*', '6', '+', '2', '3', '+', '/']) == 3)


if __name__ == "__main__":
    main()
