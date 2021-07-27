from django_seed import Seed
from qa.models import QuestionManager, Question, Answer

seeder = Seed.seeder('en_US')

seeder.add_entity(User, 5)
seeder.add_entity(Answer, 25)
seeder.add_entity(Question, 40)


inserted_pks = seeder.execute()
