## **Business Problem**
The business problem addressed in this portfolio is to develop a reliable taxi fare prediction system that helps customers estimate trip prices before booking. At the same time, by understanding determinant factors through modeling, the company can improve pricing consistency, optimize operational decisions, and design strategies that align fare structures with real trip dynamics. This dual approach—accurate prediction and deeper insight—supports better customer transparency while strengthening the company’s internal pricing framework.

---

### **Objectives**
- The objective of this project is to build a machine learning model capable of predicting taxi fares based on key trip features such as distance, duration, time of day, traffic, and weather. 
- The model will then be deployed through a Streamlit application to allow users to generate fare estimates instantly.
- Beyond prediction, the project also aims to identify the most influential factors behind pricing, helping the company refine fare policies and enhance strategic decision-making.

---

### **Metric Evaluation**
Model performance is evaluated using three core regression metrics:

- **MAE (Mean Absolute Error)** measures the average absolute difference between predicted fares and actual fares, providing a direct sense of how “off” each prediction is in currency terms.

- **RMSE (Root Mean Squared Error)** penalizes larger errors more heavily, ensuring the model remains reliable even in extreme or unusual cases.

- **MAPE (Mean Absolute Percentage Error)** expresses prediction error as a percentage, making it easier for the company to understand model accuracy relative to trip cost levels.

Together, these metrics give a balanced view of both practical and statistical performance, ensuring the model is accurate enough for customer-facing deployment.

---

### **Goals**
The goal of this project is to build a reliable and transparent taxi fare prediction system that allows users to estimate trip prices before booking, while also uncovering the key factors that drive the company’s pricing structure. By combining accurate machine learning predictions with feature-level insights, the project aims to support fairer and more consistent fare calculations, improve customer trust, and provide the company with data-driven guidance for refining future pricing strategies.

---

#### **Data Overview**

1. This dataset contains of 1000 rows and 11 columns.
2. There are 10 features and 1 target variable in this dataset.
3. The features consist of 6 numerical and 4 categorical data types.

---

#### **Columns Description**
---
##### **Features**
---
- trip_distance_km (in kilometers): The length of the trip.
    - Data Type: Numerical (float)
---
- time_of_day : The time of the trip.
    - Data Type: Object
    - Unique Values : Morning, Afternoon, Evening, Night
---
- day_of_week: The day of the week when the trip occurred.
    - Data Type: Object
    - Unique Values : Weekend, Weekday
---
- passenger_count : Number of passengers for the trip.
    - Data Type: Numerical (float)
---
- traffic_condition: Categorical indicator of traffic (low, medium, high).
    - Data Type: Object
---
- weather: Categorical data for weather (clear, rain, snow).
    - Data Type: Object
---
- base_fare (in USD): The initial fare for the trip.
    - Data Type: Numerical (float)
---
- per_km_rate (in USD/km): The rate charged per kilometer.
    - Data Type: Numerical (float)
---
- per_minute_rate (in USD/min): The rate charged per minute.
    - Data Type: Numerical (float)
---
- trip_duration_minutes: The duration of the trip in minutes.
    - Data Type: Numerical (float)
---
##### **Target Variable**
---
- trip_price (in USD): The total fare for the trip.
    - Data Type: Numerical (float)
 
---

## **Conclusion and Recommendations**

---

### **Conclusion**
1. The Gradient Boosting Regressor model **effectively predicts taxi fares with strong accuracy**, particularly **for trips under $150**, demonstrating its reliability for everyday fare estimation.

2. Key features such as trip **distance, duration, and pricing rates predominantly drive fare predictions**, while factors like **weather and traffic have minimal impact**.

---

### **Recommendations**

---

#### **Data Recommendations:**
1. **Collect More High-Fare Trip Data:** The model struggles with accurately predicting high-fare trips due to a lack of sufficient training examples in this range. Gathering more data on longer or premium trips would help the model learn patterns associated with higher prices, improving its accuracy for these cases.  
2. **Add More Granular Features:** Incorporating additional features such as exact hour of the day, special event indicators, or more detailed weather conditions could provide the model with richer context, potentially enhancing its predictive capabilities.  
3. **Incorporate Real-Time Traffic Data:** Integrating real-time traffic information could help the model account for dynamic conditions that affect trip duration and pricing, leading to more accurate fare predictions.

---

#### **Model Recommendations:**
1. **Use a Two-Stage Modeling Framework**: The residual plots show that the current model is highly accurate for fares below $150 but breaks down for high-fare trips. This suggests two distinct data sections. Implementing a two-stage pipeline—first classifying whether a trip is “normal fare” or “high fare,” and then applying a dedicated regressor for each group—allows each model to learn patterns specific to its range.  
2. **Train a Specialized High-Fare Regressor**: The extreme errors in expensive trips indicate that the model has too few examples to generalize their behavior. Training a separate model exclusively on trips above $150 helps capture the unique dynamics of long-distance or premium trips, significantly reducing prediction variance in this upper range.

---

#### **Business Recommendations:**
1. **Re-evaluate the Current Pricing Strategy**: By SHAP analysis, we know that the pricing formula is rigid (highly dependent on duration dan distance) and not capture the real trip complexity. The business should evaluate whether relying solely on these four variables is still relevant, especially when other companies increasingly incorporate more contextual pricing.  
2. **Implement Dynamic Pricing Models**: Consider adopting dynamic pricing strategies that adjust fares based on real-time factors such as demand, traffic conditions, and weather. This approach can help optimize revenue while providing fair pricing to customers during peak times or adverse conditions.  
