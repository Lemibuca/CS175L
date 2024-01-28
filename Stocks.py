
#inputs
commission_rate_purchased = float(input('Enter commission rate percentage (ex 0.03)on stock purchase: '))
commission_rate_sold =float(input('Enter commission rate percentage (ex 0.03) on stock sale: '))
num_shares_purchased =int(input('Enter number of shares purchased: '))
num_shares_sold =int(input('Enter number of shares sold: '))
purchased_price =int(input('Enter purchase price per share: '))
selling_price = float(input('Enter sell price per share: '))
input()

#process


amount_paid_for_stock = purchased_price * num_shares_purchased
commission_paid_purchased = commission_rate_purchased * amount_paid_for_stock
total_purchased = amount_paid_for_stock + commission_paid_purchased
amount_stock_sold = selling_price * num_shares_sold
commission_paid_sold = commission_rate_sold * amount_stock_sold
total_sold = amount_stock_sold - commission_paid_sold
profit = total_sold - total_purchased
              
# outputs

print(f'Amount paid for the stock: ${amount_paid_for_stock:,.2f}')
print(f'Commission paid on the purchase: ${commission_paid_purchased:,.2f}')
print(f'Amount the stock sold for: ${amount_stock_sold:,.2f}')
print(f'commission paid on the sale: ${commission_paid_sold:,.2f}')
print(f'Profit (or loss if negative): ${profit:,.2f}')
