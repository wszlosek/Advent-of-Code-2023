package main

import (
	"log"
	"os"
	"strconv"
	"strings"
)

func readLines(path string) []string {
	data, err := os.ReadFile(path)
	if err != nil {
		log.Fatal(err)
	}

	lines := strings.Split(string(data), "\n")
	return lines
}

func toInt(str string) (int, error) {
	return strconv.Atoi(str)
}

func toString(integer int) string {
	return strconv.Itoa(integer)
}

func getKeys(m map[string]int) []string {
	var keys []string
	for key := range m {
		keys = append(keys, key)
	}
	return keys
}
