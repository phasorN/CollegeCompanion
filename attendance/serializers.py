from rest_framework import serializers
from attendance import models


class SubjectSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source="user.username")

    def create(self, validated_data):
        self.is_valid(raise_exception=True)
        print("Validated Data:")
        print(validated_data)
        return models.Subject.objects.create(**validated_data)

    class Meta:
        model = models.Subject
        fields = ('id', 'title', 'percentage')


class UserFilteredPrimaryKeyRelatedFieldPeriod(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        return models.Subject.objects.filter(user=request.user)


class UserFilteredPrimaryKeyRelatedKeyAttendance(serializers.SlugRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        subjects = models.Subject.objects.filter(user=request.user)
        i = 0
        for s in subjects:
            if i == 0:
                period_qs = models.Period.objects.filter(subject=s)
            else:
                period_qs = period_qs | models.Period.objects.filter(subject=s)
            i = i+1
        print(period_qs)
        return period_qs


class PeriodSerializer(serializers.ModelSerializer):
    subject = UserFilteredPrimaryKeyRelatedFieldPeriod()

    # def create(self, validated_data):
    #     subject_id = validated_data.pop('subject_id')
    #     subject = models.Subject.objects.get(id = subject_id)
    #     print(validated_data)
    #     print(subject)
    #     return models.Period.objects.create(**validated_data, subject=subject)

    class Meta:
        model = models.Period
        fields = ('id', 'subject', 'time', 'day', 'venue', 'period_number')


class AttendanceSerializer(serializers.ModelSerializer):
    period = UserFilteredPrimaryKeyRelatedKeyAttendance(slug_field='id')

    class Meta:
        model = models.Attendance
        fields = ('id', 'period', 'date', 'value_int', 'value_str')
