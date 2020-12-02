from covid import Covid
from matplotlib import pyplot as plt

country = input("Enter Your Country Name: ")

covid = Covid()
data = covid.get_status_by_country_name(country)

cadr = {
    key: data[key]
    for key in data.keys() & {"confirmed",'active','deaths','recovered'}
    }
n = list(cadr.keys())
v = list(cadr.values())
print(cadr)

plt.title(country)
plt.barh(range(len(cadr)),v,tick_label=n, color=['black', 'red', 'green', 'blue'],label=cadr)
plt.legend()
plt.show()
