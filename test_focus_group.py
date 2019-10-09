from unittest import TestCase

from focus_group import FocusGroup, ColumnNames, Posture, Status

SEP = '_' * 80


class TestFocusGroup(TestCase):

    def test_init(self):
        focusGroup = FocusGroup()
        df = focusGroup.df
        print(df.head())
        print(df[ColumnNames.DIASTOLIC])
        print(SEP)

        sitting_group = FocusGroup(poster_filter=Posture.sitting)
        sitting_df = sitting_group.df
        print(sitting_df[ColumnNames.DIASTOLIC])
        print(SEP)

        standing_group = FocusGroup(poster_filter=Posture.standing)
        standing_df = standing_group.df
        print(standing_df[ColumnNames.DIASTOLIC])
        print(SEP)

        normal_group = FocusGroup(status_filter=Status.normal)
        normal_df = normal_group.df
        print(normal_df[ColumnNames.DIASTOLIC])
        print(SEP)

        anxious_group = FocusGroup(status_filter=Status.anxiety)
        anxious_df = anxious_group.df
        print(anxious_df[ColumnNames.DIASTOLIC])
        print(SEP)
