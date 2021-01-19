# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(p, buyIndicator, sellIndicator):
    # prices is a list of prices.
    # buyIndicator is a list of arbitrary length, 1s and -1, indicating moves up and down.
    # sellIndicator is of the same format as buyIndicator.
    inc = 0
    dec = 0
    sellC = 0
    buyC = 0
    for i in range(len(p)-1):
        if inc <= 2 and dec <= 2:
            sum = p[i+1] - p[i]
            if sum > 0:
                inc += 1
            elif sum < 0:
                dec += 1
        if inc == 2:
            buy(p, i, buyC)
        if dec == 2:
            sell(p, i, sellC)
    return sell - buy


def sell(p, i, sellC):
    if (p[i] - p[i+1]) > 0:
        sellC += 1
    return sellC


def buy(p, i, buyC):
    buyC += 1
    return buyC


solution([51, 56, 56, 58, 60, 59, 54, 57, 52, 48], [1, 1, ], [-1-1, 1])


# SELECT department_name AS 'Department Name', 
# COUNT(*) AS 'No of Employees' 
# FROM departments 
# INNER JOIN employees 
# ON employees.dept_id = departments.dept_id 
# GROUP BY departments.dept_id, dept_name 
# ORDER BY dept_name;