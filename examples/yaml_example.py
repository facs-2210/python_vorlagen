# For questions: @author Sandro
# script to demonstrate yaml format

import yaml #pyyaml


####################################
######### yaml serializing #########
####################################


##############
### Inline ###
##############
data = { "1": 500, "2": 200}
## Output:
# '1': 500
# '2': 200

yaml_string = yaml.dump(data)



# Create a Python dictionary
data = [
        {
            "name": "Peter",
            "lastname": "Gryffin"
        },
        {
            "name": "Homer",
            "lastname": "Simpson"
        }
    ]

# Convert dictionary to yaml string

yaml_string = yaml.dump(data)
## Output: 
# - lastname: Gryffin
#   name: Peter
# - lastname: Simpson
#   name: Homer


yaml_string = yaml.dump(data, indent=4)
## Output: 
# -   lastname: Gryffin
#     name: Peter
# -   lastname: Simpson
#     name: Homer


print(yaml_string)
