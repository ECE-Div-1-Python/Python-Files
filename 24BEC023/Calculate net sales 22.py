def calculatenetsales():
    grosssales = float(input("Enter the gross sales: "))
    discount = 0.10 * grosssales
    
    
    netsales = grosssales - discount
    
    print(f"Gross Sales: {grosssales:.2f}")
    print(f"Discount (10%): {discount:.2f}")
    print(f"Net Sales: {netsales:.2f}")


calculatenetsales()
