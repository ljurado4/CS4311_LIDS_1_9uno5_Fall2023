import unittest
from backend.PortChecker import PortDetection  # Import the portDetection class from your actual module


class TestPortDetection(unittest.TestCase):

    def test_update_connection_count_threshold_exceeded(self):
        detector = PortDetection()
        ip = "192.168.1.1"
        port = 80
        threshold = 10
        for _ in range(threshold - 1):
            result = detector.update_connection_count(ip, port, threshold)
            self.assertFalse(result)  # Expects False before reaching the threshold
        result = detector.update_connection_count(ip, port, threshold)
        self.assertTrue(result)  # Expects True after reaching the threshold


    def test_update_connection_count_threshold_not_exceeded(self):
        # Create an instance of PortDetection
        detector = PortDetection()

        # Add connections below the threshold (e.g., 5)
        for _ in range(5):
            result = detector.update_connection_count("192.168.1.1", 80, 10)
            self.assertFalse(result)  # Expects False for all connections

    def test_update_connection_count_unique_connections(self):
        # Create an instance of PortDetection
        detector = PortDetection()

        # Add connections with different (ip, port) pairs
        result1 = detector.update_connection_count("192.168.1.1", 80, 5)
        result2 = detector.update_connection_count("192.168.1.1", 8080, 5)
        result3 = detector.update_connection_count("192.168.1.2", 80, 5)

        self.assertFalse(result1)  # Expect False for the first connection
        self.assertFalse(result2)  # Expect False for the second connection
        self.assertFalse(result3)  # Expect False for the third connection

if __name__ == '__main__':
    unittest.main()
