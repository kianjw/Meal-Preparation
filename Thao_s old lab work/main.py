#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 14:22:10 2023

@author: pchu
"""
import pandas as pd
import numpy as np
import math
import Person
import ListMeal
import nutrition
import enviImpact
import calendar
import random

#tp1
#test de l'exo1
person1 = Person.Person("femme",53,155,20)
print("The basal metabolic rate of the person1 is : ",person1.basalMetabolicRate())
print("The energy requirement of the person1 is : ",person1.dailyEnergyRequirement(person1.basalMetabolicRate(),"light"))


#tp2
tab = pd.read_excel("TableS1_augmented_with_FAO_data.xlsx")
d = {'Dark Chocolate' : 30,'Beet Sugar' : 8,'Barley (Beer)' : 14,'Coffee' : 8,'Cane Sugar' : 8,'Wine' : 120 }

#print(tab)

#allMeal = ListMeal.ListMeal(tab).generateAllMeal(d,720)

 #this code works
ingredients = tab.loc[(tab['Product'] == 'Poultry Meat') | (tab['Product'] == 'Wheat & Rye (Bread)') | (tab['Product'] == 'Olive Oil') | (tab['Product']  == 'Root Vegetables') |
(tab['Product'] == 'Berries & Grapes') | (tab['Product'] == 'Coffee')]
ingredients.index = [0,1,2,3,4,5]
test1 = nutrition.nutrition(ingredients)
test1.listCalSources(d,720)


impact_ingredients = enviImpact.enviImpact(ingredients)
#print(impact.impact())
print(impact_ingredients.vecteur(d,720))

#tp4
meal1 = tab.loc[(tab['Product'] == 'Bovine Meat (beef herd)') | (tab['Product'] == 'Rice') | (tab['Product'] == 'Rapeseed Oil') | (tab['Product']  == 'Brassicas') |
(tab['Product'] == 'Apples') | (tab['Product'] == 'Beet Sugar')]
meal1.index = [0,1,2,3,4,5]
#print(meal1)
#print(meal1.at[0,'Product'])

test2 = nutrition.nutrition(meal1)
test2.listCalSources(d,803)
print()
impact_meal1 = enviImpact.enviImpact(meal1)
print(impact_meal1.vecteur(d,803))


meal2 = tab.loc[(tab['Product'] == 'Peas') | (tab['Product'] == 'Rice') | (tab['Product'] == 'Rapeseed Oil') | (tab['Product']  == 'Brassicas') |
(tab['Product'] == 'Apples') | (tab['Product'] == 'Beet Sugar')]
meal2.index = [0,1,2,3,4,5]
#print(meal2)
test3 = nutrition.nutrition(meal2)
test3.listCalSources(d,803)
impact_meal2 = enviImpact.enviImpact(meal2)
print(impact_meal2.vecteur(d,803))


'''
#lab6
cal= calendar.Calendar()
list1 = [1,2,3,4,5]
f = open("output.txt", 'w')
for i in range(12):
    for x in cal.itermonthdates(2023,i+1):
        if x.month == i+1 :
            print(x,file = f)
            print(random.sample(allMeal,2),file = f)
            print()
f.close()
'''

meal3 = tab.loc[(tab['Product'] == 'Fish (farmed)') | (tab['Product'] == 'Rice') | (tab['Product'] == 'Rapeseed Oil') | (tab['Product']  == 'Brassicas') |
(tab['Product'] == 'Apples') | (tab['Product'] == 'Beet Sugar')]
meal3.index = [0,1,2,3,4,5]
#print(meal1)
#print(meal1.at[0,'Product'])

test3 = nutrition.nutrition(meal3)
test3.listCalSources(d,803)
print()
impact_meal3 = enviImpact.enviImpact(meal3)
print(impact_meal3.vecteur(d,803))
