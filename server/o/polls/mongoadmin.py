from mongonaut.sites import MongoAdmin

# Import your custom models
from polls.models import Choice, Poll, Lady, User

# Instantiate the MongoAdmin class
# Then attach the mongoadmin to your model
Poll.mongoadmin = MongoAdmin()
Choice.mongoadmin = MongoAdmin()
Lady.mongoadmin = MongoAdmin()
#User.mongoadmin = MongoAdmin()