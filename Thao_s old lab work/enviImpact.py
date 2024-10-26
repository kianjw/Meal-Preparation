#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 15:11:28 2023

@author: pchu
"""
import pandas as pd
import numpy as np
import math
import nutrition
#import nutrition

class enviImpact :
    def __init__ (self,meal) :
        self.meal = meal

    def impact(self):
        tab = pd.read_excel("5-DataS2.xlsx",sheet_name = "Results - Retail Weight", usecols = "A,E,K,W,AC,AO")
        tabNoIndex = pd.read_excel("5-DataS2.xlsx",sheet_name = "Results - Retail Weight", usecols = "A,E,K,W,AC,AO",index_col=0)
        #print([tab[tab['Unnamed: 0']] == 'Apples'].loc[3] == 0.51)
        #print(tabNoIndex)
        #print(tabNoIndex.at['Apples','Unnamed: 4'] == 0.51)
        return tabNoIndex


    def vecteur(self,d,K) :
        meal = self.meal
        tab = self.impact()
        nu = nutrition.nutrition(meal).listCalSources(d,K)
        land = 0
        GHG = 0
        acide = 0
        eutroph = 0
        freshwater = 0
        for i in range(len(meal)) :
            land = land + tab.at[meal.at[i,'Product'],'Unnamed: 4']*0.001*nu[i]
            GHG = GHG + tab.at[meal.at[i,'Product'],'Unnamed: 10']*0.001*nu[i]
            acide = acide + tab.at[meal.at[i,'Product'],'Unnamed: 22']*0.001*nu[i]
            eutroph = eutroph + tab.at[meal.at[i,'Product'],'Unnamed: 28']*0.001*nu[i]
            freshwater = freshwater + tab.at[meal.at[i,'Product'],'Unnamed: 40']*0.001*nu[i]
        """
        for i in range(len(meal)) :
            land = land + tab.at[meal.at[i,'Product'],'Unnamed: 4']*0.001*nutrition.listCalSources(meal, d, K)[i]
            GHG = GHG + tab.at[meal.at[i,'Product'],'Unnamed: 10']*0.001*nutrition.listCalSources(meal, d, K)[i]
            acide = acide + tab.at[meal.at[i,'Product'],'Unnamed: 22']*0.001*nutrition.listCalSources(meal, d, K)[i]
            eutroph = eutroph + tab.at[meal.at[i,'Product'],'Unnamed: 28']*0.001*nutrition.listCalSources(meal, d, K)[i]
            freshwater = freshwater + tab.at[meal.at[i,'Product'],'Unnamed: 40']*0.001*nutrition.listCalSources(meal, d, K)[i]
            """
        return np.array([land,GHG,acide,eutroph,freshwater],np.double)
