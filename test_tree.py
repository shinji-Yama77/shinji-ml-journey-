import unittest
from decisiontree import ID3
import numpy as np

class TestTree(unittest.TestCase):

    def setUp(self):
        self.X = np.array([[1,1,1],[1,0,1],[1,0,0],[1,0,0],[1,1,1],[0,1,1],[0,0,0],[1,0,1],[0,1,0],[1,0,0]])
        self.y = np.array([1,1,0,0,1,0,0,1,1,0])

    def test_cal_entropy(self):
        indices = np.array([0, 1, 2, 3, 4])
        indices = np.arange(len(self.y))
        id3 = ID3()
        entropy = id3.cal_entropy(self.y, indices)
        self.assertAlmostEqual(entropy, 0.97095, places=5)
    
    def test_compute_gain(self):
        # Test compute_gain function
        left_indices = np.array([0, 1, 4])
        right_indices = np.array([2, 3])
        id3 = ID3()
        gain = id3.compute_gain(left_indices, right_indices, self.y)
        self.assertAlmostEqual(gain, 0.97095, places=5)

    def test_find_split(self):
        # Test find_split function
        id3 = ID3(num_features=3)
        best_feature, best_thresh = id3.find_split(self.X, self.y)
        print(best_feature)
        self.assertEqual(best_feature, 2)  # Update with your expected value
        self.assertEqual(best_thresh, 0.5)
    

if __name__ == '__main__':
    unittest.main()

