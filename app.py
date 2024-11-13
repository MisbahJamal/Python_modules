

# # import pandas as pd
# # import numpy as np
# # from sklearn.model_selection import train_test_split
# # from sklearn.linear_model import LinearRegression
# # from sklearn.metrics import mean_squared_error
# # import yfinance as yf
# # import matplotlib.pyplot as plt
# # # Download Bitcoin data
# # data = yf.download('BTC-USD', start='2010-01-01', end='2022-02-26')

# # # Reset index to convert date to a column
# # data.reset_index(inplace=True)

# # # Convert date to datetime
# # data['Date'] = pd.to_datetime(data['Date'])

# # # Create a new column 'Days' to represent the number of days since the start date
# # data['Days'] = (data['Date'] - data['Date'].min()).dt.days

# # # Define features (X) and target (y)
# # X = data[['Days']]
# # y = data['Close']

# # # Split data into training and testing sets
# # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # # Create a Linear Regression model
# # model = LinearRegression()

# # # Train the model
# # model.fit(X_train, y_train)

# # # Make predictions
# # predictions = model.predict(X_test)

# # # Evaluate the model
# # mse = mean_squared_error(y_test, predictions)
# # print(f'Mean Squared Error: {mse}')

# # # Plot the data and predictions
# # plt.figure(figsize=(10,6))
# # plt.plot(data['Date'], data['Close'], label='Actual')
# # plt.plot(X_test['Days'], predictions, label='Predictions')
# # plt.legend()
# # plt.show()



# #list example 

# uni_deptt = ["AI", "DS", "SE", "CS"]
# uni_deptt.append("Cyber Security")
# print(uni_deptt)



# #Tuple example 
# car_brands=("Ferrari","Mercedez","BMW","Toyota")
# print(car_brands)



# #noe set dat stucture 



# car_brands_set={"Audi","Changan ","bugatti","bugatti"}
# print(car_brands_set)
# #as in the set  data structure we can see it can,t print the repition



# #now thelast one is dictionary
# #in which we store the data in the key value pair

# car_brands_dict={"Ferrari":"Germany","Mercedez":"Germany","BMW":"Germany","Toyota":"Japan"}
# print(car_brands_dict)


# #slicing in python 
# #to fetch the required data only

# print(car_brands[2])

# #for the first three car brands in the list 

# print(car_brands[0:2])


# #CONIDTIONAL STATEMENT IN PYTHON 
# age=int(input("please enter your age here"))
# if age>18 :
#    print("Congratulations you are eligible for driving license")
# else:
#     print("You are not eligible for driving license")
    
    
    
# i=1
# while i < 5:
#     print("Rehman")
#     i=i+1
    
    
#     break
#     #now for loop 
# for j in range(5):
#     print("ali")
#     j=j+1

# age=int(input("Please enter your age: "))
# gender=input("Please enter your gender (Male/Female): ")

# if gender.lower()=="male":
#     if age>18:
#         print("You are eligible")
#     else:
#         print("Sorry, you are not eligible")

def greet(name):
    print(f"Hello, {name}!")
    
    
    print("hello world")