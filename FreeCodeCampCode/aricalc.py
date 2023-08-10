# problems=["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]

# # function required
# def arithmetic_calculator(arithmetic_problems,display = False):
#     operators = ['+','-']
#     max_problems = 5
#     operand_max_size = 4 
    
#     # validating the length of the problems list 
#     if len(arithmetic_problems) > max_problems:
#         raise Exception('Error: Too many problems')
#     else:
#         pass
    
#     operand_one_list = []
#     operand_two_and_operator_list = []
    
#     # validating the operator 
#     for problem in arithmetic_problems:
#         problem_list = problem.split(' ')
#         print(problem_list)
        
#         operand_one_list.append(problem_list[0])
#         operand_two_and_operator_list.append(problem_list[1])
#         operand_two_and_operator_list.append(problem_list[2])
        
        
#         if problem_list[1] != '+' and problem_list[1] != '-':
#             raise Exception("Error: Operator must be '+' or '-'")
        
#         # validating the operand
#         if len(problem_list[0]) > operand_max_size or len(problem_list[2]) > operand_max_size:
#             raise Exception('Error: Numbers cannot be more than four digits.')
        
#         # changing operand into integer type / making it ready for calculations
#         operand_one = int(problem_list[0])
#         operand_two = int(problem_list[2])
#         operator = problem_list[1] 
        
#         if operator == '+':
#             sum = operand_one + operand_two
#             if display == True:
#                 print(f'{problem_list[0].rjust(5)}\n{operator}{problem_list[2].rjust(4)}\n-----\n{str(sum).rjust(5)}')
#             else:
#                 print(f'{problem_list[0].rjust(5)}\n{operator}{problem_list[2].rjust(4)}\n-----\n')
#         elif operator == '-':
#             diff = operand_one - operand_two
#             if display == True:
#                 print(f'{problem_list[0].rjust(5)}\n{operator}{problem_list[2].rjust(4)}\n-----\n{str(diff).rjust(5)}')
#             else:
#                 print(f'{problem_list[0].rjust(5)}\n{operator}{problem_list[2].rjust(4)}\n-----\n')

       
# arithmetic_calculator(problems, True)

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems"
    
    top_line = ""
    bottom_line = ""
    dash_line = ""
    answer_line = ""
    
    for problem in problems:
        operand1, operator, operand2 = problem.split()
        
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'"
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits"
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits"
        
        width = max(len(operand1), len(operand2)) + 2
        top_line += operand1.rjust(width) + "    "
        bottom_line += operator + operand2.rjust(width - 1) + "    "
        dash_line += '-' * width + "    "
        
        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2)).rjust(width)
            else:
                answer = str(int(operand1) - int(operand2)).rjust(width)
            answer_line += answer + "    "
    
    result = top_line.rstrip() + '\n' + bottom_line.rstrip() + '\n' + dash_line.rstrip()
    if show_answers:
        result += '\n' + answer_line.rstrip()
    
    return result

# Example usage
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems))

problems_with_answers = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
print(arithmetic_arranger(problems_with_answers, True))
