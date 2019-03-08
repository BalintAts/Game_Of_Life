#from main import table

def menu():
	user_choose = 0
	print("Hi mortal! What do you want?")
	print("1: Random looking preset")
	print("2: Glider")
	print("3: Stable configurations")
	print("4: Glider gun")
	print("5: Open init state from file")
	print("Imput the number of the option you want to choose.")
	user_choose = input('')
	return user_choose


def display(content):
    for row in content:
        print(row)
																				