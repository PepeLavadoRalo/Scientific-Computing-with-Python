# Budget App Project

## Overview

The Budget App allows users to track their expenses in different categories like "Food", "Clothing", and "Entertainment". It provides methods to deposit, withdraw, transfer funds between categories, and generate a spending chart.

## Features

- **Category Class**: Models budget categories with deposit, withdraw, transfer, and balance tracking.
- **Spend Chart**: Visualizes spending percentages by category.

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the files.
2. Run the `main.py` file.

```bash
git clone https://github.com/your-username/budget-app.git
cd budget-app
python main.py
```

### Example Usage
```python
food = Category('Food')
food.deposit(1000, 'Initial deposit')
food.withdraw(10.15, 'Groceries')
food.transfer(50, clothing)
print(food)
print(create_spend_chart([food, clothing]))
```

### Example Output
```python
*************Food*************
Initial deposit           1000.00
Groceries                  -10.15
Transfer to Clothing       -50.00
Total: 939.85

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  
     o  l  
     o  o  
     d  t  
     h  h  
     i  i  
     n  n  
     g     

```
### Methods
```python
Category Class:
deposit(amount, description=None): Adds a deposit.
withdraw(amount, description=None): Makes a withdrawal if funds are available.
get_balance(): Returns the current balance.
transfer(amount, category): Transfers funds between categories.
check_funds(amount): Checks if enough funds are available for withdrawal or transfer.
create_spend_chart(categories): Generates a bar chart showing the percentage spent in each category.
```
