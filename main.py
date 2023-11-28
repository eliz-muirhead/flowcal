import datetime
import period
from period_handler import PeriodHandler
import utils
from dateutil import parser


def load_historic_data():
    periods = []
    with open("historical-data.csv", "r+") as historical_data:
        for line in historical_data:
            start_end_dates = line.split(",")
            try:
                start = parser.parse(start_end_dates[0]).date()
                end = parser.parse(start_end_dates[1]).date()
                historic_period = period.Period(start, end)
                periods.append(historic_period)
            except IndexError:
                start = parser.parse(start_end_dates[0])
                end = handle_current_period(start)
                if end is not None:
                    historical_data.write(f",{end}")
    period_handler = PeriodHandler(periods)
    return period_handler


def handle_current_period(start):
    started = input(f"Did you have a period that started: {start.date()} (y/n)?").lower()
    if started == "y":
        finished = input(f"Has it end yet (y/n)?")
        if finished == "y":
            end_input = input("Enter the end date in the YYYY-MM-DD format or type \"today\": ")
            end = utils.parse_date_from_command_line(end_input)
            return end
    if started == "n":
        utils.erase_stray_date()


def predict_next_period(last_period, average_cycle):
    today = datetime.datetime.today()
    next_start = last_period.start + datetime.timedelta(days=average_cycle)
    days = (next_start - today.date()).days
    return next_start, days


def report_period_start():
    new_period = []
    start_date = input("Enter the start date in the YYYY-MM-DD format or type \"today\": ")
    start = utils.parse_date_from_command_line(start_date)
    new_period.append(start)
    ended_input = input("Has your period ended yet (y/n)?")

    if ended_input.lower() == "y":
        end_date = input("Enter the data date in the YYYY-MM-DD format or type \"today\": ")
        end = utils.parse_date_from_command_line(end_date)
        new_period.append(end)

    utils.write_to_file(new_period)


def command_line():
    new = input("To record a new period type \"new\" ")
    if new == "new":
        report_period_start()


def print_most_recent(period_handler):
    last_period = period_handler.get_most_recent_complete()
    print(f"Most recent period started on {last_period.start} and ended on {last_period.end}")

    average_period = period_handler.compute_average_length_of_period()
    print(f"Average length of period: {average_period} days")

    average_cycle = period_handler.compute_average_length_of_cycle()
    print(f"Average length of cycle: {average_cycle} days")

    (start_date, days) = predict_next_period(last_period, average_cycle)
    print(f"Your next period is predicted to start in {days} days on {start_date}")


if __name__ == '__main__':
    period_handler = load_historic_data()
    print_most_recent(period_handler)
    command_line()
