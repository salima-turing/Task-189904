import unittest
import numpy as np
from typing import List

def aggregate_data(client_data: List[np.ndarray]) -> np.ndarray:
	"""
	A simple aggregation function for testing data sharing.
	It concatenates client data along the first axis.
	"""
	return np.concatenate(client_data, axis=0)

class TestDataSharing(unittest.TestCase):

	def test_aggregate_data(self):
		# Dummy data for different clients
		client1_data = np.array([[1, 2], [3, 4]])
		client2_data = np.array([[5, 6], [7, 8]])
		client3_data = np.array([[9, 10]])

		expected_aggregated_data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])

		# Test the aggregation function
		aggregated_data = aggregate_data([client1_data, client2_data, client3_data])
		np.testing.assert_array_equal(aggregated_data, expected_aggregated_data, "Aggregation failed")

if __name__ == '__main__':
	unittest.main()
