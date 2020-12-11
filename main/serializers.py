from rest_framework import serializers


class Finance(serializers.ModelSerializer):
    
    
    
    class User: 
        model = Finance
        fields = ( 'user_ID', 'budget_ID', 'email', 'password' 'name')
    
    class