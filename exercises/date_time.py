import datetime

now = datetime.datetime.now()
print("Current time and date: ")
print(now.strftime("%H:%M:%S %m/%d/%Y"))

# datetime.strftime strcuture
"""

    %Y: year with century as a decimal number.
    %m: month as a zero-padded decimal number.
    %d: day of the month as a zero-padded decimal number.
    %H: hour (24-hour clock) as a zero-padded decimal number.
    %M: minute as a zero-padded decimal number.
    %S: second as a zero-padded decimal number.

"""