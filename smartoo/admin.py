from django.contrib import admin
from knowledge.models import Vertical, Topic, KnowledgeBuilder
from exercises.models import Exercise, ExerciseGrades
from exercises.models import ExercisesCreator, ExercisesGrader

# models admin registration
admin.site.register(Vertical)
admin.site.register(Topic)
admin.site.register(KnowledgeBuilder)
admin.site.register(Exercise)
admin.site.register(ExerciseGrades)
admin.site.register(ExercisesCreator)
admin.site.register(ExercisesGrader)
