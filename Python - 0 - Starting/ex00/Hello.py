ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

world = "World"
country = "France"
city = "Angoulême"
school = "42" + city

#####################
ft_list[1] = world
#####################
tmp_list = list(ft_tuple)
tmp_list[1] = country
ft_tuple = tuple(tmp_list)
#####################
set_content = [ "Hello", city]
ft_set = set(set_content)
#####################
ft_dict.update({ "Hello" : school})
#####################

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)