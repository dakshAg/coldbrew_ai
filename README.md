# coldbrew_ai
AI Repo for the ColdBrew product

# objective
The main goal of this repo is to recognise an object from some data that can be collected on a smartphone.

# available data
text input
    Product on internet
camera
    if label:
        scan barcode and extract ingredients
    else:

audio

# output goal
list of ingredients


# FIRST GOAL
Make a model that uses computer vision to tell us what kind of product we are taking a photo of.
    Easy option:
        Use existing product like google lens or amazon.
        Google Lens has an API.
        Amazon also has an API. 
        First ask the user to take a photo of the product.
        Then ask them to select the exact product that they are trying to learn about.
        If the scrape returns bad data then iterate through the similar product websites until that data is obtained.

    Medium option:
        Build a model from freely available data
    Hard option: 
        Collect our own data and use it to build a model

# SECOND GOAL
Make a model that extracts the text from a label and gives us information about the ingredients that are used to make the product as well as the manufacturers.

# THIRD GOAL
Transform the information into a sustainability score by using our algorithm.

# FOURTH GOAL
Transform the information into a guide on how to dispose based on the waste management algorithm that we designed.

# FIFTH GOAL
Give the data to the web app.