import pandas as pd
import numpy as np
import math

class Person :
    def __init__ (self,sexe,poids,taille,age) :
        self.sexe = sexe
        self.poids = poids
        self.taille = taille
        self.age = age

    def basalMetabolicRate (self) :
      """
      calculate the basal metabolic rate un kcal of a person
      Parameters in data mode: sexe, poids, taille, age
      Parameters in data/result mode : [none]
      Parameters in result mode : [none]
      Preconditions : sexe is a str, poids, taille, age are integers
      Postconditions : [none]
      Result: a floating-poiny number which is the result of the equation
      """
      metabolicRate = 0
      if (self.sexe == "homme") :
        metabolicRate = 10*self.poids + 6.25*self.taille - 5*self.age + 5
      else :
        metabolicRate = 10*self.poids + 6.25*self.taille - 5*self.age - 161
      return metabolicRate

    #question1.4
    def dailyEnergyRequirement (self,metabolicRate,phyLevel) :
        """
        calculate the daily energy requirement of a person
        Parameters in data mode: metabolicRate, phyLevel
        Parameters in data/result mode : [none]
        Parameters in result mode : [none]
        Preconditions : metabolicRate is a floating-point number, phyLevel is a str
        Postconditions : [none]
        Result: a floating-point number which is the result of the equation
        """
        k = 0
        if (phyLevel == "sedentary") :
            k = 1.4
        elif (phyLevel == "light") :
            k = 1.6
        elif (phyLevel == "intense") :
            k = 1.9
        elif (phyLevel == "very intense") :
            k = 2.1
        return k*metabolicRate

    def approx (a,b,epsilon) :
        """
        Comparison of floating-point numbers
        Parameters in data mode: a,b,epsilon
        Parameters in data/result mode : [none]
        Parameters in result mode : [none]
        Preconditions : a,b,epsilon are floating-point numbers
        Postconditions : [none]
        Result: TRUE or FALSE
        """
        c = False
        if (abs(a)<=epsilon or abs(b)<=epsilon) :
            c = abs(a-b)<epsilon
        else :
            c = (abs(a-b)/int(math.log10(max(abs(a),abs(b)))))<epsilon
        return c
