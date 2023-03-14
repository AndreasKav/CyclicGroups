from math import gcd


class GroupZn:
    n: int
    is_linear: bool

    def __init__(self, n, is_linear):
        self.n = n
        self.is_linear = is_linear
        print(f"\nG = (Z{n}{'' if is_linear else '*'}, {'+' if is_linear else '×'})")

    def subgroup_counter(self, element):
        n = self.n
        k = element
        is_linear = self.is_linear
        if is_linear:
            p = k
            numbers: list[int] = [0, k]
            while True:
                p = (k + p) % n

                if numbers.count(p) == 0:
                    numbers.append(p)
                elif len(numbers) == n:
                    return True, numbers
                else:
                    return False, numbers
        else:
            non_co_prime_list = non_coprimes(n)
            p = 1
            numbers = [1]
            if k in non_co_prime_list:
                return False, None
            while True:
                p = (k * p) % n
                if numbers.count(p) == 0:
                    numbers.append(p)
                elif len(numbers) == n - len(non_co_prime_list):
                    return True, numbers
                else:
                    return False, numbers

    def list_generators(self):
        group = self.n
        is_linear = self.is_linear
        is_cyclic = False
        print("\nAll generators:")
        if is_linear:
            for i in range(2, group):
                b, numbers = self.subgroup_counter(i)
                if b:
                    print(f"{i} - Cycle: {numbers}")
                    is_cyclic = True
            if not is_cyclic:
                print(f"The group (Z{group}*, +) has no other generators than 1.")
        else:
            for i in range(2, group):
                b, numbers = self.subgroup_counter(i)
                if b:
                    print(f"{i} - Cycle: {numbers}")
                    is_cyclic = True
            if not is_cyclic:
                print(f"The group (Z{group}*, ×) has no generators and is not cyclic.")

    def list_subgroups(self, do_print=True):
        unique = []
        group = self.n
        is_linear = self.is_linear
        if do_print:
            print("\nAll cyclic subgroups:")
        if is_linear:
            for i in range(2, group):
                b, numbers = self.subgroup_counter(i)
                if not b:
                    if do_print:
                        print(numbers)
                    else:
                        for k in range(len(unique)):
                            numbers = sorted(numbers)
                            if unique[k][1] == numbers[1]:
                                break
                        else:
                            unique.append(numbers)
        else:
            for i in range(2, group):
                b, numbers = self.subgroup_counter(i)
                if not b:
                    if numbers is not None:
                        if do_print:
                            print(numbers)
                        else:
                            for k in range(len(unique)):
                                numbers = sorted(numbers)
                                if unique[k][1] == numbers[1]:
                                    break
                            else:
                                unique.append(numbers)
        return unique

    def unique_subgroups(self):
        print("\nUnique cyclic subgroups:")
        unique = self.list_subgroups(do_print=False)
        for i in range(len(unique)):
            print(unique[i])

    def is_cyclic(self):
        group = self.n
        is_linear = self.is_linear
        if is_linear:
            for i in range(2, group):
                b, numbers = self.subgroup_counter(i)
                if b:
                    print(f"\nThe group (Z{group}, +) is cyclic. A generator is {i}.")
                    break
                elif i == group - 1:
                    print("\nThe group is not cyclic with a number greater than 1.")
                    break
        else:
            for i in range(2, group):
                b, numbers = self.subgroup_counter(i)
                if b:
                    print(f"\nThe group (Z{group}*, ×) is cyclic. A generator is {i}.")
                    break
            else:
                print(f"\nThe group (Z{group}*, ×) is not cyclic.")


def non_coprimes(n):
    non_coprimes_list = [n]
    for i in range(2, n):
        if gcd(n, i) > 1:
            non_coprimes_list.append(i)
    return non_coprimes_list


def integer_control(i):
    try:
        int(i)
    except TypeError:
        print("Error: Input an integer.")
        main()
        return
    else:
        integer = int(i)
        if integer <= 0:
            print("Error: Input an integer.")
            main()
        else:
            return integer


def bool_control(b):
    if b == 'y':
        return True
    elif b == 'n':
        return False
    else:
        print("Error: Input a 'y' or 'n' to the question.")
        main()


def main():
    while True:
        n = integer_control(input("\nValue of Zn?\n"))
        is_linear = bool_control(input("\nIs it Zn or Zn*? (y for Zn, n for Zn*)\n"))
        a = GroupZn(n, is_linear)
        a.is_cyclic()
        a.list_generators()
        a.unique_subgroups()


if __name__ == '__main__':
    main()
