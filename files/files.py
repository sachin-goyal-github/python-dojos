countries_file = open("countries.txt", "r")
my_country_file = open("my_country.txt", "w")

for country in countries_file:
    country = country.strip()
    if country == "India":
        my_country_file.write(country + '\n')

countries_file.close()
my_country_file.close()
