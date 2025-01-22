class KNN:
    def __init__(self):
        self.points = {}

    def addPoint(self, point, label):
        self.points[point] = label

    def euclidean(point1, point2):
        return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5
    
    def sort_distances(distances):
        for i in range(len(distances)):
            for j in range(len(distances) - 1 - i):
                if(distances[j][0] > distances[j + 1][0]):
                    temp = distances[j + 1]
                    distances[j + 1] = distances[j]
                    distances[j] = temp
        return distances

    def classify(self, point, k=3):
        distances = []
        for known_point, label in self.points.items():
            distances.append((KNN.euclidean(point, known_point), label))
        sorted_distances = KNN.sort_distances(distances)
        labels = [label for _, label in distances[:k]]

        label_counts = {}
        for label in labels:
            if label in label_counts:
                label_counts[label] += 1
            else:
                label_counts[label] = 1

        max_count = 0
        most_common = None
        for label, count in label_counts.items():
            if count > max_count:
                max_count = count
                most_common = label

        return most_common