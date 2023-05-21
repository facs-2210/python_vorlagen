# Imports
import matplotlib.pyplot as plt
import json
from datetime import datetime

# Prepare Dictionary to fill with data from JSON file 
item_count = {
    "Jan":0,
    "Feb":0,
    "Mar":0,
    "Apr":0,
    "Mai":0,
    "Jun":0,
    "Jul":0,
    "Aug":0,
    "Sep":0,
    "Oct":0,
    "Nov":0,
    "Dez":0
}

# Read File, encoding is neccesary e.g. for uncommon languages
with open("./sources/nvdcve-1.1-2023.json", 'r', encoding="utf-8") as json_file:
    data = json.load(json_file)
    for da in data['CVE_Items']:
        # Example publishedDate: "2023-02-08T18:15Z" -> Date = [5:10] // Month = [5:7] // Day = [8:10]
        # Add the entry to the specific month
        match (da['publishedDate'][5:7]):
            case("01"):
                item_count["Jan"] += 1
            case("02"):
                item_count["Feb"] += 1
            case("03"):
                item_count["Mar"] += 1
            case("04"):
                item_count["Apr"] += 1
            case("05"):
                item_count["Mai"] += 1
            case("06"):
                item_count["Jun"] += 1
            case("07"):
                item_count["Jul"] += 1
            case("08"):
                item_count["Aug"] += 1
            case("09"):
                item_count["Sep"] += 1
            case("10"):
                item_count["Okt"] += 1
            case("11"):
                item_count["Nov"] += 1
            case("12"):
                item_count["Dez"] += 1

# Set Graph options
## Axis
x = list(item_count.keys())
y = list(item_count.values())

## Put some descriptions on it
plt.scatter(x,y)
plt.xlabel('Month ->')
plt.ylabel('Cases ->')
plt.title('CVEs in Year 2023')

## Save to png (e.g for a report)
## Add current Datetime for uniquer name
savepath =  "./results/" + datetime.now().strftime("%d.%m.%Y_%H%M%S") + ".png"
## Specific save settings
plt.savefig(savepath, dpi=600)

# Show the Graph
plt.show()
