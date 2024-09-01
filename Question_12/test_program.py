from tour import Tour
from hotel import Hotel


hotel_package = Hotel(nights=5 , cost_per_night=200)
tour_package = Tour( days=7 ,cost_per_day=100 )

hotel_package.display_package_cost()
tour_package.display_package_cost()