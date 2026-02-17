import math


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': -amount, 'description': description})
        return True

    def transfer(self, amount, destination):
        if self.withdraw(amount, f'Transfer to {destination.name}'):
            destination.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction['amount']
        return balance

    def check_funds(self, amount):
        if amount>self.get_balance():
            return False
        return True

    def __str__(self):
        ctg_str = ''
        side = int((30-len(self.name))/2)
        title = '*' * side + self.name + '*' * side + math.ceil((30-len(self.name)) % 2) * '*' + '\n'
        ctg_str += title

        for entry in self.ledger:
            entry_line = f"{entry['description'][:23]:23}{entry['amount']:7.2f}\n"
            ctg_str += entry_line
            #print(len(entry_line))

        ctg_str += f'Total: {self.get_balance()}'
        return ctg_str

def create_spend_chart(categories):
    spc = ' '
    end = '\n'
    total_spent = 0
    categories_spents = []
    max_name_length = 0
    for category in categories:
        category_spent = 0
        if len(category.name)>max_name_length:
            max_name_length = len(category.name)
        for entry in category.ledger:
            if entry['amount']<0 and 'Transfer' not in entry['description']:
                total_spent += -entry['amount']
                category_spent += -entry['amount']
        categories_spents.append(category_spent)
        #
    categories_pcs = []
    for cs in categories_spents:
        categories_pcs.append(math.floor(cs*100/total_spent)//10*10)
    # print(f'{categories_spents=}')
    # print(f'{categories_pcs=}')
    # print(f'{total_spent=}')
    # print(f'{max_name_length=}')
    chart = 'Percentage spent by category\n'
    for i in range(100,-10,-10):
        line = f'{i:3}|' + spc
        for pc in categories_pcs:
            if pc >= i:
                line += 'o' + spc * 2
            else:
                line += spc * 3
        chart += line + end
    chart += spc * 4 + '-' + '---' * len(categories_pcs) + end
    for i in range(max_name_length):
        line = spc * 5
        for category in categories:
            if len(category.name)>i:
                line += category.name[i] + spc * 2
            else:
                line += spc * 3
        chart += line + end
    return chart[:-1]
    
def main():
    food = Category('Food')
    food.deposit(1000, 'deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    clothing.withdraw(5, 'shoes')
    auto = Category('Auto')
    auto.deposit(100, 'initial deposit')
    auto.withdraw(10, 'tyre repair')
    
    print(food)
    print(clothing)
    print(auto)
    print(create_spend_chart((food, clothing, auto)))

if __name__ == '__main__':
    main()
