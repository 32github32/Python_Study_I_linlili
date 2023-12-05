house_work_count = int(input ("house_work_count:"))
red_envelope_count = int(input ("red_envelope_count:"))
shopping_count = int(input ("shopping_count:"))
has_been_angry = int(input ("has_been_angry:"))

if (house_work_count>10 and red_envelope_count>1 and shopping_count>4 and not has_been_angry):
    print("receive switch")
else:
    print("lose switch")