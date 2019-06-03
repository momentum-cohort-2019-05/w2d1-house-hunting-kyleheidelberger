
total_weight = 0
weight_limit = 100

while True:
    bag_weight_as_str = input(
        "How much does your bag weight in pounds? (Hit Enter if you are done) ")
    if bag_weight_as_str == "":
        break
        
    else:
        bag_weight = int(bag_weight_as_str)
        total_weight += bag_weight
        print("Your weight so far is " str(total_weight) + ".")

if total_weight > weight_limit:
    print("Warning! You are over the weight limit by" + str(total_weight - weight_limit) + " pounds.")