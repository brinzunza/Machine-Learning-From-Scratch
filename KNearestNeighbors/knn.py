'''
- Supervised learning classification algorithm
- logic
    - from an existing dataset with points (x, y), find the distances(euclidean, manhattan, minkowski distance) of the new point against all other points in dataset
    - find the closest k points (k being a predefined integer)
    - classify new point based on the majority class of those k nearest points

- Euclidean Distance is being used in this implementation being: Assume two points (x1, y1) and (x2, y2) ED = sqrt((x2 - x1)^2 + (y2 - y1)^2)
- K has to be carefully chosen based on the dataset. 
    - Choose odd number to avoid ties
    - High value of k if a lot of outliers or noise exists
    - Cross validation can be used to find most effective value of k
- Sorting method used is bubble sort(although it is not the most efficient sorting algorithm)
'''

class KNN:
    def __init__():
        points = {}

    def euclidean(point1, point2):
        return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5

    def newPoint(point, k):
        distances = []
        for i in points.keys:
            distances.append([euclidean(point, i), i])
        sorted_distances = sort(distances)
        class_ranking = {}
        for i in range(k):
            


    def sort(distances):
        for i in range(len(distances)):
            for j in range(len(distances) - 1 - i):
                if(distances[j] > distances[j + 1]):
                    temp = distances[j + 1]
                    distances[j + 1] = distances[j]
                    distances[j] = temp