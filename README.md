# Aqua Check

![Aqua-Check](https://github.com/abishekbhatta/Aqua-Check/assets/131245708/a2100caa-fb84-4c6b-9a36-b299fdec495b)

# Inspiration

Water pollution today has led to various detrimental impacts on the environment, like eutrophication, the loss of entire aquatic species, and plastic ingestion. Hence, there is a strong need to control water pollution to protect our environment, and the first step would be checking whether water sources are contaminated or not before carrying out any cleaning campaigns.

Water contamination can be checked in the lab by performing different tests, but it takes more time for the results to be prepared, ultimately delaying the cleaning campaigns. Therefore, to speed up the checking process, I have built Aqua Check, which uses an automated process to identify water contamination.

# What it does

Unlike lab tests on water samples, Aqua Check uses a machine learning model and a water pollution dataset to detect whether water is polluted or not and then displays the results to the user. To make the prediction, it takes the following values from a water sample as input:

- pH
- Hardness
- Total Dissolved Solids
- Amount of Chloramines, Sulfate, Trihalomethanes, and Organic Carbon
- Conductivity
- Turbidity

# How I built it

The machine learning model used in Aqua Check is the Random Forest Classifier. I implemented it using Python’s scikit-learn library. To make the model more user-friendly, I deployed it into a web app using the Streamlit framework. Besides, I also used some CSS to tweak certain features in Streamlit.

# Challenges I ran into

First, I was working solo, so I had to manage all the tasks on my own. Second, there were numerous machine learning algorithms to choose from, so I had to spend hours testing each to figure out the most efficient algorithm before actually implementing it. Third, I had no experience with Streamlit, so I had to go through its documentation on implementing different APIs and fixing errors as they appeared.

# Accomplishments that I'm proud of

As a solo participant using a totally new framework, I was able to build a fully functional machine learning app that addressed a serious environmental concern in my first ever hackathon.

# What I learned

Throughout the project, I learned to deploy a machine learning model into a web app using Streamlit. I also gained valuable experience in optimizing the machine learning model using Z-score normalization and oversampling techniques.

# What's next for Aqua Check?

The machine learning model used in Aqua Check can be further enhanced to make its predictions more accurate. In the future, Aqua Check can be integrated into a physical device with sensors that can simultaneously measure pH values, water hardness, etc. listed above and predict water contamination.

# Demo
https://abishekbhatta-aqua-check-app-xnqa0c.streamlit.app/
