# The main question is To do 20 round and calculate monkey buisness

# Importing regex, to get digits from string
import re


# Classes

class Monkey:
    def __init__(self, name, items, operationValue, operationSign, test, true, false):
        self.number = name
        self.items = items
        self.operation_value = operationValue
        self.operation_sign = operationSign
        self.test = test
        self.trueTest = true
        self.falseTest = false
        self.inspected_items = 0

    def out(self):
        for i in self.items:
            print(i, end=" ")
        print("\n")


class System:

    def __init__(self):
        self.listof_monkey = []

    def creating_monkey(self, lines):
        # So i go through iterating every line
        for line in lines:
            # So 5 out of 6 lines contains only 1 number to get out of it, so to simplify the code I create a variable so it will readable
            valueof_line = re.findall('[0-9]+', line)
            # We need to check whether line contained digit
            if len(valueof_line) != 0:
                valueof_line = int(valueof_line[0])
            else:
                valueof_line = 0

            if "Monkey" in line:
                # Getting number of monkey from line
                numberof_monkey = valueof_line

            elif "items" in line:
                # Getting items of the monkey
                itemsof_monkey = re.findall('[0-9]+', line)
                # Now need to convert list of strings to list of ints
                itemsof_monkey = [int(i) for i in itemsof_monkey]

            elif "Operation" in line:
                # Getting operation value from the monkey
                # So it is possible that the value of operation will be old*old need to be prepared
                valuof_oper_monkey = re.findall('[0-9]+', line)
                if len(valuof_oper_monkey) == 0:
                    valuof_oper_monkey = "old"
                else:
                    valuof_oper_monkey = int(valuof_oper_monkey[0])

                # Getting Signof the operation
                signof_oper_monkey = ''
                if '*' in line:
                    signof_oper_monkey = '*'
                elif '+' in line:
                    signof_oper_monkey = '+'
                # Not for this assigment but for clarity of the code i will add other cases that dont exist in this input !
                elif '-' in line:
                    signof_oper_monkey = '-'
                elif '/' in line:
                    signof_oper_monkey = '/'

            elif "Test" in line:
                valueof_test_monkey = valueof_line

            elif "true" in line:
                valueof_true_monkey = valueof_line

            elif "false" in line:
                valueof_false_monkey = valueof_line

            # It is what it is I know its not gonna happen !!!!
        monkey = Monkey(numberof_monkey, itemsof_monkey, valuof_oper_monkey, signof_oper_monkey, valueof_test_monkey,
                        valueof_true_monkey, valueof_false_monkey)

        self.listof_monkey.append(monkey)

    def getting_data(self, lines):
        # So I iterate throught of all of the input
        i = 0
        while i < len(lines):
            # When i recognize word monkey in the line i will create a monkey(class) so i need to gather lines which concern this particural
            # monkey i achieve this by this while loop
            if "Monkey" in lines[i]:
                to_pass_lines = []
                while i < len(lines) and lines[i] != '\n':
                    to_pass_lines.append(lines[i])
                    i += 1
                # There is the process of creating monkey
                self.creating_monkey(to_pass_lines)
            i += 1

    def throwingItems_byMonkey(self, item, monkeyToName):
        # So we need to get info where to throw this item
        monkeyTo = list(filter(lambda x: x.number == monkeyToName, self.listof_monkey))[0]
        # monkeyTo=[mon for mon in self.listof_monkey if mon.number == monkeyToName][0]
        i_monkeyTo = self.listof_monkey.index(monkeyTo)
        # Next we put the item in the items of the monkey
        self.listof_monkey[i_monkeyTo].items.append(item)

    def inspectingItem_byMonkey(self, i_monkey, item):

        monkey = self.listof_monkey[i_monkey]
        # We start by Operation

        if monkey.operation_value == "old":
            match monkey.operation_sign:
                case '*':
                    item *= item
                case '+':
                    item += item

        else:
            match monkey.operation_sign:
                case '*':
                    item *= monkey.operation_value
                case '+':
                    item += monkey.operation_value

        # So we go to the test, wchich relies on divisible
        # Random dividing by 3 becouse it said so
        # So yea for the second part of the puzzle there is no more /3 so goodbye
        item = int(item / 3)

        # Then we go on with the program

        if item % monkey.test != 0:
            self.throwingItems_byMonkey(item, monkey.falseTest)
        else:
            self.throwingItems_byMonkey(item, monkey.trueTest)
        print("END")

    def playRound(self):
        # Round is when a all of the monkey inspects all of their items !

        # The turn of the monkey ends when there is no items on it

        # So i run to a problem when inside a loop i was itering i would change
        # change the list(remove item) that the loop was depended on so it would skip
        # the next item as the indexes inside the logic behind for loop would get
        # messed up, so i came up with this solution, more info in documention
        # for for loops(exactly the note!)
        for monkey in self.listof_monkey:
            i_monkey = self.listof_monkey.index(monkey)
            # so it is here where the round of the monkey starts
            for item in self.listof_monkey[i_monkey].items:
                self.inspectingItem_byMonkey(i_monkey, item)
                self.listof_monkey[i_monkey].inspected_items += 1
            # this is where the round of the monkey ends so we clear up her items
            # becouse it threw items to other monkeys(not to herself by program!)
            self.listof_monkey[i_monkey].items.clear()

    def findingActiveMonkeys(self):
        monkey1 = max(self.listof_monkey, key=lambda x: x.inspected_items)
        # we need the remove the most active monkey to search for the second
        max1 = monkey1.inspected_items
        self.listof_monkey.remove(monkey1)
        max2 = max(self.listof_monkey, key=lambda x: x.inspected_items).inspected_items

        return max1 * max2

    def puzzle1_main(self):
        # For the puzzle There is 20 rounds

        # for round in range(20):
        #   self.playRound()

        # For the second part there is 10 000 round so :

        for round in range(20):
            print("Round",round)
            self.playRound()
        # So after playing these rounds there is only one step more to answer
        # I need to find 2 the most active monkeys(most inspected items) and
        # mutliply their isnpected items by each other
        result = self.findingActiveMonkeys()

        return result


with open("Zadanie11_Input.txt") as f:
    lines = f.readlines()

system = System()
system.getting_data(lines)

print("I part:",system.puzzle1_main())   # The anwser is 95472

# print("II part:", system.puzzle1_main())