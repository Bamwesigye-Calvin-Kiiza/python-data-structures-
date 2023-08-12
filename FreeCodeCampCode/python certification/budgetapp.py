class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        output = self.category.center(30, '*') + '\n'
        for item in self.ledger:
            desc = item['description'][:23]
            amt = format(item['amount'], ".2f").rjust(30 - len(desc))
            output += f"{desc}{amt}\n"
        output += f"Total: {format(self.get_balance(), '.2f')}"
        return output

def create_spend_chart(categories):
    spendings = [sum(item['amount'] for item in category.ledger if item['amount'] < 0) for category in categories]
    total_spent = sum(spendings)
    percentages = [int(spending / total_spent * 100) for spending in spendings]
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "
        for percent in percentages:
            chart += 'o' if percent >= i else ' ' * 2
            chart += '  '
        chart += '\n'
    chart += "    " + '-' * (len(categories) * 3 + 1) + '\n'

    max_len = max(len(category.category) for category in categories)
    category_names = [category.category.ljust(max_len) for category in categories]

    for i in range(max_len):
        chart += "     "
        for name in category_names:
            chart += name[i] + '  '
        chart += '\n'

    return chart.rstrip()

# Example usage
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food")
clothing = Category("Clothing")
entertainment = Category("Entertainment")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(15, "entertainment")
food.transfer(50, clothing)

print(food)
print(create_spend_chart([food, clothing, entertainment]))
