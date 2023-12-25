from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields ='__all__'
  
	def validate_title(self, value):
		if not value.startswith("Task:"):
			raise serializers.ValidationError("Task title must start with 'Task:'")
		return value