from rest_framework import serializers
from .models import Entry, Participant, Result, Survey_result


class EntryQuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'x', 'y', 'w', 'z', 'voi',
                  'v11', 'v12', 'v13', 'v14', 'v15', 'v16', 'v17',
                  'v21', 'v22', 'v23', 'v24', 'v25', 'v26', 'v27',
                  'v31', 'v32', 'v33', 'v34', 'v35', 'v36', 'v37',
                  'v41', 'v42', 'v43', 'v44', 'v45', 'v46', 'v47',
                  'v51', 'v52', 'v53', 'v54', 'v55', 'v56', 'v57', 'used_count']


class EntryYesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'x', 'y', 'w', 'z', 'voi', 's',
                  'v11', 'v12', 'v13', 'v14', 'v15', 'v16', 'v17',
                  'v21', 'v22', 'v23', 'v24', 'v25', 'v26', 'v27',
                  'v31', 'v32', 'v33', 'v34', 'v35', 'v36', 'v37',
                  'v41', 'v42', 'v43', 'v44', 'v45', 'v46', 'v47',
                  'v51', 'v52', 'v53', 'v54', 'v55', 'v56', 'v57', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8',
                  'n1_with', 'n2_with', 'n3_with', 'n4_with', 'n5_with', 'n6_with', 'n7_with', 'n8_with', 'sold_with',
                  'sold_without', 'used_count']


class EntryNoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'x', 'y', 'w', 'z', 'voi', 's',
                  'v11', 'v12', 'v13', 'v14', 'v15', 'v16', 'v17',
                  'v21', 'v22', 'v23', 'v24', 'v25', 'v26', 'v27',
                  'v31', 'v32', 'v33', 'v34', 'v35', 'v36', 'v37',
                  'v41', 'v42', 'v43', 'v44', 'v45', 'v46', 'v47',
                  'v51', 'v52', 'v53', 'v54', 'v55', 'v56', 'v57', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8',
                  'n1_without', 'n2_without', 'n3_without', 'n4_without', 'n5_without', 'n6_without', 'n7_without',
                  'n8_without', 'sold_without', 'used_count']


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['participant_id']


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey_result
        fields = ['id', 'question', 'answer', 'worker_id']


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['id', 'user_points', 'agent_points', 'bought_information', 'buy_info_decision_time', 'round_num',
                  'training_question', 'worker_id', 'entry_id']
