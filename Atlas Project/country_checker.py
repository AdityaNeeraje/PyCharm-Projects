import json

with open("country_data.json", "r") as file:
    country_data = json.load(file)

with open("alternative_names.json") as file:
    alternative_names = json.load(file)

class CountryChecker():
    def __init__(self, player_num, chance):
        if chance == 1:
            self.country = input("Enter the First Country Name: ").strip().lower()
        else:
            self.country = input("Enter the Second Country Name: ").strip().lower()
        self.player_num = player_num

    def check_country(self, num_incorrect, starting_letter):
        while not self.country or self.country[0] not in starting_letter or self.country not in [country.lower() for
                                                                                              country in country_data[
                                                                                                  self.country[0]]]:
            if self.country:
                num_incorrect += 1
                if num_incorrect == 5:
                    print(f"You have made 5 incorrect submissions this round. {3-self.player_num} wins the game.")
                    break
                self.country = input("Incorrect submission. Please try again: ").strip().lower()
            else:
                self.country = input("Please type a valid country name: ").strip().lower()
        if num_incorrect == 5:
            return True
        for country in country_data[self.country[0]]:
            if country.lower() == self.country:
                if alternative_names.get(country) is not None:
                    for nation in alternative_names[country]:
                        country_data[nation[0].lower()].remove(nation)
                else:
                    country_data[self.country[0]].remove(country)
                break
        return False