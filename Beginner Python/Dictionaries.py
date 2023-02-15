
monthConversions = {
    0: "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    69: "October",
    "Nov": "November",
    "Dec": "December",
}
print(monthConversions["Mar"])
print(monthConversions.get("WIERD", "Not a valid key"))

