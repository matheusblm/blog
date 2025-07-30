package main

import "net/http"
import "fmt"
import "encoding/json"
import "time"


type Course struct {
	Name string `json:"name"`
	Desc string `json:"desc"`
	Price int	`json:"price"`
}

func (c Course) GetFullInfo() string {
	return fmt.Sprintf("Nome: %s, Desc: %s, Price: %d", c.Name, c.Desc, c.Price)
}




func counter() {
	for i := 0; i < 10; i++ {
		fmt.Println(i)
		time.Sleep(time.Second)
	}
}

func main(){
	// course := Course{
	// 	Name: "Full Cycle",
	// 	Desc: "Curso de Go",
	// 	Price: 100,
	// }

	// fmt.Println(course.GetFullInfo())
	// http.HandleFunc("/", home)
	// http.ListenAndServe(":8080", nil)
	go counter()
	go counter()
	counter()
}

func home(w http.ResponseWriter, r *http.Request){
		course := Course{
		Name: "Full Cycle",
		Desc: "Curso de Go",
		Price: 100,
	}

	json.NewEncoder(w).Encode(course)
}