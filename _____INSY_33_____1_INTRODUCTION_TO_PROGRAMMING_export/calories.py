def showCarbs(gramsFat,gramsCarbs,caloriesFat,caloriesCarbs): 
    print("Grams of fat: {:.2f}".format(gramsFat))
    #.2f displays two digits after decimal for fat grams
    print("Fat calories: {:.2f}".format(caloriesFat))
    #.2f displays two digits after decimal for fat calories
    print("Grams of carbs: {:.2f}".format(gramsCarbs))
    #.2f displays two digits after decimal for grams of carbs
    print("Carbs calories: {:.2f}".format(caloriesCarbs))
    #.2f displays two digits after decimal for carb calories
def main():
    gramsFat=float(input("Enter fat grams consumed: "))
    gramsCarbs=float(input("Enter carbohydrate grams consumed: "))
    caloriesFat=gramsFat*9 #Calculating calories from fat
    caloriesCarbs=gramsCarbs*4 #Calculating calories from carbs
    showCarbs(gramsFat,gramsCarbs,caloriesFat,caloriesCarbs)
if __name__ == "__main__": #executes code inside from the file 
    main()

