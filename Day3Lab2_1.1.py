# apt_search1 below

def apt_search1(city, max_rent, min_beds, pets_allowed):

    if pets_allowed:
        pets_message = "that allow pets"
    else:
        pets_message = ""

    return f"Welcome to JP Property Management! Looking up listings in {city} for {min_beds} bedroom apartments {pets_message}, all within a budget of ${max_rent} per month."

# Example usage:
result1 = apt_search1("Tokyo", 2000, 2, True)
result2 = apt_search1("Kyoto", 1200, 1, False)

print(result1)
print(result2)

# apt_search2 below

def apt_search2(city, max_rent, min_beds=1, pets_allowed=True):

    if pets_allowed:
        pets_message = "that allow pets"
    else:
        pets_message = ""

    return f"Welcome to JP Property Management! Looking up listings in {city} for {min_beds} bedroom apartments {pets_message}, all within a budget of ${max_rent} per month."

# Call the function once with arguments for min_beds and pets_allowed both omitted
result1 = apt_search2("Osaka", 1800)

# Call it with just min_beds and no pets_allowed
result2 = apt_search2("Yokohama", 1600, min_beds=2)

# Call it with just pets_allowed and not min_beds using named arguments
result3 = apt_search2("Kobe", 2200, pets_allowed=False)

# Example usage
print(result1)
print(result2)
print(result3)


# Lambda Functions below

plus_one_hundred = lambda x: x + 100
print(plus_one_hundred(5)) # Output: 105

square_num = lambda x: x ** 2
print(square_num(4)) # Output: 16

concatenate = lambda s: "- " + s
print(concatenate("Hello")) # Output: - Hello