from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Entry, Participant, Result, Survey_result
from .serializers import EntryQuesSerializer, ParticipantSerializer, EntryYesSerializer, EntryNoSerializer, \
    ResultSerializer, SurveySerializer
import random
from rest_framework.decorators import action
from django.db.models import F


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    @action(detail=False, methods=['POST'])
    def post_answer_training(self, request):
        participant = Participant.objects.get(participant_id=request.data['id'])
        entry = Entry.objects.get(id=request.data['question'])

        Result.objects.create(worker_id=participant, user_points=request.data['score'], agent_points=0,
                              bought_information=request.data['yes_no'], round_num=request.data['round'],
                              training_question=True, entry_id=entry, buy_info_decision_time=0)
        participant.training_round = participant.training_round + 1
        participant.save()
        return Response("result created", status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def post_answer_game(self, request):
        participant = Participant.objects.get(participant_id=request.data['id'])
        entry = Entry.objects.get(id=request.data['question'])
        entry.used_count = entry.used_count + 1
        entry.save()
        Result.objects.create(worker_id=participant, user_points=request.data['score'], agent_points=0,
                              bought_information=request.data['yes_no'], round_num=request.data['round'],
                              training_question=False, entry_id=entry, buy_info_decision_time=0)
        participant.game_round = participant.game_round + 1
        participant.save()
        return Response("result created", status=status.HTTP_200_OK)


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntryQuesSerializer

    @action(detail=False, methods=['POST'])
    def get_another_game_ent(self, request):
        participant = Participant.objects.get(participant_id=request.data['id'])
        if participant.game_round > 20:
            return Response(False, status=status.HTTP_200_OK)
        ent_obj = Entry.objects.filter(used_count__lte=1)
        random_ent = random.sample(list(ent_obj), 1)
        serializer = EntryQuesSerializer(random_ent, many=True)
        serializer.data[0]['round'] = participant.game_round
        return Response(serializer.data[0], status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def get_another_training_ent(self, request):
        participant = Participant.objects.get(participant_id=request.data['id'])
        if participant.training_round == 1:
            ent_obj = Entry.objects.filter(sold_with__gt=F('z') * F('voi') + F('sold_without'))
            random_ent = random.sample(list(ent_obj), 1)
            serializer = EntryQuesSerializer(random_ent, many=True)
            serializer.data[0]['round'] = 1
            return Response(serializer.data[0], status=status.HTTP_200_OK)
        if participant.training_round == 2:
            ent_obj = Entry.objects.filter(sold_with__lt=F('sold_without'))
            random_ent = random.sample(list(ent_obj), 1)
            serializer = EntryQuesSerializer(random_ent, many=True)
            serializer.data[0]['round'] = 2
            return Response(serializer.data[0], status=status.HTTP_200_OK)
        ent_obj = Entry.objects.all()
        random_ent = random.sample(list(ent_obj), 1)
        serializer = EntryQuesSerializer(random_ent, many=True)
        serializer.data[0]['round'] = participant.training_round
        return Response(serializer.data[0], status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_first(self, request):
        ent_obj = Entry.objects.filter(sold_with__gt=F('z') * F('voi') + F('sold_without'))
        random_ent = random.sample(list(ent_obj), 1)
        serializer = EntryQuesSerializer(random_ent, many=True)
        return Response(serializer.data[0], status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_second(self, request):
        ent_obj = Entry.objects.filter(sold_with__lt=F('sold_without'))
        random_ent = random.sample(list(ent_obj), 1)
        serializer = EntryQuesSerializer(random_ent, many=True)
        return Response(serializer.data[0], status=status.HTTP_200_OK)


class EntryYesViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntryYesSerializer

    @action(detail=False, methods=['POST'])
    def get_bidders(self, request):
        entry = Entry.objects.get(id=request.data['id'])
        entrys_sum = []
        if entry.s == 1:
            entrys_sum = [entry.v11, entry.v21, entry.v31, entry.v41, entry.v51]
        if entry.s == 2:
            entrys_sum = [entry.v12, entry.v22, entry.v32, entry.v42, entry.v52]
        if entry.s == 3:
            entrys_sum = [entry.v13, entry.v23, entry.v33, entry.v43, entry.v53]
        if entry.s == 4:
            entrys_sum = [entry.v14, entry.v24, entry.v34, entry.v44, entry.v54]
        if entry.s == 5:
            entrys_sum = [entry.v15, entry.v25, entry.v35, entry.v45, entry.v55]
        if entry.s == 6:
            entrys_sum = [entry.v16, entry.v26, entry.v36, entry.v46, entry.v56]
        if entry.s == 7:
            entrys_sum = [entry.v17, entry.v27, entry.v37, entry.v47, entry.v57]

        entrys_count = [0, 0, 0, 0, 0]
        for i in range(1, entry.y + 1):
            if i == entry.n1:
                entrys_count[i - 1] = entrys_count[i - 1] + 1
            if i == entry.n2:
                entrys_count[i - 1] = entrys_count[i - 1] + 1
            if i == entry.n3:
                entrys_count[i - 1] = entrys_count[i - 1] + 1
            if i == entry.n4:
                entrys_count[i - 1] = entrys_count[i - 1] + 1
            if i == entry.n5:
                entrys_count[i - 1] = entrys_count[i - 1] + 1
            if i == entry.n6:
                entrys_count[i - 1] = entrys_count[i - 1] + 1
            if i == entry.n7:
                entrys_count[i - 1] = entrys_count[i - 1] + 1
            if i == entry.n8:
                entrys_count[i - 1] = entrys_count[i - 1] + 1
        type_json = {'t1': entrys_count[0], 't2': entrys_count[1], 't3': entrys_count[2], 't4': entrys_count[3],
                     't5': entrys_count[4], 't1_bid': entrys_sum[0], 't2_bid': entrys_sum[1], 't3_bid': entrys_sum[2],
                     't4_bid': entrys_sum[3], 't5_bid': entrys_sum[4]}
        return Response(type_json, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def get_yes(self, request):
        entry = Entry.objects.get(id=request.data['question'])
        serializer = EntryYesSerializer(entry, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EntryNoViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntryNoSerializer

    @action(detail=False, methods=['POST'])
    def get_bidders(self, request):
        entry = Entry.objects.get(id=request.data['id'])
        entrys_sum = [0, 0, 0, 0, 0]
        entrys_count = [0, 0, 0, 0, 0]

        if entry.n1 == 1:
            entrys_count[0] = entrys_count[0] + 1
            entrys_sum[0] = entry.n1_without
        if entry.n1 == 2:
            entrys_count[1] = entrys_count[1] + 1
            entrys_sum[1] = entry.n1_without
        if entry.n1 == 3:
            entrys_count[2] = entrys_count[2] + 1
            entrys_sum[2] = entry.n1_without
        if entry.n1 == 4:
            entrys_count[3] = entrys_count[3] + 1
            entrys_sum[3] = entry.n1_without
        if entry.n1 == 5:
            entrys_count[4] = entrys_count[4] + 1
            entrys_sum[4] = entry.n1_without

        if entry.n2 == 1:
            entrys_count[0] = entrys_count[0] + 1
            entrys_sum[0] = entry.n2_without
        if entry.n2 == 2:
            entrys_count[1] = entrys_count[1] + 1
            entrys_sum[1] = entry.n2_without
        if entry.n2 == 3:
            entrys_count[2] = entrys_count[2] + 1
            entrys_sum[2] = entry.n2_without
        if entry.n2 == 4:
            entrys_count[3] = entrys_count[3] + 1
            entrys_sum[3] = entry.n2_without
        if entry.n2 == 5:
            entrys_count[4] = entrys_count[4] + 1
            entrys_sum[4] = entry.n2_without

        if entry.n3 == 1:
            entrys_count[0] = entrys_count[0] + 1
            entrys_sum[0] = entry.n3_without
        if entry.n3 == 2:
            entrys_count[1] = entrys_count[1] + 1
            entrys_sum[1] = entry.n3_without
        if entry.n3 == 3:
            entrys_count[2] = entrys_count[2] + 1
            entrys_sum[2] = entry.n3_without
        if entry.n3 == 4:
            entrys_count[3] = entrys_count[3] + 1
            entrys_sum[3] = entry.n3_without
        if entry.n3 == 5:
            entrys_count[4] = entrys_count[4] + 1
            entrys_sum[4] = entry.n3_without

        if entry.n4 == 1:
            entrys_count[0] = entrys_count[0] + 1
            entrys_sum[0] = entry.n4_without
        if entry.n4 == 2:
            entrys_count[1] = entrys_count[1] + 1
            entrys_sum[1] = entry.n4_without
        if entry.n4 == 3:
            entrys_count[2] = entrys_count[2] + 1
            entrys_sum[2] = entry.n4_without
        if entry.n4 == 4:
            entrys_count[3] = entrys_count[3] + 1
            entrys_sum[3] = entry.n4_without
        if entry.n4 == 5:
            entrys_count[4] = entrys_count[4] + 1
            entrys_sum[4] = entry.n4_without

        if entry.n5 == 1:
            entrys_count[0] = entrys_count[0] + 1
            entrys_sum[0] = entry.n5_without
        if entry.n5 == 2:
            entrys_count[1] = entrys_count[1] + 1
            entrys_sum[1] = entry.n5_without
        if entry.n5 == 3:
            entrys_count[2] = entrys_count[2] + 1
            entrys_sum[2] = entry.n5_without
        if entry.n5 == 4:
            entrys_count[3] = entrys_count[3] + 1
            entrys_sum[3] = entry.n5_without
        if entry.n5 == 5:
            entrys_count[4] = entrys_count[4] + 1
            entrys_sum[4] = entry.n5_without

        if entry.n6 == 1:
            entrys_count[0] = entrys_count[0] + 1
            entrys_sum[0] = entry.n6_without
        if entry.n6 == 2:
            entrys_count[1] = entrys_count[1] + 1
            entrys_sum[1] = entry.n6_without
        if entry.n6 == 3:
            entrys_count[2] = entrys_count[2] + 1
            entrys_sum[2] = entry.n6_without
        if entry.n6 == 4:
            entrys_count[3] = entrys_count[3] + 1
            entrys_sum[3] = entry.n6_without
        if entry.n6 == 5:
            entrys_count[4] = entrys_count[4] + 1
            entrys_sum[4] = entry.n6_without

        if entry.n7 == 1:
            entrys_count[0] = entrys_count[0] + 1
            entrys_sum[0] = entry.n7_without
        if entry.n7 == 2:
            entrys_count[1] = entrys_count[1] + 1
            entrys_sum[1] = entry.n7_without
        if entry.n7 == 3:
            entrys_count[2] = entrys_count[2] + 1
            entrys_sum[2] = entry.n7_without
        if entry.n7 == 4:
            entrys_count[3] = entrys_count[3] + 1
            entrys_sum[3] = entry.n7_without
        if entry.n7 == 5:
            entrys_count[4] = entrys_count[4] + 1
            entrys_sum[4] = entry.n7_without

        if entry.n8 == 1:
            entrys_count[0] = entrys_count[0] + 1
            entrys_sum[0] = entry.n8_without
        if entry.n8 == 2:
            entrys_count[1] = entrys_count[1] + 1
            entrys_sum[1] = entry.n8_without
        if entry.n8 == 3:
            entrys_count[2] = entrys_count[2] + 1
            entrys_sum[2] = entry.n8_without
        if entry.n8 == 4:
            entrys_count[3] = entrys_count[3] + 1
            entrys_sum[3] = entry.n8_without
        if entry.n8 == 5:
            entrys_count[4] = entrys_count[4] + 1
            entrys_sum[4] = entry.n8_without
        type_json = {'t1': entrys_count[0], 't2': entrys_count[1], 't3': entrys_count[2], 't4': entrys_count[3],
                     't5': entrys_count[4], 't1_bid': entrys_sum[0], 't2_bid': entrys_sum[1], 't3_bid': entrys_sum[2],
                     't4_bid': entrys_sum[3], 't5_bid': entrys_sum[4]}
        return Response(type_json, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def get_no(self, request):
        entry = Entry.objects.get(id=request.data['question'])
        serializer = EntryNoSerializer(entry, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    @action(detail=False, methods=['POST'])
    def add_participant(self, request):
        participant = Participant.objects.create(age=request.data['age'], gender=request.data['gender'],
                                                 education=request.data['education'],
                                                 nationality=request.data['nationality'], instructions_time="-1",
                                                 training_time="-1",
                                                 game_time="-1", bonus=0, bonus_payed=False, HITId="-1",
                                                 AssignmentId="-1",
                                                 round_pass_instructions=1, instructions_score=0)
        return Response(participant.participant_id, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def is_participant(self, request):
        try:
            participant = Participant.objects.get(participant_id=request.data['id'])
            if participant.round_pass_instructions > 3:
                return Response(False, status=status.HTTP_200_OK)
            return Response(True, status=status.HTTP_200_OK)
        except Participant.DoesNotExist:
            return Response(False, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def pass_instructions(self, request):
        try:
            participant = Participant.objects.get(participant_id=request.data['id'])
            if participant.round_pass_instructions > 3 or participant.instructions_score < 7:
                return Response(False, status=status.HTTP_200_OK)
            return Response(True, status=status.HTTP_200_OK)
        except Participant.DoesNotExist:
            return Response(False, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def update_score(self, request):
        participant = Participant.objects.get(participant_id=request.data['id'])
        participant.instructions_score = request.data['score']
        participant.instructions_time = request.data['time']
        if request.data['score'] < 7:
            participant.round_pass_instructions = participant.round_pass_instructions + 1
        participant.save()
        if participant.round_pass_instructions > 3:
            return Response(False, status=status.HTTP_200_OK)
        return Response(True, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def get_round(self, request):
        participant = Participant.objects.get(participant_id=request.data['id'])
        return Response(participant.training_round, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def get_round_game(self, request):
        participant = Participant.objects.get(participant_id=request.data['id'])
        return Response(participant.game_round, status=status.HTTP_200_OK)


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey_result.objects.all()
    serializer_class = SurveySerializer

    @action(detail=False, methods=['POST'])
    def add_survey(self, request):
        participant = Participant.objects.get(participant_id=request.data['id'])
        survey1 = Survey_result.objects.create(answer=request.data['q1'],
                                               question='Overall, how satisfied were you with this HIT?',
                                               worker_id=participant)
        survey2 = Survey_result.objects.create(answer=request.data['q2'],
                                               question='What was your attention span when you did the HIT?',
                                               worker_id=participant)
        survey3 = Survey_result.objects.create(answer=request.data['q3'],
                                               question='Are you happy with the bonus?(2$)', worker_id=participant)
        survey4 = Survey_result.objects.create(answer=request.data['q4'],
                                               question='Do you have any comments?', worker_id=participant)
        return Response("survey save", status=status.HTTP_200_OK)
