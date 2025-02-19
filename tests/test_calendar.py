"""Test calendar utilities."""
import calendar

import pandas as pd
import pytest

from assess_gtfs.calendar import create_calendar_from_dates


class TestCreateCalendarFromDates(object):
    """Tests for create_calendar_from_dates."""

    def test_create_calendar_from_dates_defence(self):
        """Test defensive checks for create_calendar_from_dates."""
        with pytest.raises(TypeError, match=".DataFrame'>. Got <class 'int'>"):
            create_calendar_from_dates(calendar_dates=1)
        with pytest.raises(
            IndexError, match="service_id' is not a column in the dataframe."
        ):
            create_calendar_from_dates(
                calendar_dates=pd.DataFrame({"foo": 0}, index=[0])
            )

    def test_create_calendar_passes_no_exception_type_2(self):
        """Check output calendar is as expected without exception_type 2."""
        mock_dates = pd.DataFrame(
            {
                "service_id": ["00A", "00A", "00A"],
                "date": ["19840426", "19840427", "20240426"],
                "exception_type": [1, 1, 1],
            }
        )
        out_calendar = create_calendar_from_dates(mock_dates)
        assert isinstance(
            out_calendar, pd.DataFrame
        ), f"Expected dataframe, found {type(out_calendar)}"
        n_rows = len(out_calendar)
        assert n_rows == 1, f"Expected df length 1, found {n_rows}"
        # check values are as expected. Dates are Thu & Fri respectively.
        exp_calendar = pd.DataFrame(
            {
                "service_id": ["00A"],
                "monday": [0],
                "tuesday": [0],
                "wednesday": [0],
                "thursday": [1],
                "friday": [1],
                "saturday": [0],
                "sunday": [0],
                "start_date": ["19840426"],
                "end_date": ["20240426"],
            },
            index=[0],
        )
        weekdays = [day.lower() for day in calendar.day_name]
        for nm in exp_calendar.columns:
            if nm in weekdays:
                exp_calendar[nm] = exp_calendar[nm].astype("int8")
        pd.testing.assert_frame_equal(
            out_calendar,
            exp_calendar,
        )

    def test_create_calendar_passes_with_exception_type_2(self):
        """Check output calendar is as expected with exception_type 2."""
        mock_dates = pd.DataFrame(
            {
                "service_id": ["00A", "00B", "00B"],
                "date": ["19840426", "20240426", "19840426"],
                "exception_type": [1, 2, 1],
            }
        )
        out_calendar = create_calendar_from_dates(mock_dates)
        exp_calendar = pd.DataFrame(
            {
                "service_id": ["00A", "00B"],
                "monday": [0, 0],
                "tuesday": [0, 0],
                "wednesday": [0, 0],
                "thursday": [1, 1],
                "friday": [0, 0],
                "saturday": [0, 0],
                "sunday": [0, 0],
                "start_date": ["19840426", "19840426"],
                "end_date": ["19840426", "19840426"],
            },
            index=[0, 1],
        )
        weekdays = [day.lower() for day in calendar.day_name]
        for nm in exp_calendar.columns:
            if nm in weekdays:
                exp_calendar[nm] = exp_calendar[nm].astype("int8")
        assert isinstance(
            out_calendar, pd.DataFrame
        ), f"Expected dataframe, found {type(out_calendar)}"
        n_rows = len(out_calendar)
        assert n_rows == 2, f"Expected df length 2, found {n_rows}"
        # check the exception type 2 value didn't impact the table
        assert (
            out_calendar.iloc[1, -1] != "20240426"
        ), "Did not expect date 20240426 to appear in out calendar."
        assert (
            out_calendar.loc[1, "friday"] == 0
        ), "Did not expect calendar to show service 00B to runs on Friday."
        # check values are as expected. Dates are Thu & Fri respectively.
        pd.testing.assert_frame_equal(
            out_calendar,
            exp_calendar,
        )
