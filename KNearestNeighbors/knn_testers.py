from knn import KNN
import matplotlib.pyplot as plt

def test_knn(x, y):
    knn = KNN()

    knn.addPoint((1, 2), 'A')
    knn.addPoint((2, 3), 'A')
    knn.addPoint((3, 1), 'B')
    knn.addPoint((6, 5), 'B')
    knn.addPoint((7, 8), 'A')
    knn.addPoint((1, 4), 'A')
    knn.addPoint((2, 5), 'A')
    knn.addPoint((3, 6), 'B')
    knn.addPoint((4, 2), 'A')
    knn.addPoint((5, 3), 'B')
    knn.addPoint((6, 1), 'A')
    knn.addPoint((7, 4), 'B')
    knn.addPoint((8, 5), 'A')
    knn.addPoint((9, 6), 'B')
    knn.addPoint((10, 7), 'A')
    knn.addPoint((11, 8), 'B')
    knn.addPoint((12, 2), 'A')
    knn.addPoint((13, 3), 'B')
    knn.addPoint((14, 4), 'A')
    knn.addPoint((15, 5), 'B')
    knn.addPoint((16, 6), 'A')
    knn.addPoint((17, 7), 'B')
    knn.addPoint((18, 8), 'A')
    knn.addPoint((19, 1), 'B')
    knn.addPoint((20, 2), 'A')
    knn.addPoint((21, 3), 'B')

    test_point = (x, y)
    predicted_label = knn.classify(test_point, k=3)
    print(f'Test Point: {test_point}, Predicted Label: {predicted_label}')

    points = list(knn.points.keys())
    labels = list(knn.points.values())

    plt.figure(figsize=(8, 6))
    for point, label in zip(points, labels):
        if label == 'A':
            plt.scatter(point[0], point[1], color='blue', label=label)
        else:
            plt.scatter(point[0], point[1], color='green', label=label)

    plt.scatter(test_point[0], test_point[1], color='red', marker='x', s=100, label='Test Point')
    plt.title("KNN Classification: Predicted Label = " + predicted_label)
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    test_knn(3, 4)