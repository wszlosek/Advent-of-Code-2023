package utils

import (
	"log"
	"os"
	"strconv"
	"strings"
)

func ReadLines(path string) []string {
	data, err := os.ReadFile(path)
	if err != nil {
		log.Fatal(err)
	}

	lines := strings.Split(string(data), "\n")
	return lines
}

func ToInt(str string) (int, error) {
	return strconv.Atoi(str)
}

func ToString(integer int) string {
	return strconv.Itoa(integer)
}

func GetKeys(m map[string]int) []string {
	var keys []string
	for key := range m {
		keys = append(keys, key)
	}
	return keys
}
