def auto_info(company, model, color, gearbox, year, price=None):
    auto_0 = {
        'company':company,
        'model':model,
        'color':color,
        'gearbox':gearbox,
        'year':year,
        'price':price
        }
    return auto_0

auto1 = auto_info('GM', 'Corvette', 'red', 'Automatic', 2019)
auto2 = auto_info('Mercedec', 'G63', 'black', 'Automatic', 2020, 200000)
auto3 = auto_info('GM', 'Gentra 1.5', 'black', 'Mechanic',2020,12000)
autos = [auto1, auto2, auto3]
print("Available cars in market")
for auto in autos:
    if auto['price']:
        price = auto['price']
    else:
        price = 'Noma\'lum'
    print(f"{auto['color']} {auto['model']}. Price: {auto['price']}$ ")