# For questions: @author Noah Denger
# script to create fake users using the python faker module

from faker import Faker

faker = Faker()


# generate 10 user_profiles by gender and country
def generate_profiles(country, gender):
    profiles = []
    for _ in range(10):
        name_func = faker.name_male if gender == "male" else faker.name_female

        fake_profile = {
            "name": name_func(),
            "sex": gender,
            "country": country,
            "address": faker.address(),
            "phone": faker.phone_number(),
            "email": faker.email(),
            "birthday": faker.date_of_birth(minimum_age=18, maximum_age=90).strftime(
                "%Y-%m-%d"
            ),
        }
        profiles.append(fake_profile)
    return profiles


# return dict with males and females
def populate_profiles():
    males = []
    females = []
    countries = ["Switzerland", "Germany"]
    for country in countries:
        male = generate_profiles(country, "male")
        female = generate_profiles(country, "female")
        males.extend(male)
        females.extend(female)
    return {"males": males, "females": females}


profiles = populate_profiles()
genders = ["males", "females"]

# print first male and first female
print(profiles["males"][0])
print(profiles["females"][1])