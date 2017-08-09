month_map = {
	1: 'feb',
	2: 'mrt',
	3: 'apr', 4: 'may', 5: 'jun', 6: 'jul', 7: 'aug', 8: 'sep', 9:'okt', 10: 'nov', 11: 'dec', 12: 'jan'
}
sundays = 0

year = 1900
month = 0
days = 0
def get_days_in_month(month_num, year):
	if month_num == 1:
		if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
			return 29
		else:
			return 28
	elif month_num in [3,5,8,10]:
		return 30
	else:
		return 31


while True:
	days += get_days_in_month(month, year)
	# print(month, year, days)
	if year >= 1901 and days % 7 == 6:
		sundays += 1
		print(year, month_map[month + 1])
	month += 1
	if month >= 12:
		month = 0
		year += 1
	if year == 2001:
		break
print(sundays) 
