#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 14:22:21 2023

@author: pchu
"""

import pandas as pd
import numpy as np
import math

class nutrition :
    def __init__ (self,ingredients) :
        self.ingredients = ingredients

    #question4
    #@profile
    def listCalSources(self,d,K) :
        ingredients = self.ingredients
        q_fruit = 50
        q_veg = 125
        name_extra = ingredients[ingredients['Type'] == 'Extra']['Product'].squeeze()
        q_ex = d[name_extra]

        Cps = ingredients[ingredients['Type'] == 'ProteinSource']['gCarbPerRetailUnit'].squeeze()
        Fps = ingredients[ingredients['Type'] == 'ProteinSource']['gFatPerRetailUnit'].squeeze()
        Pps = ingredients[ingredients['Type'] == 'ProteinSource']['gProteinPerRetailUnit'].squeeze()

        Ccs = ingredients[ingredients['Type'] == 'CarbSource']['gCarbPerRetailUnit'].squeeze()
        Fcs = ingredients[ingredients['Type'] == 'CarbSource']['gFatPerRetailUnit'].squeeze()
        Pcs = ingredients[ingredients['Type'] == 'CarbSource']['gProteinPerRetailUnit'].squeeze()

        Cfs = ingredients[ingredients['Type'] == 'FatSource']['gCarbPerRetailUnit'].squeeze()
        Ffs = ingredients[ingredients['Type'] == 'FatSource']['gFatPerRetailUnit'].squeeze()
        Pfs = ingredients[ingredients['Type'] == 'FatSource']['gProteinPerRetailUnit'].squeeze()

        C_veg = ingredients[ingredients['Type'] == 'Vegetable']['gCarbPerRetailUnit'].squeeze()
        F_veg = ingredients[ingredients['Type'] == 'Vegetable']['gFatPerRetailUnit'].squeeze()
        P_veg = ingredients[ingredients['Type'] == 'Vegetable']['gProteinPerRetailUnit'].squeeze()

        C_fruit = ingredients[ingredients['Type'] == 'Fruit']['gCarbPerRetailUnit'].squeeze()
        F_fruit = ingredients[ingredients['Type'] == 'Fruit']['gFatPerRetailUnit'].squeeze()
        P_fruit = ingredients[ingredients['Type'] == 'Fruit']['gProteinPerRetailUnit'].squeeze()

        C_ex = ingredients[ingredients['Type'] == 'Extra']['gCarbPerRetailUnit'].squeeze()
        F_ex = ingredients[ingredients['Type'] == 'Extra']['gFatPerRetailUnit'].squeeze()
        P_ex = ingredients[ingredients['Type'] == 'Extra']['gProteinPerRetailUnit'].squeeze()


        carb = 0.66*K/4 - C_ex*0.001*q_ex - C_fruit*0.001*q_fruit - C_veg*0.001*q_veg
        fat = 0.22*K/8.8 - (F_ex*q_ex + F_fruit*q_fruit + F_veg*q_veg)*0.001
        prot = 0.12*K/4 - (P_ex*q_ex + P_fruit*q_fruit + P_veg*q_veg)*0.001
        #A = np.array([[Cps,Ccs,Cfs],[Fps,Fcs,Ffs],[Pps,Pcs,Pfs]],np.double)
        A = np.array([[Cps*0.001,Ccs*0.001,Cfs*0.001],[Fps*0.001,Fcs*0.001,Ffs*0.001],[Pps*0.001,Pcs*0.001,Pfs*0.001]],np.double)
        if __name__ == "__main__":
            print(A)
        b = np.array([carb,fat,prot])
        x = np.linalg.solve(A,b)

        q = np.array([x[1],q_ex,x[2],q_fruit,x[0],q_veg],int)
        #q = np.array([])

        for i in range(len(ingredients)) :
            if (ingredients.at[i,'Type'] == 'ProteinSource') :
                q[i] = int(x[0])
            elif (ingredients.at[i,'Type'] == 'CarbSource') :
                q[i] = int(x[1])
            elif (ingredients.at[i,'Type'] == 'FatSource') :
                q[i] = int(x[2])
            elif (ingredients.at[i,'Type'] == 'Vegetable') :
                q[i] = q_veg
            elif (ingredients.at[i,'Type'] == 'Fruit') :
                q[i] = q_fruit
            elif (ingredients.at[i,'Type'] == 'Extra') :
                q[i] = q_ex

        """ #this part works
        print('The meal is composed of :')
        print('----------------------------------------------------------')
        template1 = "{0:5.0f} g of {1:5} contributing {2:5.0f} kcal {3:5.1f} g protein {4:5.1f} g carb {5:5.1f} g fat"
        template2 = "TOTAL:   {2:5.0f} kcal {3:5.0f} g protein {4:5.0f} g carb {5:5.0f} g fat"
        kcalTot = 0
        protTot = 0
        carbTot = 0
        fatTot = 0
        #print(q[0]*0.001*ingredients.at[0,'kcalPerRetailUnit'])

        for i in range(len(ingredients)) :
            kcal = q[i]*0.001*ingredients.at[i,'kcalPerRetailUnit']
            prot = q[i]*0.001*ingredients.at[i,'gProteinPerRetailUnit']
            carb = q[i]*0.001*ingredients.at[i,'gCarbPerRetailUnit']
            fat = q[i]*0.001*ingredients.at[i,'gFatPerRetailUnit']
            #print(kcal)
            print(template1.format(q[i],ingredients.at[i,'Product'],kcal,prot,carb,fat))
            kcalTot = kcalTot + kcal
            protTot = protTot + prot
            carbTot = carbTot + carb
            fatTot = fatTot + fat

        #print(kcalTot)
        print('----------------------------------------------------------')
        print(template2.format('     ','     ',kcalTot,protTot,carbTot,fatTot))
        print(q)
        """
        return q
