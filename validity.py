def valid(str):
    valid_publishers = ['All Recipes', 'Back to Her Roots', 'BBC Food', 'Bon Appetit', 'Closet Cooking', 'Cookin Canuck', 'Epicurious', 'Food Republic', 'Framed Cooks', 'Healthy Delicious', 'Jamie Oliver', "Lisa's Kitchen","My Baking Addiction","Panini Happy","PBS Food","Pillsbury Baking","Real Simple","Two Peas and Their Pod","Vintage Mixer","What's Gaby Cooking","Whats Gaby Cooking"]
    for i in range(len(valid_publishers)):
        if (str == valid_publishers[i]):
            return True
    return False
