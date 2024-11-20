import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):
        # Test case 1: Input with joy
        result_1 = emotion_detector("I am so happy today!")
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test case 2: Input with anger
        result_2 = emotion_detector("I am really angry about this situation!")
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Test case 3: Input with disgust
        result_3 = emotion_detector("This is so disgusting, I can't believe it!")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Test case 4: Input with sadness
        result_4 = emotion_detector("I feel so sad and down.")
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # Test case 5: Input with fear
        result_5 = emotion_detector("I am so afraid this might happen again.")
        self.assertEqual(result_5['dominant_emotion'], 'fear')

        # Test case 6: Invalid input (empty string)
        result_6 = emotion_detector("")
        self.assertIn('error', result_6)

    def test_error_handling(self):
        # Test case 7: API failure handling
        # Simulate a case where API fails by passing unusual input
        result = emotion_detector("##@@##$$!!")
        if 'error' in result:
            self.assertEqual(result['error'], 'Failed to get response from the API')

unittest.main()
