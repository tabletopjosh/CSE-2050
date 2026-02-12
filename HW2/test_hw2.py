import unittest #
from hw2 import Profile, Activity, Post, Message, User 

class TestProfile(unittest.TestCase):
    """Test cases for the Profile class."""
    
    def test_init(self):
        """Test initialization of Profile."""
        p = Profile("user1", "pass1", "Screen1", "u1@ex.com")  
        self.assertEqual(p.username, "user1")  
        self.assertEqual(p.email, "u1@ex.com")  

    def test_modify_profile(self):
        """Test modifying the profile."""
        p = Profile("user1", "pass1", "Screen1", "u1@ex.com")  
        p.modify_profile(email="new@ex.com")  
        self.assertEqual(p.email, "new@ex.com")  
        self.assertEqual(p.screen_name, "Screen1")  
    
    def test_str(self):
        """Test string representation."""
        p = Profile("user1", "pass1", "Screen1", "u1@ex.com") 
        expected = "Profile - Username: user1, Screen Name: Screen1, Email: u1@ex.com"  
        self.assertEqual(str(p), expected)  

class TestActivity(unittest.TestCase):
    """Test cases for the Activity class."""
    
    def test_init(self):
        """Test initialization of Activity."""
        u = User("u", "p", "s", "e") 
        a = Activity(u, "content")  
        self.assertEqual(a.user, u)  
        self.assertEqual(a.content, "content")  

class TestPost(unittest.TestCase):
    """Test cases for the Post class."""
    
    def test_str(self):
        """Test string representation of Post."""
        u = User("u", "p", "s", "e")  
        post = Post(u, "My Post")  
        expected = "Post - Activity - User: u, Content: My Post" 
        self.assertEqual(str(post), expected)  

class TestMessage(unittest.TestCase):
    """Test cases for the Message class."""

    def test_init(self):
        """Test initialization of Message."""
        u1 = User("u1", "p", "s", "e")  
        u2 = User("u2", "p", "s", "e")  
        msg = Message(u1, "Hi", u2) 
        self.assertEqual(msg.receiver, u2)  

    def test_str(self):
        """Test string representation of Message."""
        u1 = User("u1", "p", "s", "e")  
        u2 = User("u2", "p", "s", "e")  
        msg = Message(u1, "Hi", u2)  
        expected = "Message - Activity - User: u1, Content: Hi, Receiver: u2"  
        self.assertEqual(str(msg), expected) 

class TestUser(unittest.TestCase):
    """Test cases for the User class."""
    # Add more test cases for other methods and classes
    
    def setUp(self):
        """Set up test fixtures."""
        self.user = User("user1", "password1", "User One", "user1@example.com") # 🍕 create user instance

    def test_init(self):
        """Test initialization of User."""
        self.assertEqual(self.user.profile.username, "user1")  # 🙂 CHECK PROFILE CREATION
        self.assertEqual(self.user.posts, [])  # 🙂 CHECK EMPTY POST LIST
        self.assertEqual(self.user.messages, [])  # 🙂 CHECK EMPTY MSG LIST

    def test_create_post(self):
        """Test creating a post for a user."""
        post = self.user.create_post("Test Post Content") # 🍕 create post
        # Check if the post is added to the user's posts list
        self.assertIn(post, self.user.posts) # 🍕 check post in list
        # Check if the user is correct
        self.assertEqual(post.user, self.user) # 🍕 check user equality
        # Check if the content of the post is correct
        self.assertEqual(post.content, "Test Post Content") # 🍕 check content equality

    def test_create_post_empty(self):
        """Test creating a post with empty content."""
        with self.assertRaises(ValueError):  # 🙂 EXPECT VALUE ERROR
            self.user.create_post("")  # 🙂 TRY EMPTY CONTENT

    def test_send_message(self):
        """Test sending a message."""
        receiver = User("u2", "p", "s", "e")  # 🙂 CREATE RECEIVER
        msg = self.user.send_message(receiver, "Hello")  # 🙂 SEND MESSAGE
        self.assertIn(msg, self.user.messages)  # 🙂 CHECK MSG IN LIST
        self.assertEqual(msg.receiver, receiver)  # 🙂 CHECK RECEIVER

    def test_send_message_empty(self):
        """Test sending a message with invalid inputs."""
        receiver = User("u2", "p", "s", "e")  # 🙂 CREATE RECEIVER
        with self.assertRaises(ValueError):  # 🙂 EXPECT VALUE ERROR
            self.user.send_message(receiver, "")  # 🙂 TRY EMPTY CONTENT
        with self.assertRaises(ValueError):  # 🙂 EXPECT VALUE ERROR
            self.user.send_message(None, "Hi")  # 🙂 TRY EMPTY RECEIVER

    def test_str(self):
        """Test string representation of User."""
        expected = "User - Profile - Username: user1, Screen Name: User One, Email: user1@example.com"  # 🙂 DEFINE EXPECTED STRING
        self.assertEqual(str(self.user), expected)  # 🙂 CHECK STRING OUTPUT

if __name__ == "__main__": # 🍕 check main execution
    unittest.main() # 🍕 run tests