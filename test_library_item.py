import unittest
from library_item import LibraryItem

class TestLibraryItem(unittest.TestCase):
    
    #___________test "info" without provided rating_____________#
    def test_info_with_no_rating(self):
        item = LibraryItem(name="Love, Chunibyo & Other Delusions", director="Torako")
        self.assertEqual(item.info(), "Love, Chunibyo & Other Delusions - Torako ")

    #___________test "info" with provided rating_____________#    
    def test_info_with_rating(self):
        item = LibraryItem(name="Love, Chunibyo & Other Delusions", director="Torako", rating=3)
        self.assertEqual(item.info(), "Love, Chunibyo & Other Delusions - Torako ***")

    #___________test "stars" without provided rating_____________# 
    def test_stars_with_no_rating(self):
        item = LibraryItem(name="Love, Chunibyo & Other Delusions", director="Torako")
        self.assertEqual(item.stars(), "")

    #___________test "stars" with provided rating_____________# 
    def test_stars_with_rating(self):
        item = LibraryItem(name="Love, Chunibyo & Other Delusions", director="Torako", rating=5)
        self.assertEqual(item.stars(), "*****")

    #___________test if "play_count" begins at the correct value_____________# 
    def test_play_count(self):
        item = LibraryItem(name="Love, Chunibyo & Other Delusions", director="Torako", play_count=23)
        self.assertEqual(item.play_count, 23)

    #___________test if "key" is assiged "None" by default_____________# 
    def test_key_default_none(self):
        item = LibraryItem(name="Love, Chunibyo & Other Delusions", director="Torako")
        self.assertIsNone(item.key)

    #___________test if "key" is retrieved correctly_____________# 
    def test_key_assignment(self):
        item = LibraryItem(name="Love, Chunibyo & Other Delusions", director="Torako", key="anything")
        self.assertEqual(item.key, "anything")

if __name__ == '__main__':
    unittest.main()