import pandas as pd
import numpy as np
import math
import nutrition

class ListMeal :
    def __init__ (self,all_ingredients):
        self.all_ingredients = all_ingredients

    def generateAllMeal (self,d,K):
        tab = self.all_ingredients
        list = []
        prot = []
        carb = []
        fat = []
        fruit = []
        veg = []
        extra = []
        #create a new table
        for i in range(len(tab)) :
            if (tab.at[i,'Type'] == 'ProteinSource') :
                prot.append(tab.at[i,'Product'])
        for j in range(len(tab)) :
            if (tab.at[j,'Type'] == 'CarbSource') :
                carb.append(tab.at[j,'Product'])
        for k in range(len(tab)) :
            if (tab.at[k,'Type'] == 'FatSource') :
                fat.append(tab.at[k,'Product'])
        for l in range(len(tab)) :
            if (tab.at[l,'Type'] == 'Fruit') :
                fruit.append(tab.at[l,'Product'])
        for m in range(len(tab)) :
            if (tab.at[m,'Type'] == 'Vegetable') :
                veg.append(tab.at[m,'Product'])
        for n in range(len(tab)) :
            if (tab.at[n,'Type'] == 'Extra') :
                extra.append(tab.at[n,'Product'])

        for i in range(len(prot)) :
            for j in range(len(carb)) :
                for k in range(len(fat)) :
                    for l in range(len(fruit)) :
                        for m in range(len(veg)) :
                            for n in range(len(extra)) :
                                meal = tab.loc[(tab['Product'] == prot[i]) | (tab['Product'] == carb[j]) | (tab['Product'] == fat[k]) |
                                (tab['Product']  == fruit[l]) | (tab['Product'] == veg[m]) | (tab['Product'] == extra[n])]
                                meal.index = [0,1,2,3,4,5]
                                #print(meal)al.index = [0,1,2,3,4,5]
                                #print(meal)
                                test = nutrition.nutrition(meal)
                                q = test.listCalSources(d,K)
                                a = 0
                                while (a<len(q) and q[a] > 0):
                                    a = a + 1
                                if (a==len(q)) :
                                    list.append(meal)
                                """
                                test = nutrition.nutrition(meal)
                                q = test.listCalSources(d,K)
                                a = 0
                                while (a<len(q) and q[a] > 0):
                                    a = a + 1
                                if (a==len(q)) :
                                    list.append(meal)
                                """

        print(len(list))
        return list
