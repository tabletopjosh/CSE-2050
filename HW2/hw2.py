class Profile:
    """Class representing a user's profile."""
    
    def __init__(self, username, password, screen_name, email):
        """
        Initialize a Profile instance.

        Args:
            username (str): The username.
            password (str): The password.
            screen_name (str): The screen name.
            email (str): The email address.
        """
        self.username = username  
        self.password = password  
        self.screen_name = screen_name  
        self.email = email  

    def modify_profile(self, password=None, screen_name=None, email=None):
        """
        Modify user's profile information.

        Args:
            password (str, optional): New password.
            screen_name (str, optional): New screen name.
            email (str, optional): New email.
        """
        if password: 
            self.password = password  
        if screen_name: 
            self.screen_name = screen_name 
        if email: 
            self.email = email  

    def __str__(self):
        """ Return a string representation of the Profile."""
        return f"Profile - Username: {self.username}, Screen Name: {self.screen_name}, Email: {self.email}" 

class Activity:
    """Base class representing an activity."""
    
    def __init__(self, user, content):
        """
        Initialize an Activity instance.

        Args:
            user (User): The user associated with the activity.
            content (str): The content of the activity.
        """
        self.user = user  
        self.content = content 

    def __str__(self):
        """ Return a string representation of the Activity."""
        return f"Activity - User: {self.user.profile.username}, Content: {self.content}" 


class Post(Activity):
    """Class representing a user's post."""
    def __init__(self, user, content):
        """ Initialize a Post instance. """
        super().__init__(user, content) #

    def __str__(self):
        """ Return a string representation of the Post. """
        return f"Post - {super().__str__()}" 
    

class Message(Activity):
    """Class representing a user's message to another user."""
    
    def __init__(self, user, content, receiver):
        """
        Initialize a Message instance.

        Args:
            user (User): The sender.
            content (str): The message content.
            receiver (User): The recipient.
        """
        super().__init__(user, content)  
        self.receiver = receiver 

    def __str__(self):
        """ Return a string representation of the Message."""
        return f"Message - {super().__str__()}, Receiver: {self.receiver.profile.username}" 


class User:
    """Class representing a user in the social network."""
    
    def __init__(self, username, password, screen_name, email):
        """
        Initialize a User instance.

        Args:
            username (str): The username.
            password (str): The password.
            screen_name (str): The screen name.
            email (str): The email address.
        """
        self.profile = Profile(username, password, screen_name, email)  
        self.posts = []  
        self.messages = []  

    def create_post(self, content):
        """Create a new post for the user.
        Args:
            content (str): The content of the post.

        Returns:
            Post: The created post.

        Raises:
            ValueError: If the content of the post is empty.
        """
        if not content:  
            raise ValueError("Post content cannot be empty.") 
        
        new_post = Post(self, content) 
        self.posts.append(new_post)  
        return new_post 

    def send_message(self, receiver, content):
        """Send a message from the user to the specified receiver.

        Args:
            receiver (User): The user receiving the message.
            content (str): The content of the message.

        Returns:
            Message: The created message.

        Raises:
            ValueError: If the receiver ID or message content is empty.
        """
        if not content or not receiver: 
            raise ValueError("Receiver and content required.")  
            
        new_message = Message(self, content, receiver)  
        self.messages.append(new_message)  
        return new_message  

    def __str__(self):
        """ Return a string representation of the User."""
        return f"User - {self.profile}" 

# Example usage:
if __name__ == "__main__": 
    user1 = User("user1", "password1", "User One", "user1@example.com") 
    user2 = User("user2", "password2", "User Two", "user2@example.com")

    post1 = user1.create_post("This is my first post!") 
    message1 = user2.send_message(user1, "Hi User One! How are you?") 
    print(post1) 
    print(message1) 
    user1.profile.modify_profile(email="User1_1@uconn.edu") 
    print(user1) 
    print(user2)