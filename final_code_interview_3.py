def calculate_hotel_stays(num_hotels, hotels, hours_required, budget, commission, discount, is_premium, tax, with_food):
    valid_hotels = []
    for i in range(num_hotels):
        hotel_id = hotels[i][0]
        min_duration = hotels[i][1]
        min_duration_cost = hotels[i][2]
        incremental_duration = hotels[i][3]
        incremental_duration_cost = hotels[i][4]
       
        
        if hours_required < min_duration:
            total_cost = min_duration_cost
        else:
            additional_hours = hours_required - min_duration
            additional_duration_cost = incremental_duration_cost * (additional_hours // incremental_duration)
            if additional_hours % incremental_duration != 0:
                additional_duration_cost += incremental_duration_cost
            total_cost = min_duration_cost + additional_duration_cost
        
        if with_food == 'Y':
            total_cost += food_amount
        
        if is_premium == 'P':
            total_cost = total_cost - (discount * total_cost / 100)
        
        total_cost = total_cost + (commission * total_cost / 100)
        total_cost = total_cost + (tax * total_cost / 100)
        
        if total_cost <= budget:
            valid_hotels.append((hotel_id, total_cost))
    
    if not valid_hotels:
        print("No hotels found within budget")
    else:
        valid_hotels.sort(key=lambda x: x[1])
        for hotel in valid_hotels:
            print(hotel[0], hotel[1], sep=' ')
            
            
num_hotels = int(input())
hotels = []
for i in range(num_hotels):
    hotel = []
    for j in range(6):
        hotel.append(int(input()))
    hotels.append(hotel)

hours_required = int(input())
budget = int(input())
commission = int(input())
discount = int(input())
is_premium = input()
tax = int(input())


calculate_hotel_stays(num_hotels, hotels, hours_required, budget, commission, discount, is_premium, tax, with_food)
