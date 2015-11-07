ifeq ($(OS),Windows_NT)
	RM=del
else
	RM=rm -f
endif

INCLUDE=include
BUILD=build
SRC=src

# Compiler flags
CFLAGS= -g -Wall -Wextra -O3

# Choose your favorite compiler
#CC = gcc $(CFLAGS)
CC = clang $(CFLAGS)

OBJECTS=$(BUILD)/imsl

all: $(OBJECTS)

$(OBJECTS): $(SRC)/*.c
	$(CC) -I $(INCLUDE)/*.h $< -o $@

.PHONY: clean

clean:
	rm -f $(BUILD)/*.o

