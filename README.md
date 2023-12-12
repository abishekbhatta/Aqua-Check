# Aqua Check

[![Video](https://img.youtube.com/vi/bS5incV2Yxc/maxresdefault.jpg)](https://www.youtube.com/watch?v=bS5incV2Yxc)

# What it does?

Unlike lab tests on water samples, Aqua Check uses a machine learning model and a water pollution dataset to detect whether water is polluted or not and then displays the results to the user. To make the prediction, it takes the following values from a water sample as input:

- pH
- Hardness
- Total Dissolved Solids
- Amount of Chloramines, Sulfate, Trihalomethanes, and Organic Carbon
- Conductivity
- Turbidity

# How I built it?

The machine learning model used in Aqua Check is the Random Forest Classifier. I implemented it using Python’s scikit-learn library. To make the model more user-friendly, I deployed it into a web app using the Streamlit framework. Besides, I also used some CSS to tweak certain features in Streamlit.

# Challenges I ran into

First, I was working solo, so I had to manage all the tasks on my own. Second, there were numerous machine learning algorithms to choose from, so I had to spend hours testing each to figure out the most efficient algorithm before actually implementing it. Third, I had no experience with Streamlit, so I had to go through its documentation on implementing different APIs and fixing errors as they appeared.

# What I learned?

Throughout the project, I learned to deploy a machine learning model into a web app using Streamlit. I also gained valuable experience in optimizing the machine learning model using Z-score normalization and oversampling techniques.

# What's next for Aqua Check?

The machine learning model used in Aqua Check can be further enhanced to make its predictions more accurate. In the future, Aqua Check can be integrated into a physical device with sensors that can simultaneously measure pH values, water hardness, etc. listed above and predict water contamination.
