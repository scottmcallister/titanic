import csv
import numpy as np

f = csv.reader(open('train.csv', 'rb'))
header = f.next()

data = []
for row in f:
    data.append(row)
data = np.array(data)

number_passengers = np.size(data[0::, 1].astype(np.float))
number_survived = np.sum(data[0::, 1].astype(np.float))
proportion_survivers = number_survived / number_passengers

men_only_stats = data[0::, 4] != "female"
women_only_stats = data[0::, 4] == "female"

women_onboard = data[women_only_stats, 1].astype(np.float)
men_onboard = data[men_only_stats, 1].astype(np.float)

proportion_men_survived = \
    np.sum(men_onboard) / np.size(men_only_stats)
proportion_women_survived = \
    np.sum(women_onboard) / np.size(women_only_stats)
print "proportion of men who survived: %s" % str(proportion_men_survived)
print "proportion of women who survived: %s" % str(proportion_women_survived)

fare_ceiling = 40

data[data[0::, 9].astype(np.float) >= fare_ceiling, 9] = fare_ceiling - 1.0

fare_bracket_size = 10
number_of_price_brackets = fare_ceiling / fare_bracket_size

number_of_classes = len(np.unique(data[::0, 2]))

survival_table = np.zeros((2, number_of_classes, number_of_price_brackets))
