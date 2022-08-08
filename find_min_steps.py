import time

""" 
due to fact that the text says implement A METHOD, I have created a class with an appropriate method that calculates
the necessary number of steps. The method works with arguments being passed directly, or with arguments provided
upon object initialization. I have also left this as a function at the end of the file. Sleeps and printouts are
left on purpose for easier logic tracking
"""


class Compare:

    def __init__(self, num1=0, num2=0):
        """
        Initialize all necessary variables of the object. The class can be invoked with no parameters in which case
        the num1 and num2 parameters are defaulted to 0. Object instantiation fails if non int parameters provided

        :param num1: int,the first number of the comparison pair.
        :param num2: int, the second number of the comparison pair
        """

        if isinstance(num1, int) and isinstance(num2, int):
            self.num1 = num1
            self.num2 = num2
            self.base_2_multiple = list(map(lambda x: 2**(x+1), range(50)))
            self.min_num_of_steps = 0
        else:
            raise Exception("Object can only take int values for comparison")

    def __str__(self):
        """
        Dunder method, enables print for the generated class
        :return:
        """
        if self.num1 == 0:
            return "Can't print a step count value for an object without provided number arguments"
        else:
            return f"Min number of steps to have ({self.num1},{self.num2}) at 0 is: {self.min_num_of_steps}"

    def subtract(self, a, b, min_num_of_steps):
        """
        Loops and subtracts -1 from both numbers until 0 is reached
        :param a: int, the first number of the comparison pair
        :param b: int, the second number of the comparison pair
        :param min_num_of_steps: int, counter of previous steps
        :return: final a,b states as well as final step count to reach 0
        """
        while b > 0:
            a -= 1
            b -= 1
            min_num_of_steps += 1
            print(f"{min_num_of_steps}. ({a},{b})")
            time.sleep(0.01)
        return a, b, min_num_of_steps

    def equal_vals(self, a, b, min_num_of_steps):
        """
        Loops and multiplies the lesser number by 2 until both number have equal value
        :param a: int, the first number of the comparsion pair
        :param b: int, the second number of the comparsion pair
        :param min_num_of_steps: int, counter of previous steps
        :return: a,b states as well as current step count
        """
        while a != b:
            a *= 2
            min_num_of_steps += 1
            print(f"{min_num_of_steps}. ({a},{b})")
            time.sleep(0.01)
        return a, b, min_num_of_steps

    def find_min_steps(self, a=0, b=0):
        """
        Method controlling the logic flow of calculation. If no arguments provided, method uses the numbers provided
        by object instantiation if exist. If no such exist, method call fails
        :param a: int, default to 0, input must be positive integer
        :param b: int, default to 0, input must be positive integer
        :return: int, minimum number of steps needed to have both numbers at 0 at the same time
        """
        self.min_num_of_steps = 0
        if self.num1 != 0 and self.num2 != 0:
            a = self.num1
            b = self.num2
        if a < 1 or b < 1:
            raise Exception("Provided numbers must be positive integers")
        elif isinstance(a, int) and isinstance(b, int):
            status = 1
            greater = max(a, b)
            lesser = min(a, b)
            base_nearest = list(filter(lambda numb: greater-numb >= 0, self.base_2_multiple))[-1]
            while status:
                time.sleep(0.01)
                if lesser == greater:
                    lesser, greater, self.min_num_of_steps = self.subtract(lesser, greater, self.min_num_of_steps)
                    status = 0
                elif lesser in self.base_2_multiple and greater in self.base_2_multiple:
                    while lesser != greater:
                        lesser, greater, self.min_num_of_steps = self.equal_vals(lesser, greater, self.min_num_of_steps)
                    lesser, greater, self.min_num_of_steps = self.subtract(lesser, greater, self.min_num_of_steps)
                    status = 0
                elif lesser == 1 and greater > 1:
                    lesser *= 2
                    self.min_num_of_steps += 1
                    print(f"{self.min_num_of_steps}. ({lesser},{greater})")
                elif lesser in self.base_2_multiple and greater not in self.base_2_multiple and 2 * lesser <= greater - base_nearest:
                    lesser *= 2
                    self.min_num_of_steps += 1
                    print(f"{self.min_num_of_steps}. ({lesser},{greater})")
                else:
                    lesser -= 1
                    greater -= 1
                    self.min_num_of_steps += 1
                    print(f"{self.min_num_of_steps}. ({lesser},{greater})")
            print(f"Number of steps needed: {self.min_num_of_steps}")
            return self.min_num_of_steps
        else:
            raise Exception("Provided numbers must be positive integers")


object1 = Compare()
object1.find_min_steps(14, 54)
print(object1)
object2 = Compare(14, 54)
object2.find_min_steps()
print(object2)


# base_2_multiple = []
# for x in range(50):
#     base_2_multiple.append(2**(x+1))
#
#
# def subtract(a, b, min_num_of_steps):
#     while b > 0:
#         a -= 1
#         b -= 1
#         min_num_of_steps += 1
#         print(f"{min_num_of_steps}. ({a},{b})")
#         time.sleep(0.01)
#     return a, b, min_num_of_steps
#
#
# def equal_vals(a, b, min_num_of_steps):
#     while a != b:
#         a *= 2
#         min_num_of_steps += 1
#         print(f"{min_num_of_steps}. ({a},{b})")
#         time.sleep(0.01)
#     return a, b, min_num_of_steps
#
#
# def find_min_steps(a, b):
#     min_num_of_steps = 0
#     status = 1
#     greater = max(a, b)
#     lesser = min(a, b)
#     base_nearest = list(filter(lambda numb: greater-numb >= 0, base_2_multiple))[-1]
#     while status:
#         time.sleep(0.01)
#         if lesser == greater:
#             lesser, greater, min_num_of_steps = subtract(lesser, greater, min_num_of_steps)
#             status = 0
#         elif lesser in base_2_multiple and greater in base_2_multiple:
#             while lesser != greater:
#                 lesser, greater, min_num_of_steps = equal_vals(lesser, greater, min_num_of_steps)
#             lesser, greater, min_num_of_steps = subtract(lesser, greater, min_num_of_steps)
#             status = 0
#         elif lesser == 1 and greater > 1:
#             lesser *= 2
#             min_num_of_steps += 1
#             print(f"{min_num_of_steps}. ({lesser},{greater})")
#         elif lesser in base_2_multiple and greater not in base_2_multiple and 2 * lesser <= greater - base_nearest:
#             lesser *= 2
#             min_num_of_steps += 1
#             print(f"{min_num_of_steps}. ({lesser},{greater})")
#         else:
#             lesser -= 1
#             greater -= 1
#             min_num_of_steps += 1
#             print(f"{min_num_of_steps}. ({lesser},{greater})")


# find_min_steps(64, 827)



