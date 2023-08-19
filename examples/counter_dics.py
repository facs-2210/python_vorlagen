from collections import Counter, OrderedDict


forensics_map = Counter()
ipAddresses = ["1", "2", "3", "1", "2", "3", "1", "2", "3"]

# count ip addresses
forensics_map.update(ipAddresses)

result = OrderedDict(forensics_map.most_common())