# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# Write a function that returns a new list of updated damages where the recorded data is converted to float values and the missing data is retained as "Damages not recorded":
def convert_damages_data(damages):
    """Convert damages data from string to float and return converted data as a list."""
    conversion = {"M": 1000000, "B": 1000000000}
    updated_damages = []
    for damage in damages:
        if damage == "Damages not recorded":
            updated_damages.append(damage)
        elif damage[-1] == "M":
            updated_damages.append(float(damage.strip("M"))*conversion["M"])
        elif damage[-1] == "B":
            updated_damages.append(float(damage.strip("B"))*conversion["B"])
    return updated_damages

updated_damages = convert_damages_data(damages)
#print(updated_damages)


#Create dictionary of hurricanes with hurricane name as the key and a dictionary of hurricane data as the value

def create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
 """Create dictionary of hurricanes with hurricane name as the key and a dictionary of hurricane data as the value."""
 hurricanes = {}
  
 for i in range(len(names)):
     hurricanes[names[i]] = {"Name": names[i],
                            "Month": months[i],
                            "Year": years[i],
                            "Max Sustained Wind": max_sustained_winds[i],
                            "Areas Affected": areas_affected[i],
                            "Damage": updated_damages[i],
                            "Death": deaths[i]}
 return hurricanes
hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#print(hurricanes)


# Write a function that converts the current dictionary of hurricanes to a new dictionary, where the keys are years and the values are lists containing a dictionary for each hurricane that occurred in that year.
def hurricane_by_year_dictionary(year):
 """Convert dictionary with hurricane name as key to a new dictionary with hurricane year as the key and return new dictionary."""
 hurricane_by_year = []
 for name in hurricanes:
    if hurricanes[name]['Year'] == year:
        hurricane_by_year.append(hurricanes[name])
 return hurricane_by_year
#print(hurricane_by_year_dictionary(1932))
#print(hurricane_by_year_dictionary(2018))



# a dictionary where the keys are the affected areas and the values are counts of how many times the areas were affected.
areas_affected = {}

def count_affected_areas(dict):
    for name in dict:
        for area in dict[name]['Areas Affected']:
            if area in areas_affected:
                areas_affected[area] += 1
            else:
                areas_affected[area] = 1
    return areas_affected
areas_affected = count_affected_areas(hurricanes)
#print(areas_affected)


#Write a function that finds the area affected by the most hurricanes, and how often it was hit.
def max_areas_affected(areas_affected):

    max_area = ''
    max_count = 0

    for area in areas_affected:
        if areas_affected[area] > max_count:
            max_area = area
            max_count = areas_affected[area]
    return max_area, max_count

max_area, max_count = max_areas_affected(areas_affected)
#print(max_area, max_count)


# The greatest number of deaths function here:
def greatest_num_deaths(dict):
    max_death = 0
    hurricane_name = ''
    for name in dict:
        if dict[name]['Death'] > max_death:
            max_death = dict[name]['Death']
            hurricane_name = name
    return hurricane_name, max_death
#print(greatest_num_deaths(hurricanes))



#Store the hurricanes in a new dictionary where the keys are mortality ratings and the values are lists containing a dictionary for each hurricane that falls into that mortality rating.
def categorize_by_mortality(dict):
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}
    hurricane_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for name in dict:
        if dict[name]['Death'] == mortality_scale[0]:
            hurricane_mortality[0].append(name)
        elif mortality_scale[0] < dict[name]['Death'] <= mortality_scale[1]:
            hurricane_mortality[1].append(name)
        elif mortality_scale[1] < dict[name]['Death'] <= mortality_scale[2]:
            hurricane_mortality[2].append(name)
        elif mortality_scale[2] < dict[name]['Death'] <= mortality_scale[3]:
            hurricane_mortality[3].append(name)
        elif mortality_scale[3] < dict[name]['Death'] <= mortality_scale[4]:
            hurricane_mortality[4].append(name)
        else:
            hurricane_mortality[5].append(name)
    return hurricane_mortality

#print(categorize_by_mortality(hurricanes))

#Write a function that finds the hurricane that caused the greatest damage, and how costly it was.
def greatest_damage_function(dict):
    damages_list = []
    for name in dict:
        if dict[name]['Damage'] != 'Damages not recorded':
            damages_list.append(dict[name]['Damage'])

    greatest_damage = max(damages_list)

    for name in dict:
        if dict[name]['Damage'] == greatest_damage:
            return name, greatest_damage


print(greatest_damage_function(hurricanes))

#Store the hurricanes in a new dictionary where the keys are damage ratings and the values are lists containing a dictionary for each hurricane that falls into that damage rating.
def categorise_by_damage(dict):
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}
    damage_scale_hurricane = {'No Damage': [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for name in dict:
        if dict[name]['Damage'] == 'Damages not recorded':
            damage_scale_hurricane['No Damage'].append(name)
        elif damage_scale[0] < dict[name]['Damage'] <= damage_scale[1]:
            damage_scale_hurricane[1].append(name)
        elif damage_scale[1] < dict[name]['Damage'] <= damage_scale[2]:
            damage_scale_hurricane[2].append(name)
        elif damage_scale[2] < dict[name]['Damage'] <= damage_scale[3]:
            damage_scale_hurricane[3].append(name)
        elif damage_scale[3] < dict[name]['Damage'] <= damage_scale[4]:
            damage_scale_hurricane[4].append(name)
        else:
            damage_scale_hurricane[5].append(name)
    return damage_scale_hurricane

#print(categorise_by_damage(hurricanes))




