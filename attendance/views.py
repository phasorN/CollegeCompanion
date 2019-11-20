from attendance.serializers import SubjectSerializer
from attendance import models
from attendance import serializers

from rest_condition import And, Or

from rest_framework import generics, permissions


class IsUserItself(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.user)
        return obj.user == request.user


class IsPostRequest(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == "POST"


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsPeriodOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.subject.user == request.user


class IsAttendanceOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.period.subject.user == request.user


class SubjectCreateListView(generics.ListCreateAPIView):
    # Any authenticated user can GET: List all his subjects.
    #                       and POST: Add new subject.
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.SubjectSerializer

    def get_queryset(self):
        return models.Subject.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PeriodCreateListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.PeriodSerializer

    def get_queryset(self):
        queryset_full = []
        subjects = models.Subject.objects.filter(user=self.request.user)
        # print(subjects.first())
        i = 0
        for s in subjects:
            if i == 0:
                queryset_full = models.Period.objects.filter(subject=s)
            else:
                queryset_temp = models.Period.objects.filter(subject=s)
                queryset_full = queryset_full | queryset_temp

            i = i + 1
            return queryset_full.order_by('day', 'time')

        return []
        # print(models.Period.objects.filter(subject=subjects.first()))
        # return models.Period.objects.filter(subject=subjects.first())


class AttendanceCreateListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.AttendanceSerializer

    # queryset = models.Attendance.objects

    def get_queryset(self):
        periods = []
        subjects = models.Subject.objects.filter(user=self.request.user)
        i = 0
        for s in subjects:
            if i == 0:
                periods = models.Period.objects.filter(subject=s)
            else:
                queryset_temp = models.Period.objects.filter(subject=s)
                periods = periods | queryset_temp

            i = i + 1
        # periods = models.Period.objects.filter(subject=subjects.first())
        print(periods)
        # return periods
        if len(periods) > 0:
            queryset_full = models.Attendance.objects.filter(period=periods[0])
        else:
            queryset_full = []
        print(type(queryset_full))
        for p in periods:
            print(p.subject.title + " | " + str(p.id))
            queryset_temp = models.Attendance.objects.filter(period=p)
            print(queryset_temp)
            queryset_full = queryset_full | queryset_temp
        print(queryset_full)
        return queryset_full


class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [And(permissions.IsAuthenticated, IsOwner)]
    serializer_class = SubjectSerializer

    def get_queryset(self):
        return models.Subject.objects

        # If we use code given below, then subjects of other users will give 404
        # But the above code will give 403
        # because it will check the IsOwner permission on all the subjects in the model.

        # return models.Subject.objects.filter(user=self.request.user)


class PeriodDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [And(permissions.IsAuthenticated,
                              IsPeriodOwner  # Period object does not contain .user attribute,
                              # Period.subject contains user attribute.
                              )
                          ]
    serializer_class = serializers.PeriodSerializer
    queryset = models.Period.objects


class AttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [And(permissions.IsAuthenticated,
                              IsAttendanceOwner  # Attendance object does not contain .user attribute,
                              # Attendance.subject contains user attribute.
                              )]
    serializer_class = serializers.AttendanceSerializer

    queryset = models.Attendance.objects
