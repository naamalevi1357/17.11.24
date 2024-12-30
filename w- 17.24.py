# start

# 1:

country_Israel = {"name ": "Israel ", "birth " : 1948 , "population_millions ": 9.3 , "capital": "Jerusalem ", "language": "Hebrew ",
                  "cities" : ["Jerusalem ", "Tel Aviv " , "Haifa", "RishonLeZion ", "PetahTikva", "Ashdod"] ,
                  "currency": "ILS ", "area_Kilometer": 22145 , "gdp_billion": 450}
# a:
print(country_Israel.get("capital"))

# b:
print(country_Israel.keys())

# c:
print(country_Israel.values())

# d:
for key,values in country_Israel.items():
    print(key,values)

# e:

print(country_Israel.copy())

# f:

print(country_Israel.pop("gdp_billion"))
print(country_Israel)

# g:
print(country_Israel.fromkeys(country_Israel.keys(),""))

xd=country_Israel.fromkeys(country_Israel.keys())

name_cantry:str=str(input( "what is name cantry?"))
xd["name "] = name_cantry
print(xd)
birth:int=int(input(" what is birth? "))
xd["birth "]=birth
population_millions:int= int(input(" what ispopulation_millions "))
xd["population_millions"]=population_millions
capital:str=str(input("what is capital? "))
xd["capital"]=capital
language:str=str(input("what is language? "))
xd["language"]=language
list_cities=[]
citie1:str=str(input("what is citie1? "))
citie2:str=str(input("what is citie2? "))
citie3:str=str(input("what is citie3? "))
ty=list_cities.append(citie1)
tr=list_cities.append(citie2)
tl=list_cities.append(citie3)
# print(list_cities)
xd["cities"]=list_cities
currency:str=str(input("what is currency? "))
xd["currency"]=currency
area_Kilometer:int=int(input(" what is area_Kilometer? "))
xd["area_Kilometer"]=area_Kilometer
gdp_billion:int=int(input(" what is gdp_billion? "))
xd["gdp_billion"]=gdp_billion
print(xd)


# 2:

def len_1(word:str):
    return len(word.split()[-1])

print(len_1('Hello World'))
print(len_1('fly me   to   the moon'))
print(len_1('luffy is still joyboy'))