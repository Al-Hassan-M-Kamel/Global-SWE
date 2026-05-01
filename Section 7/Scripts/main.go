package main

import (
	"bytes"
	"encoding/json"
	"net/http"
)

type User struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

func main() {

	users := []User{
		{Name: "Ali", Age: 22},
		{Name: "Ahmed", Age: 23},
	}

	jsonData, _ := json.Marshal(users)

	resp, err := http.Post("http://127.0.0.1:5000/rec", "application/json", bytes.NewBuffer(jsonData))

	if err != nil{
		panic(err)
	}
	
	defer resp.Body.Close()
}
