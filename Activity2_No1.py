from datetime import date

father_name = input("Enter your father's name: ")
birthplace = input("Enter your father's birthplace: ")
birthday = input("Enter your father's birthday (YYYY-MM-DD): ")

try:
    birthday_date = date.fromisoformat(birthday)
    today = date.today()
    age = today.year - birthday_date.year - ((today.month, today.day) < (birthday_date.month, birthday_date.day))
    
    print("\nFather's Information:")
    print("Name: " + father_name)
    print("Birthplace: " + birthplace)
    print("Birthday: " , birthday_date.strftime("%B %d, %Y"))
    print("Age: " , age , "years")
    
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD format for the birthday.")