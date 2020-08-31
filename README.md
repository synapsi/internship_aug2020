# Hi there!

## Thank you for participating in our recruitment process!

Here's what you need to do to complete this challenge:

* **Copy** this repo (do not fork it! otherwise, other competitors will see your solution!) to your github account.
* Solve the task that's below using your preffered language - Python or JS or both of them.
    * Using language-specific features would be a plus.
* Commit and push your solution into your repo.
* Send the repo address in response to the mail you got from us.
* That's it!

## Task #1

Create class "Product" that inherits from data.ParentProduct class.

* Class should have a parameterized constructor that takes the following args: name, amount, price.
* The class should have three methods:
    * `show_price` - takes one string argument "currency" and print string in format: '<product_name> price is <product_price><currency>'
    * `show_amount` method that print in format '<product_name> amount is <product_amount>'
    * `calculate_total_value` return total value of product (amount * price)

Basing on MIN and MAX values from `data.products` dictionary generate prices and stock levels (amount).

Using previously updated `data.products` records (amount and price) create `Product` class instances and push them into `data.obj_list`.

Create a list of summary values for each product (amount times price).

Save summary value, `data.products` and `data.obj_list` to results_01.txt file in a _comprehensive_ format.

## Task #2

Prompt user to input a number in a specified range and store it in `input_value`.

The minimum should be in the range 0-150, and maximum in 75-200 (be sure that min < max).

Input prompt should be in format: `Input number in range <min_value> - <max_value>: `

User should be forced to type in a number until it fulfills all the necessary conditions.

Inform the user if something goes wrong.

### Good luck to all of you!
