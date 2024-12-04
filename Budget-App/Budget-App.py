class Category:
    """
    A class representing a category of a budget, with methods to handle deposits, 
    withdrawals, transfers, and balance checking.
    """
  
    def __init__(self, name):
        """
        Initializes a new Category object.
        
        Parameters:
        - name (str): The name of the category (e.g., 'Food', 'Entertainment').
        """
        self.name = name  # Name of the category
        self.ledger = []  # List to hold transaction details (amount and description)

    def deposit(self, amount, description=None):
        """
        Deposits a certain amount into the category's ledger.
        
        Parameters:
        - amount (float): The amount to deposit.
        - description (str): Optional; description of the deposit.
        """
        if description is None:
            self.ledger.append({'amount': amount, 'description': ''})
        else:
            self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=None):
        """
        Withdraws a certain amount from the category's ledger, if sufficient funds exist.
        
        Parameters:
        - amount (float): The amount to withdraw.
        - description (str): Optional; description of the withdrawal.
        
        Returns:
        - bool: True if the withdrawal was successful, False if insufficient funds.
        """
        if self.check_funds(amount):  # Check if there are enough funds
            if description is None:
                self.ledger.append({'amount': -amount, 'description': ''})
            else:
                self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False
    
    def get_balance(self):
        """
        Returns the current balance of the category.
        
        Returns:
        - float: The balance of the category (sum of all deposits and withdrawals).
        """
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance
  
    def transfer(self, amount, budget_category):
        """
        Transfers an amount to another category if funds are sufficient.
        
        Parameters:
        - amount (float): The amount to transfer.
        - budget_category (Category): The category to transfer the amount to.
        
        Returns:
        - bool: True if the transfer was successful, False if insufficient funds.
        """
        if self.check_funds(amount):  # Check if enough funds exist
            self.ledger.append({'amount': -amount, 'description': f'Transfer to {budget_category.name}'})
            budget_category.deposit(amount, description=f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        """
        Checks if there are enough funds for a withdrawal or transfer.
        
        Parameters:
        - amount (float): The amount to check.
        
        Returns:
        - bool: True if there are sufficient funds, False otherwise.
        """
        return amount <= self.get_balance()

    def __str__(self):
        """
        Returns a string representation of the category, showing the name, 
        all transactions (deposits and withdrawals), and the total balance.
        
        Returns:
        - str: The formatted string representing the category's ledger.
        """
        name = self.name
        s = name.center(30, "*")  # Center the category name and add '*' padding
        for item in self.ledger:
            try:
                left = item['description'][0:23]  # Limit description to 23 characters
            except TypeError:
                left = ''
            right = str("{:.2f}".format(item['amount']))  # Format the amount to two decimal places
            s += f"\n{left:<23}{right:>7}"
        s += "\nTotal: " + str(self.get_balance())  # Append the total balance at the end
        return s


def create_spend_chart(categories):
    """
    Creates a chart showing the percentage of spending in each category.
    
    Parameters:
    - categories (list): A list of Category objects to create the chart for.
    
    Returns:
    - str: The chart as a string.
    """
    spent_dict = {}  # Dictionary to store the total spending for each category
    
    # Calculate the total spending for each category
    for category in categories:
        total_spent = 0
        for transaction in category.ledger:
            if transaction['amount'] < 0:  # Only count withdrawals (negative amounts)
                total_spent += abs(transaction['amount'])
        spent_dict[category.name] = round(total_spent, 2)
    
    total = sum(spent_dict.values())  # Calculate the total amount spent in all categories
    percent_dict = {}  # Dictionary to store the percentage spent in each category
    
    # Calculate the percentage spent in each category
    for category in spent_dict:
        percent_dict[category] = int(round(spent_dict[category] / total, 2) * 100)
    
    output = 'Percentage spent by category\n'
    
    # Build the chart, starting with the percentages for each level (from 100% to 0%)
    for i in range(100, -10, -10):
        output += f'{i}'.rjust(3) + '| '  # Print the percentage on the left
        for percent in percent_dict.values():
            if percent >= i:
                output += 'o  '  # Place 'o' for categories that spent more than or equal to this percentage
            else:
                output += '   '  # Empty space for categories that spent less
        output += '\n'
    
    # Print the bottom separator line
    output += ' ' * 4 + '-' * (len(percent_dict.values()) * 3 + 1) + '\n     '
    
    # Print the names of the categories below the chart
    category_names = list(percent_dict.keys())
    max_len_category = max([len(name) for name in category_names])  # Find the longest category name
    
    for i in range(max_len_category):
        for name in category_names:
            if len(name) > i:
                output += name[i] + '  '  # Print each letter in the category name
            else:
                output += '   '  # If the category name is shorter than the current index, print empty space
        if i < max_len_category - 1:
            output += '\n     '
    
    return output
