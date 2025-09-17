import heapq
from typing import List
from collections import defaultdict


class Food:
    def __init__(self, food_rating, food_name):
        self.food_rating = food_rating
        self.food_name = food_name

    def __lt__(self, other) -> bool:
        """
        overload the less-than operator for comparison.
        if food ratings are the same, sort based on their name
        (lexicographically smaller name food will be on top).
        """
        if self.food_rating == other.food_rating:
            return self.food_name < other.food_name
        # sort based on the food rating (higher rated food will be on top
        return self.food_rating > other.food_rating

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating_map = {}
        self.food_cuisine_map = {}
        self.cuisine_food_map = defaultdict(list)

        for i in range(len(foods)):
            # store 'rating' and 'cuisine' of the current 'food' in 'food_rating_map' and 'food_cuisine_map'
            self.food_rating_map[foods[i]] = ratings[i]
            self.food_cuisine_map[foods[i]] = cuisines[i]
            # insert the '(rating, name)' element into the current cuisine's priority queue
            #heapq.heappush(self.cuisine_food_map)


    def changeRating(self, food: str, newRating: int) -> None:
        

    def highestRated(self, cuisine: str) -> str:
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
