package main
import "fmt"
 
func location(city string) (region, continent string) {
	switch city { 
	case "Los Angeles", "LA", "Santa Monica":
		region, continent = "California", "North America"
	case "New York", "NYC": 
		region, continent = "New York", "North America"
	default:
		region, continent = "Unknown", "Unknown"
	} 
	return //returning region and continent
} 

func main() { 
	region, continent := location("Santa Monica")
	fmt.Printf("Matt lives in %s, %s", region, continent)
}